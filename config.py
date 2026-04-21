
# General configuration 

LLM = "llama3.1:8b"
OLLAMA_SERVER = "http://localhost:11434"
EMBEDDINGS = "BAAI/bge-small-en-v1.5"
CHROMADB_PATH = "data/chroma_db"
DATA_PATH = "data/raw"

COLLECTION_NAME = "documents"
CHUNK_SIZE = 256
CHUNK_OVERLAP = int( ( CHUNK_SIZE * 10 ) / 100 )
RETRIEVE = 3