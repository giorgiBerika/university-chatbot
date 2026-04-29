from v1_manual.ingestion.loader import load_data 
from v1_manual.ingestion.chunking import make_chunks
from v1_manual.ingestion.embedder import embed_chunks 
from v1_manual.retrieval.store import store_data 

def run_ingestion( path ):

    data = load_data( path ) # list of dicts { "text": content, "source": filename }
    chunks = make_chunks( data )
    embeddings = embed_chunks( chunks )
    store_data( chunks, embeddings)

