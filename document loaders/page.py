from langchain_community.document_loaders import WebBaseLoader

url = "https://en.wikipedia.org/wiki/Machine_learning"

data = WebBaseLoader(url)

docs = data.load()

print(len(docs))