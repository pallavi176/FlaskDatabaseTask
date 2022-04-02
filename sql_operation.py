import mysql.connector as connection
from custom_logger import CustomLogger

class MysqlOperation:
    log = CustomLogger.log('mysql.log')

    def __init__(self,host,user,passwd):
        """
        Intializing with Variables
        """
        try:
            self.host=host
            self.user=user
            self.passwd=passwd
            self.conn=self.establish_db_conn()
            self.cursor=self.conn.cursor()
            self.log.info(f"Initialized all the variables: {host}, {user}, {passwd}")
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def establish_db_conn(self):
        """
        Creating mysql database connection
        """
        try:
            self.log.info("Creating mysql database connection")
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd)
            return mydb
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def use_database(self,db):
        """
        Use database
        """
        try:
            query = "use {}".format(db)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            self.log.info(f"Database: {db} in use.")
            return f"Database: {db} in use."
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_data_table(self, tabl):
        """
        Select Data from table
        """
        try:
            query = "select * from {}".format(tabl)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            res = self.cursor.fetchall()
            self.log.warning(f"Returning data from Table: {tabl}.")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)