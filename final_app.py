from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
import streamlit as st 
import time 
import os

# Load Nvidia Api Key
os.environ['NVIDIA_API_KEY'] = "Enter your NVIDIA API key here"

# Calling the LLM model
llm = ChatNVIDIA(model_name = "nvidia/llama-3.1-nemotron-ultra-253b-v1")   # NVIDIA NIM Inferencing Model

# Creating vector embeddings
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = NVIDIAEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("./data", glob="*.pdf")  
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 700, chunk_overlap = 50)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:30])  # taking top 30 records
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        
# Creating title
st.title("🧠💚🖥️ NVIDIA LLM Chatbot")
st.subheader("Chatbot using NVIDIA LLM and Langchain")

# Creating prompt temlpate
prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "Answer the question based on the provided context only.\n"
     "Please provide the most accurate response based on the question.\n"
     "<context>\n{context}\n</context>"),
    ("human", "Question: {input}")
])

question = st.text_input("Ask a question about the PDF documents")

if st.button("Document Embeddings"):
    vector_embedding()
    st.success("Document embeddings created successfully using NVIDIA Embeddings")
    st.balloons()
    
if question:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({"input": question}) 
    print("Response time:", time.process_time() - start)
    st.write(response['answer'])
    
    # With streamliot expander
    with st.expander("Document similarity search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("----------------------------------------------------------------") 
