import os
import streamlit as st
import pickle
import time
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)

st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()

llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:

    #load data

    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    # split data

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )

    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)

    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    #time.sleep(2)

    # Save FAISS properly
    vectorstore_openai.save_local("vector_index")

query = main_placeholder.text_input("Question: ")
    
if query:

    if os.path.exists("vector_index"):

        # Load FAISS properly
        embeddings = OpenAIEmbeddings()

        vectorstore = FAISS.load_local("vector_index",embeddings,allow_dangerous_deserialization=True)

        # Create Retrieval QA chain
        chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm,retriever=vectorstore.as_retriever())

        # Get answer
        result = chain.invoke({"question": query})

        # Display answer
        st.header("Answer")
        st.write(result["answer"])

        # Display sources
        sources = result.get("sources", "")

        if sources:
            st.subheader("Sources:")

            sources_list = sources.split("\n")

            for source in sources_list:
                st.write(source)
