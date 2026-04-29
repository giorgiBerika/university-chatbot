from sentence_transformers import SentenceTransformer
from v1_manual.config import EMBEDDINGS 


def embed_chunks( chunks ):
    model = SentenceTransformer(EMBEDDINGS) 

    texts = [] 

    for chunk in chunks:
        texts.append(chunk.page_content)

    embeddings = model.encode(texts)

    return embeddings

