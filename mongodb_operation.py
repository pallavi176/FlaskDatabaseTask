import pymongo
from custom_logger import CustomLogger

class MyMongo:
    log = CustomLogger.log("mongo.log")

    def __init__(self,db_name,coll_name):
        """
        This will initialize the connection
        """
        try:
            self.client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sg1qp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            self.db = self.create_database(db_name)
            self.coll = self.create_collection(coll_name)
            self.log.info("Connection created with mongo db atlas")
        except Exception as e:
            print(e)
            self.log.exception(str(e))

    def show_databases(self):
        """
        This method will show all the databases present
        """
        try:
            self.log.info("Listing all the databases ")
            db_list = self.client.list_database_names()
            self.log.info(f"Databases available are: {db_list}")
            return db_list
        except Exception as e:
            print(e)
            self.log.exception(str(e))

    def create_database(self,db_name):
        """
        This method will create database
        """
        try:
            self.log.info(f"Creating database: {db_name}")
            db = self.client[db_name]
            return db
        except Exception as e:
            print(e)
            self.log.exception(str(e))

    def create_collection(self,coll_name):
        """
        This method will create collection
        """
        try:
            self.log.info(f"Creating collection: {coll_name} in database: {self.db}")
            collection = self.db[coll_name]
            return collection
        except Exception as e:
            print(e)
            self.log.exception(str(e))

    def select_all_docs(self,query=None):
        """
        This method will select & return all the documents from the collection
        """
        try:
            self.log.info(f"selecting all the documents from the collection: {self.coll}")
            data_list = []
            if query:
                if isinstance(query, dict):
                    data_list = [i for i in self.coll.find(query)]
                else:
                    self.log.error("Raising exception since dictionary query is not passed in select_all_docs")
                    raise Exception(f"You have not entered a dictionary query: {query} in select_all_docs")
            else:
                data_list = [i for i in self.coll.find()]
            if data_list:
                return data_list
            else:
                return f"No document found with query: {query}"
        except Exception as e:
            print(e)
            self.log.exception(str(e))