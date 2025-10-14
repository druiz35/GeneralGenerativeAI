from langchain_community.vectorstores import FAISS

class GeneralLangChainVectorStores:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vector_store = None

    def create_FAISS_vector_store(self, documents):
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        return self.vector_store

    def clear_vector_store(self):
        self.vector_store = None
    
    def search(self, query, k=5):
        if self.vector_store is None:
            raise ValueError("Vector store has not been created yet.")
        return self.vector_store.similarity_search(query, k=k)