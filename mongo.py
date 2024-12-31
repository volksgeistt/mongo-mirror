from pymongo import MongoClient
import logging

def cloneDatabase(sourceURL: str, otherURL: str):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        sourceUser = MongoClient(sourceURL)
        otherUser = MongoClient(otherURL)
        
        sourceDB = sourceUser.get_default_database()
        if not sourceDB:
            raise ValueError("The Provided Source Connection Has No Specified DATABASE.")
        
        dbName = sourceDB.name
        otherDB = otherUser[dbName]
        logger.info(f"Connected To DATABASE — Cloning — {dbName}")
        
        allCollections = sourceDB.list_collection_names()
        for collectionName in allCollections:
            logger.info(f"Processing collection — {collectionName}")
            sourceCollection = sourceDB[collectionName]
            otherCollection = otherDB[collectionName]
            
            documents = list(sourceCollection.find({}))
            if documents:
                logger.info(f"Found `{len(documents)}` Docs In — {collectionName}")
                otherCollection.insert_many(documents)
                logger.info(f"Transferred — {collectionName}")
            else:
                logger.info(f"Collection `{collectionName}` is empty")
                
        logger.info("Database Cloned — Successfully")
        
    except Exception as e:
        logger.error(f"Error While Cloning — {str(e)}")
        raise
    finally:
        sourceUser.close()
        otherUser.close()
        logger.info("Database Connection — Closed")


if __name__ == "__main__":
    sourceURL = "mongodb://your_source_connection_string"
    otherURL = "mongodb://your_destination_connection_string"
    
    cloneDatabase(sourceURL, otherURL)
