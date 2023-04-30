import csv
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
    
    #?cursor for performing database operations
    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
        
    #?creating a new table 
    # with connection.cursor() as cursor:
    #     cursor.execute("""
    #                    CREATE TABLE users(
    #                     id serial PRIMARY KEY,
    #                     name varchar(50) NOT NULL, 
    #                     phone varchar(50) NOT NULL)
    #                    """)
        
    #     print("[INFO] created a new table")


    #?insert data into a table from csv file
    #?first, enter new data from csv file
    with open('name_phone.csv', 'r') as file:
        csv_reader = csv.reader(file)
    
        with connection.cursor() as cursor:
            #to skip first line in csv file
            next(csv_reader)
            
            for line in csv_reader:
                    cursor.execute(
                    f"""INSERT INTO lab11 (name, phone) VALUES
                    ('{line[0]}', '{line[1]}')"""
                )
                
            print("[INFO] Data was succesfully inserted")
    
    
    #?insert data into a table from terminal
    # name = input("Enter the name: ")
    # phone = input("Enter the phone number: ")
    
    # with connection.cursor() as cursor:
    #     cursor.execute(f"""
    #                    INSERT INTO users (name, phone) VALUES ('{name}', '{phone}')
    #                    """)
        
    #     print("[INFO] Data was succesfully inserted")
        
    
    #?update data in a table 
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         UPDATE users
    #         SET name = 'Greg', 
    #             phone = '123456789'
    #         WHERE id = 1;
    #         """
    #     )
    #     print("[INFO] Data was succesfully updated")
        

    #?get data from table with filters
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT phone FROM users WHERE name = 'Alibek';"""
    #     )
        
    #     print(cursor.fetchone())
        
    
    #?delete data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         DELETE FROM users
    #         WHERE id = '4' or
    #             name = 'Nurken'
    #         """
    #     )
        
    #     print("[INFO] Data was succesfully deleted")
    
    
    #?deleting a table
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
