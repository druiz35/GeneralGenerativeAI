import os

class GeneralGenerativeAICredentials:
    def __init__(self):
        self.huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")