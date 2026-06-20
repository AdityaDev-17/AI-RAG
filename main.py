from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

template = ChatPromptTemplate.from_messages([
    ("system","You are a AI that summaarizes the content of the document provided to you."),
    ("human","{data}")
])

model = ChatMistralAI(model="mistral-small-2506")
