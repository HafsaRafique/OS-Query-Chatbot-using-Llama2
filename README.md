# Query-Chatbot-using-Llama2
This repository contains code to set up a query chatbot using the Llama 2 model. The chatbot extracts data from a PDF file, processes it, and responds to inquiries based on the extracted data. The implementation uses LangChain and HuggingFace libraries, along with a vector database (Pinecone) to handle the embeddings.

## Requirements
To run this project, you'll need to install the necessary libraries in requirements.txt or you may need to install more as you go. Make sure to install the correct versions as specified to avoid any compatibility issues. Some features might be deprecated, for that refer to the following documentations:
[Langchain](https://python.langchain.com/v0.2/docs/integrations/platforms/huggingface/), 
[Pinecone](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pinecone/)

Download the LLM from this link:
[Llama2](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin)


## Environment Setup
You'll need to go to Anaconda command prompt, create an environment using:

> conda create -r chatbot

> conda activate chatbot

> code .


## Steps
Note that to this chatbot is just extracting data from a pdf file, so we need to extract data from the pdf file and use it for further processing. The main steps to building this bot are as follows:
1. Load the PDF file and extract the data from it.
2. Extract text chunks from the pdf file, this is because llama 2 has a token limit.
3. Load the embedding model and perform embedding on the text chunks.
4. Pass these embeddings to a vector database. It should look something like this:
   
<p align="center">
<image src="https://github.com/HafsaRafique/OS-Query-Chatbot-using-Llama2/blob/main/images/pinecone.png" width="800">
</p>
  
You are likely to encounter an error here, although I have resolved it using PineconeVectorStore, I recommend restarting your kernel. Incase, it is deprecated you may read the following documentation for help [Pinecone](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pinecone/).

5. Pass the vector data to the LLM.


## User Interface
We deploy our frontend using Flask. For this we followed a basic syntax:

>app =Flask(__name__)

>@app.route("/")

>def index():
>
>    return render_template('chat.html')
>
> if __name__ == '__main__':
>
>   app.run(host="0.0.0.0", port= 8080, debug= True)

## Results

Firstly, we test out the model by asking a relevant question: 

<p align="center">
<image src="https://github.com/HafsaRafique/OS-Query-Chatbot-using-Llama2/blob/main/images/query_chatbot.png" width="500">
</p>

We can see the resulting output has been fetched by the model from the vector store. 


## Note
1. Incase you get the following error: 

pydantic.error_wrappers.ValidationError: 1 validation error for RetrievalQA
retriever
Can't instantiate abstract class BaseRetriever with abstract methods _get_relevant_documents (type=type_error)

You'll need to upgrade your langchain version to 0.1.9. You will get a lot of deprecation warnings and incompatibility warnings, ignore them for now. Your application should run smoothly.

2. Access you page by typing either http://127.0.0.1:8080 or http://10.2.0.2:8080.

3. The model takes about 17-18 mins to respond, so you'll need some patience if you don't have a GPU.

4. For guidance refer to this link [Chatbot](https://www.youtube.com/watch?v=Fe5B90R8DTg&t=2021s)   

