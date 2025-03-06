# PDF Assistant using Phidata 📄🤖

Welcome to the PDF Assistant using Phidata repository! This project leverages the [Phidata](https://github.com/phidatahq/phidata) framework to create an intelligent assistant capable of reading, analyzing, and interacting with PDF documents. By integrating advanced language models, the assistant can extract information, summarize content, and answer questions related to the provided PDFs.

## Overview 📝

The PDF Assistant utilizes Phidata's capabilities to build a multimodal agent equipped with memory, knowledge, tools, and reasoning. This allows the assistant to process and understand complex PDF documents, providing users with accurate and relevant information.

## Features ✨

- **PDF Content Extraction**: The assistant can extract text and data from PDF files, enabling further analysis and interaction.
- **Content Summarization**: Generates concise summaries of lengthy PDF documents, highlighting key points and insights.
- **Question Answering**: Allows users to ask questions about the content of the PDF, providing accurate and context-aware responses.
- **Custom Tool Integration**: Supports the addition of custom tools to enhance functionality, such as making API calls or performing web searches.

## Getting Started 🚀

To set up and run the PDF Assistant locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Rohit-Madhesiya/Pdf-Assistant-using-Phidata.git
   cd Pdf-Assistant-using-Phidata

2. **Create a Virtual Environment:**

It's recommended to use a virtual environment to manage dependencies:

  ```bash
  python3 -m venv env
  source env/bin/activate  # On Windows, use 'env\Scripts\activate'
  ```

3. **Install Dependencies:**

Install the required Python libraries:

  ```bash
  pip install -r requirements.txt
  ```

4. **Run the PDF Assistant:**

Execute the main script to start the assistant:

  ```bash
  python pdf_assistant.py
  ```

## Usage 🛠️

Once the assistant is running, you can interact with it through the console or integrate it into other applications. The assistant accepts natural language queries related to the content of the PDF, such as:

* "Summarize the main findings of this research paper."
* "What are the key points discussed in this legal document?"
* "Extract all tables from this financial report."

The assistant will process these queries and provide detailed, structured responses.

## Customization 🔧

You can customize the assistant's behavior by modifying the pdf_assistant.py script. For instance, you can add or remove tools, adjust the assistant's memory settings, or integrate additional data sources. Refer to the [Phidata documentation](https://github.com/phidatahq/phidata) for guidance on extending assistant functionalities.
