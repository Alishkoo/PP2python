import psycopg2
from config import host, user, password, db_name


try:
    #connect to exist database
    connection = psycopg2.connect(
        host = host,
        user = user, 
        password = password, 
        database = db_name
    )
    connection.autocommit = True
    
    #cursor for performing database operations
    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
    
    #creating a new table 
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL, 
    #             nick_name varchar(50) NOT NULL) """
    #     )
        
    #     # connection.commit()
    #     print("[INFO] created a new table")
        
    #insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Alibek', 'Alishko')"""
    #     )
        
    #     print("[INFO] Data was succesfully inserted")
        
    #get data from table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE id = '2';"""
    #     )
        
    #     print(cursor.fetchone())
        
    #deleting a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
        
    #     print("[INFO] table was deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
    
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")