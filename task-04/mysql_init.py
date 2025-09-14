# import csv
# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",         
#     password="Rish@2006",
#     database="moviesdb"
# )
# cursor = conn.cursor()


# with open("movies.csv", newline='', encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  
#     for row in reader:
        

#         released_year = row[1].strip()
#         released_year = int(released_year) if released_year.isdigit() else None

#         imdb_rating = row[3].strip()
#         imdb_rating = float(imdb_rating) if imdb_rating else None

#         values = (
#             row[0],         
#             released_year,   
#             row[2],          
#             imdb_rating,    
#             row[4],          
#             row[5],          
#             row[6],          
#             row[7]           
#         )

#         cursor.execute("""
#             INSERT INTO movies 
#             (Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """, values)

# conn.commit()
# cursor.close()
# conn.close()