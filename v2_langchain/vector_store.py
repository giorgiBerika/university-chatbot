from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 

from v2_langchain.config import ( CHUNK_SIZE, CHUNK_OVERLAP, 
                    DATA_PATH, CHROMADB_PATH, 
                    EMBEDDINGS, RETRIEVE )

def build_vector_store():
    loader = DirectoryLoader( DATA_PATH, glob="**/*.txt", loader_cls=TextLoader )

    docs = loader.load()


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents( docs )
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDINGS)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMADB_PATH
    )

def get_retriever():
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDINGS)
    vectordb = Chroma(
        persist_directory=CHROMADB_PATH, 
        embedding_function=embedding_model
    )

    return vectordb.as_retriever(search_kwargs={"k" : RETRIEVE})