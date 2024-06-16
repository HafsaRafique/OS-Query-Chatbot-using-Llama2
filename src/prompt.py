prompt_template="""
Use the following information to answer the users question
If you don't know the answer, just say that you are a text model that hasn't been trained for that data, don't try to make up an answer.
Context:{context}
Question:{question}
only return a useful answer and nothing else.
Useful answer:

"""