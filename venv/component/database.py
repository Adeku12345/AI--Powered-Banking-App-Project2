def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pass@#$123456",
        database="bankingdb2"
    )
