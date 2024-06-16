from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import os
from langchain_pinecone import PineconeVectorStore
import dotenv
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

index_name = "medical-chatbot"

def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents= loader.load()
    return documents

def text_chunk_create(extracted_files):
     text_chunker= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
     text_chunk= text_chunker.split_documents(extracted_files)
     return text_chunk

#Embedding Step:
def getting_embedding_model():
    embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
