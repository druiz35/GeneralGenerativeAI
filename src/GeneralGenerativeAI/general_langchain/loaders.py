from langchain_community.document_loaders import CSVLoader

class GeneralLangChainLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        loader = CSVLoader(file_path=self.file_path)
        documents = loader.load()
        return documents