from ingestion.loader import load_data 
from ingestion.chunking import make_chunks
from ingestion.embedder import embed_chunks 
from retrieval.store import store_data 

def run_ingestion( path ):

    data = load_data( path ) # list of dicts { "text": content, "source": filename }
    chunks = make_chunks( data )
    embeddings = embed_chunks( chunks )
    store_data( chunks, embeddings)

