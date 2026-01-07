from src.vector_store import VectorStoreBuilder
# this is the vector store builder class that we have created in the vector_store.py file
from src.recommender import AnimeRecommender
# this is the recommender class that we have created in the recommender.py file
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
# this is the logger class that we have created in the logger.py file
from utils.custom_exception import CustomException
# this is the custom exception class that we have created in the custom_exception.py file

logger = get_logger(__name__)
# logger is initialized here

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        # uses the persist_dir , where the vector data store is 
        try:
            logger.info("Intializing Recommdation Pipeline")
            # track custom exceptions

            vector_builder = VectorStoreBuilder(csv_path="" , persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
            # this pipeline is used for generating the responses
        


        