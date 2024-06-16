from src.helper import load_pdf, text_chunk_create, getting_embedding_model
from langchain_pinecone import PineconeVectorStore
import pinecone
from dotenv import load_dotenv
import os
load_dotenv()
PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
print(PINECONE_API_KEY)

extracted_files= load_pdf("Data/")
text_chunks= text_chunk_create(extracted_files)
print(text_chunks)
embeddings= getting_embedding_model()
print(embeddings)
index_name="medical-chatbot"



docsearch = PineconeVectorStore.from_documents(text_chunks, embedding=embeddings, index_name=index_name)

