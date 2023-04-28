import psycopg2
from config import host, user, password, db_name


try:
    #?connect to exist database
    connection = psycopg2.connect(
        host = host, 
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
    
    def information():
        #?cursor for performing database operations
        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            
            return(f"Server version: {cursor.fetchone()}")
        
    def get_total(name):
        #?get data from table with filters
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT total FROM snake_users WHERE name = '{name}';"""
            )
            
            return cursor.fetchone()
    
    
    def insert_inf(name, total):
        #?insert data into a table from terminal
        with connection.cursor() as cursor:
            cursor.execute(f"""
                           INSERT INTO snake_users (name, total) VALUES ('{name}', '{total}')
                           """)
            
            print("[INFO] Data was succesfully inserted")
            
            
    def update_inf(name, total):
        #?update data in a table 
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE snake_users
                SET total = '{total}'
                WHERE name = '{name}';
                """
            )
            print("[INFO] Data was succesfully updated")
            
            
      
            
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

def close():
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

            
