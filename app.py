from src.data_loader import load_all_doc
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# from src.embedding import EmbeddingPipeline

# from src.vectorstore
# from src.search 


if __name__ == "__main__":
    
    # data_dir = "data"
    # documents = load_all_doc(data_dir)
           
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(documents)
    store.load()
    # print(store.query("what skills in Maged Cv ?", top_k=3))
    
    rag = RAGSearch(persist_dir="faiss_store")
    query = "Summarize the key skills and experiences mentioned in the documents."
    summary = rag.search_and_summarize(query, top_k=3)
    print("Summary:\n", summary)    
    
    
    
    
    # chunks = EmbeddingPipeline().chunk_documents(documents)
    # embeddings = EmbeddingPipeline().embed_chunks(chunks)
    
    # print(f"Total chunks created: {len(chunks)}")
    
    # print(f"Total documents loaded: {len(documents)}")
    
    # print(f"Embeddings shape: {embeddings.shape}")
    
    # print("embedding : ", embeddings)
    
    
    # print("Embedding pipeline completed successfully.")