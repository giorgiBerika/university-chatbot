from sentence_transformers import SentenceTransformer
from config import EMBEDDINGS 


def embed_chunks( chunks ):
    model = SentenceTransformer(EMBEDDINGS) 

    texts = [] 

    for chunk in chunks:
        texts.append(chunk.page_content)

    embeddings = model.encode(texts)

    return embeddings


