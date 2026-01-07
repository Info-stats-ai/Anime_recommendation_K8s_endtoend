from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)
        # groq will ask for three things
        # apikey, model name, temperature
        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type = "stuff",
            # stuff is used to pass the entire context to the model from the prompt 
            # we don't want to pass the context to the model in chunks
            retriever = retriever,
            return_source_documents = True,
            # we want to return the source documents to the user
            chain_type_kwargs = {"prompt":self.prompt}
            # this means that we want to use the prompt that we have created in the prompt_template.py file
        )

    def get_recommendation(self,query:str):
        # here quey is the user question
        result = self.qa_chain({"query":query})
        return result['result']
        # result['result'] is the answer to the user's question