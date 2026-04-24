import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Patrick@1234",  # CHANGE THIS
        database="analytics_db"
    )