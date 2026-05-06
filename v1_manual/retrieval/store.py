import chromadb 
from config import CHROMADB_PATH


def store_data( chunks, data ):
    
    chroma_client = chromadb.PersistentClient(path=CHROMADB_PATH) 
    collection = chroma_client.get_or_create_collection(name="iliauni_info")

    chunks_len = len(chunks)

    collection.add(
        ids=[f"chunk_{num}" for num in range(chunks_len) ],
        documents=[chunks[num].page_content for num in range(chunks_len)],
        embeddings=data.tolist(),
        metadatas=[chunks[num].metadata for num in range(chunks_len)]

    )