from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.retrieval_qa.base import RetrievalQA

import streamlit as st

load_dotenv()

df = pd.read_csv('data/product.csv')
content = df.to_string(index=False)
documents = [Document(page_content=content)]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
docs = text_splitter.split_documents(documents)

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
persist_dir = "./chroma_db_csv"
if os.path.exists(persist_dir):
    vectordb = Chroma(persist_directory=persist_dir,embedding_function=embedding)
else:
    vectordb=Chroma.from_documents(docs,embedding,persist_directory="./chroma_db_csv")
    vectordb.persist()

llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-70b-8192"
    
    )

retriever=vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm,retriever=retriever)

st.title('Llama Chatbot')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.chat_message('assistant'):
    st.markdown('Hi! Ask me anything about your dataset.')

for i,(user_msg,bot_msg) in enumerate(st.session_state.chat_history):
    with st.chat_message('user',avatar='🧑‍💻'):
        st.markdown(user_msg)
    with st.chat_message('assistant',avatar='🤖'):
        st.markdown(bot_msg)

user_input = st.chat_input("Type your questions here..")

if user_input:
    with st.chat_message('user',avatar='🧑‍💻'):
        st.markdown(user_input)
    with st.chat_message('assistant',avatar='🤖'):
        with st.spinner("Thinking..."):
            response = qa_chain.run(user_input)
            st.markdown(response)

st.session_state.chat_history.append((user_input,response))
    

