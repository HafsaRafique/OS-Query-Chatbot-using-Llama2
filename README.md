# Medical-Chatbot-using-Llama2
This repository contains code to set up a medical chatbot using the LLaMA 2 model. The chatbot extracts data from a PDF file, processes it, and responds to medical inquiries based on the extracted data. The implementation uses LangChain and HuggingFace libraries, along with a vector database (Pinecone) to handle the embeddings.

## Requirements
To run this project, you'll need to install the necessary libraries in requirements.txt or you may need to install more as you go. Make sure to install the correct versions as specified to avoid any compatibility issues. Some features might be deprecated, for that refer to the following documentations:
[Langchain](https://python.langchain.com/v0.2/docs/integrations/platforms/huggingface/)
[Pinecone](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pinecone/)

## Environment Setup
You'll need to go to Anaconda command prompt, create an environment using:

> conda create -r medicalchatbot

> conda activate medicalchatbot

> code .


## Steps
Note that to this chatbot is just extracting data from a pdf file, so we need to extract data from the pdf file and use it for further processing. The main steps to building this bot are as follows:
1. Load the PDF file and extract the data from it.
2. Extract text chunks from the pdf file, this is because llama 2 has a token limit.
3. Load the embedding model and perform embedding on the text chunks.
4. Pass these embeddings to a vector database.
You are likely to encounter an error here, although I have resolved it using PineconeVectorStore, I recommend restarting your kernel. Incase, it is deprecated you may read the following documentation for help [Pinecone](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pinecone/).
6. Pass the vector data to the LLM.

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

<p align="center">
<image src="https://github.com/HafsaRafique/Medical-Chatbot-using-Llama2/images/medical_chatbot.png">
</p>


