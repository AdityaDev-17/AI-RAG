#load pdf
#split into chunks
#create the embeddings
# store in chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

data = PyPDFLoader(r"U:\AI\AIProjects\AI-RAG\document loaders\deeplearning.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = splitter.split_documents(docs)

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding = embedding_model,
    persist_directory = "chroma_db"
)