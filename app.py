from flask import Flask, render_template, jsonify, request
from src.helper import get_embeddings
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain.vectorstores import pinecone
import os
from src.prompt import *

app= Flask(__name__)
load_dotenv()
PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV= os.environ.get('PINECONE_API_ENV')

embeddings= get_embeddings()
index_name="bot"

docsearch= PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)

PROMPT= PromptTemplate(template=prompt_template, input_variables=["context","question"])
chain_t_kwargs={"prompt":PROMPT}

llm= CTransformers(model="model\llama-2-7b-chat.ggmlv3.q4_0.bin", model_type="llama", config={'max_new_tokens':512, 'temperature':0.8})

questionanswer= RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={'k':2}), return_source_documents=True, chain_type_kwargs=chain_t_kwargs)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = questionanswer.invoke({"query": input})
    print("Response: ", result["result"])
    
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True) 