import chromadb
from rag.embeddings import create_embedding

client = chromadb.PersistentClient(path="hr_chroma_db")
collection = client.get_or_create_collection(name="hr_documents")

def add_documents(chunks, source):
    for index, chunk in enumerate(chunks):
        collection.add(
            ids=[f"{source}_{index}"],
            documents=[chunk],
            embeddings=[create_embedding(chunk)],
            metadatas=[{"source": source}]
        )

def retrieve_context(question):
    if collection.count() == 0:
        return ""
    results = collection.query(
        query_embeddings=[create_embedding(question)],
        n_results=3
    )
    docs = results.get("documents", [])
    return "\n\n".join(docs[0]) if docs else ""
