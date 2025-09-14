from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "Rish@2006",
        database = "moviesdb"
    ) as connection:
        show_db_query = "SHOW DATABASES"
        print(connection)
        
        with connection.cursor() as cursor:
            # Show first 10 movies from the table
            cursor.execute("SELECT * FROM movies LIMIT 1000")

            # Fetch all results
            rows = cursor.fetchall()

            # Print results row by row
            for row in rows:
                print(row)
except Error as error:
    print(error)
