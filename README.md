
# Equity-News-Research-Tool 

An AI-powered Equity News Research Tool built using LangChain, OpenAI, FAISS, and Streamlit for intelligent financial news analysis and question answering.
This tool allows users to input financial news article URLs, process the content using Large Language Models (LLMs), and ask natural language questions to receive relevant answers along with source references.

![](rockybot.jpg)

## Features

- Load and analyze financial news articles through URLs
- Extract article content using LangChain's UnstructuredURLLoader
- Split and preprocess text for efficient retrieval
- Generate embeddings using OpenAI Embeddings
- Store and index embeddings using FAISS for fast similarity search
- Ask questions in natural language and receive AI-generated answers
- Display relevant source URLs along with responses
- User-friendly Streamlit interface for easy interaction
- Save FAISS vector database locally for future retrieval


## Tech Stack

  - Python
  - Streamlit
  - LangChain
  - OpenAI API
  - FAISS
  - dotenv


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Desilva93/Equity-News-Research-Tool.git
```

### 2. Navigate to the project directory

```bash
cd Equity-News-Research-Tool
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API Key

Create a `.env` file in the project root directory and add:

```bash
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

After launching:

1. The Streamlit app opens in your browser.
2. Enter financial news article URLs in the sidebar.
3. Click **Process URLs** to load and process articles.
4. The system performs:
   - Text splitting
   - Embedding generation
   - FAISS vector indexing
5. Ask questions related to the news articles.
6. Receive AI-generated answers with supporting source URLs.


---

## Example Use Case

Input news articles related to:

- Stock market trends
- Company earnings
- Financial reports
- Market analysis
- Economic news

Example questions:

- What is the market sentiment around Tata Motors?
- What are the key financial highlights mentioned?
- Which companies are expected to grow according to these reports?

---


## Project Structure

- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- faiss_store_openai.pkl: A pickle file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.
