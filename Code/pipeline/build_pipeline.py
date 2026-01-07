from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv" , "data/anime_updated.csv")
        # anime upadted data is after processing the data
        processed_csv = loader.load_and_process()
# store the processed.csv
        logger.info("Data  loaded and processed...")
# build the vector store
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
# vector store is built sucesfully
# as it is not returning any value , we don't need to store it in a variable
        logger.info("Vector store Built sucesfully....")

        logger.info("Pipelien built sucesfully....")
    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error during pipeline " , e)
    
if __name__=="__main__":
     main()
# creating a vector store using the build_pipeline.py file
# pipeline.py is loading the vectors form the store 
# but here we generating those vectors

