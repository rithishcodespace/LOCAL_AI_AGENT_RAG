# here we are vectorising our csv file making it into the form of list and storing in the desired file path using chroma db
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import langchain_chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model = "mxbai-embed-large")

db_location = "./chroma_langchain_db" #path to store data
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content = row["title"] + " " + row["Review"],
            metadata = {"rating": row["rating"], "date": row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "restaurant_reviews",
    persistent_directory = db_location,
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents = documents, ids = ids)