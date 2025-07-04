from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from langserve import add_routes

import os
from dotenv import load_dotenv
load_dotenv()

groq_apikey=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="gemma2-9b-It")

# creating prompt template

from langchain_core.prompts import ChatPromptTemplate

generic_temp="Translate the following into {language}"

prompt=ChatPromptTemplate.from_messages(
    [("system",generic_temp),
     ("user","{text}")],

)
 # parser
parser=StrOutputParser()

#create chain, LCEL

chain=prompt|model|parser


## APP DEFINITION
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interafces")



#adding chains routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn 
    uvicorn.run(app,host="localhost",port=8000)







