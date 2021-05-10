import mysql.connector

def connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cricket@123",
        database="eagr"
        )
    return db 
