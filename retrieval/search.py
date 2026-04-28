from sentence_transformers import SentenceTransformer
import chromadb
from config import CHROMADB_PATH, EMBEDDINGS, RETRIEVE

model = SentenceTransformer(EMBEDDINGS)
def search_in_db( user_question ):
   
    chroma_client = chromadb.PersistentClient(path=CHROMADB_PATH)
    collection = chroma_client.get_or_create_collection(name="iliauni_info")


    embedding = model.encode( user_question )
    
    return collection.query(
        query_embeddings=embedding,
        n_results=RETRIEVE
    )
    