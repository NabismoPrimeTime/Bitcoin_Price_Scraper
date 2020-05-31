import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",

    database="Bitcoin_Prices"
)

mycursor = db.cursor()

mycursor = db.cursor()

mycursor.execute("CREATE TABLE date_price (date VARCHAR(20), price int, entryid int PRIMARY KEY AUTO_INCREMENT)")