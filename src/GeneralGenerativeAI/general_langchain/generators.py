from langchain_openai import ChatOpenAI

class GeneralLangchainGenerators:
    def set_OpenAI_llm(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

    def generate_text(self, prompt: str) -> str:
        response = self.llm.predict(prompt)
        return response