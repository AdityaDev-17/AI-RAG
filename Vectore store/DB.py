from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

docs = [
    Document(page_content="Python is Widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in python.", metadata={"source": "DataSciecne_book"}), 
    Document(page_content="Neural networks are used in Deep Learning.", metadata={"source": "DL_book"})
]

embedding_model = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents = docs, 
    embedding = embedding_model,
    persist_directory = "chroma_db" 
    )

result = vectorstore.similarity_search("What is used for  data analysis?", k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver = vectorstore.as_retriever()
docs  = retriver.invoke("Explain Deep Learning")

for d in docs:
    print(d.page_content)
    print(d.metadata)
