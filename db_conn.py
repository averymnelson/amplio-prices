import mysql.connector
from tabulate import tabulate
from datetime import datetime
# set up with basic connection and close for mysql because I don't have an answer for where this is hosted. 
class DB:
    
    def open_database(self, hostname, user_name, mysql_pw, database_name):
        global conn
        conn = mysql.connector.connect(host=hostname,
                                    user=user_name,
                                    password=mysql_pw,
                                    database=database_name
                                    )
        global cursor
        cursor = conn.cursor()

    def close_database(self):
        conn.close()
        print("Database connection closed.")