# Ollama Neural Studio — Local AI Chatbot

A locally running AI chatbot built with Python and Streamlit, powered by Ollama and open-source language models.

## Overview

Ollama Neural Studio provides a conversational interface for interacting with locally hosted language models. Users can select a model, adjust the temperature, customize the system instruction, and maintain conversation history during a session.

## Features

- Interactive chat interface using Streamlit
- Local language model inference through Ollama
- Streaming responses
- Model selection from the supported model list
- Adjustable temperature and system instructions
- Conversation history maintained during the session
- Reset conversation context
- Error handling for unavailable Ollama services and model requests

## Technology Stack

- Python
- Streamlit
- Requests
- Ollama
- Locally hosted language models

## Architecture

User → Streamlit Interface → Python Application → Ollama API → Local Language Model → Streamed Response

## Prerequisites

- Python installed on your computer
- Ollama installed and running
- At least one supported model downloaded
- Sufficient memory and system resources for the selected model

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tamil-coder/offline-customer-support-rag-chatbot.git
   cd offline-customer-support-rag-chatbot
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it on Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Download the default model:

   ```bash
   ollama pull llama3.2
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

Open the local URL printed by Streamlit in your browser.

## How to Use

1. Ensure Ollama is running.
2. Select a downloaded model in the sidebar.
3. Adjust the temperature or system instruction if needed.
4. Enter a question in the chat input.
5. View the streamed response.
6. Use Reset Context to start a fresh conversation.

## Current Limitations

- Requires Ollama and a compatible local model.
- Only models installed locally can be used successfully.
- Conversation history is stored in Streamlit session state.
- Document-based retrieval and RAG are not currently implemented.
- Response quality and performance depend on the selected model and hardware.

## Future Improvements

- Add automated tests.
- Improve request timeouts and error reporting.
- Add document ingestion and retrieval for a genuine RAG workflow.
- Evaluate response quality using a defined set of test questions.
- Add a demo screenshot and more detailed setup documentation.

## Author

Tamil Selvi

GitHub: https://github.com/Tamil-coder
