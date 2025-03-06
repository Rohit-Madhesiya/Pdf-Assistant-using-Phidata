import streamlit as st
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
import os
from dotenv import load_dotenv
import tempfile

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

def initialize_session_state():
  if "messages" not in st.session_state:
    st.session_state.messages=[]
  if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base=None
  if "assistant" not in st.session_state:
    st.session_state.assistant=None
  if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed=None

def upload_pdf(uploaded_file):
  # create temp dir
  with tempfile.TemporaryDirectory()  as tempdir:
    # save uploaded file to temp dir
    temp_pdf_path=os.path.join(tempdir,uploaded_file.name)
    with open(temp_pdf_path,"wb") as file:
      file.write(uploaded_file.getbuffer())
    
    # initialize knowledge base with temp file
    st.session_state.knowledge_base=PDFUrlKnowledgeBase(
      urls=[temp_pdf_path],
      vector_db=PgVector2(
        collection="user_pdf",
        db_url=db_url
      )
    )

    # load the knowledge base
    with st.spinner("Processing PDF..."):
      st.session_state.knowledge_base.load(recreate=True,upsert=True)
    
    # init assistant with new knowledge base
    st.session_state.assistant=Assistant(
      knowledge_base=st.session_state.knowledge_base,
      storage=PgAssistantStorage(table_name="pdf_assistant",db_url=db_url),
      show_tool_calls=True,
      search_knowledge=True,
      read_chat_history=True
    )
    st.session_state.pdf_processed=True
    return True
  

def main():

  st.set_page_config(page_title="PDF Assistant",page_icon="📚",layout="wide")
  st.title("PDF Assistant")

  os.environ['OPENAI_API_KEY']=st.sidebar.text_input("OPENAI API KEY",type="password")

  initialize_session_state()

  with st.sidebar:
    st.header("Upload PDF")
    uploaded_file=st.file_uploader("Choos a PDF File",type="pdf")

    if uploaded_file:
      if st.button("Process PDF"):
        success=upload_pdf(uploaded_file)
        if success:
          st.success("PDF processed successfully!")
          st.session_state.messages=[] #clear chat history for new PDF file
        

  if not st.session_state.pdf_processed:
    st.info("Please upload and process a PDF file to start chatting")
    return 

  for message in st.session_state.messages:
    with st.chat_message(message['role']):
      st.write(message['content'])
  
  # chat input
  if prompt:=st.chat_input("Ask about you PDF..."):
    # add user msg to chat history
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
      st.write(prompt)
    
    # get assistant response
    with st.chat_message("assistant"):
      try:
        with st.spinner("Thinking..."):
          response=st.session_state.assistant.chat(prompt)
          st.write(response)
          st.session_state.messages.append({"role":"assistant","content":response})
      except Exception as e:
        st.error(f"An error occurred: str{e}")
  
  # button to clear chat history
  if st.button("Clear Chat"):
    st.session_state.message=[]
    st.rerun()

if __name__=="__main__":
  main()
    

  

