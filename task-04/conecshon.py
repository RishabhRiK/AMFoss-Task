import mysql
from mysql.connector import connect,Error
import csv


def connect_init():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",         # use your MySQL username
            password="Rish@2006",  # your password
            database="moviesdb"
        )
        print("Mysql connection established")
        cursor = conn.cursor()
        return conn, conn.cursor()
    
    except Error as error:
        print("Error:", error)

headers = []
mode_1 = ''
name_1 = ''

x = ["Series_Title", "Released_Year", "Genre", 
         "IMDB_Rating", "Director","Star1", "Star2", "Star3"]

def col_inputs(column):
    global x
    for i in x:
        print(headers)
        if (column.lower() in i.lower()):
            
            if i not in headers:
                headers.append(i) 
    

def search_type(mode):
    global mode_1
    for i in x:
        print(mode_1)
        if (mode.lower() in i.lower()):
            mode_1= mode

rows = []

def search(search_term):
    global mode_1,name_1,headers,rows
    name_1 = search_term 
    choice = mode_1
    conn,cursor = connect_init()
    text = ", ".join(headers) if headers else "Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3"

    query = ""
    params = ()

    if choice == "director":
        query = f"SELECT {text} FROM movies WHERE Director = %s"
        params = (name_1,)

    elif choice == "genre":
        query = f"SELECT {text} FROM movies WHERE Genre LIKE %s"
        params = ("%" + name_1 + "%",)

    elif choice == "year":
        query = f"SELECT {text} FROM movies WHERE Released_Year = %s"
        params = (name_1,)

    elif choice == "rating":
        query = f"SELECT {text} FROM movies WHERE IMDB_Rating = %s"
        params = (name_1,)

    elif choice == "star":
        query = f"SELECT {text} FROM movies WHERE Star1 = %s OR Star2 = %s OR Star3 = %s"
        params = (name_1, name_1, name_1)
    print(query,params)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
    return headers,rows

def csv_export():
    with open("movies_output.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)   
        writer.writerows(rows)     

    print("Data exported to movies_output.csv")