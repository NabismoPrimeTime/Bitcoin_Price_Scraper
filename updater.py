import mysql.connector
import bs4
import requests
from bs4 import BeautifulSoup
rows_in_table = []
cells_in_table = []
dates = []
sliced_close_price = []
real_close_price = []
close_floats = []
# Function to import data from the table
def import_table():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    table = soup.find('div', {'class': 'cmc-tab-historical-data ctxmt9-0 ASvFA'})
    rows = table.find_all('tr')

    global rows_in_table
    global cells_in_table

    '''for row in rows:
        if row != rows[0]:
            rows_in_table.append(row.text)
            print(row.text)
            for cell in row:
                if cell.text != 'Date':
                    cells_in_table.append(cell.text)'''
    for row in rows:
        if row == rows[3]:
            rows_in_table.append(row.text)
            #print(row.text)
            for cell in row:
                cells_in_table.append(cell.text)
import_table()
withcom = cells_in_table[4]
if ',' in withcom:
    split = withcom.split(',')
    withcom = split[0] + split[1]
    print(withcom)


to_enter =(cells_in_table[0],float(withcom))
print(to_enter)


## Creat a connection between our program and a MySQL database

db = mysql.connector.connect(
    host="localhost",
    user="root",

    database="Bitcoin_Prices"
)

mycursor = db.cursor()



#mycursor.execute("CREATE TABLE date_price (date VARCHAR(20) PRIMARY KEY, price float)")
#qlquery = "SELECT * FROM date_price"
sqlformula = "INSERT INTO date_price (date, price) VALUES (%s, %s)"
#mycursor.execute(sqlquery)
#print(mycursor.text)
mycursor.execute(sqlformula,to_enter)


db.commit()