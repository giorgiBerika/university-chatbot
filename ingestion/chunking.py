from ingestion.loader import load_data
from config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP 

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter




def make_chunks( ):
    content = load_data( DATA_PATH )
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )

    document_list = []
    for doc in content:
        document = Document(
            page_content=doc['text'], metadata={"source": doc['source']}
        )

        document_list.append(document)

    return text_splitter.split_documents(document_list)


