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

    for row in rows:
        if row != rows[0]:
            rows_in_table.append(row.text)
            # print(row.text)
            for cell in row:
                if cell.text != 'Date':
                    cells_in_table.append(cell.text)


# Extract prices and dates from lists
def extract_close_prices(list_to_review):
    global list_dates, list_close_price, dates, sliced_close_price
    list_dates = list_to_review[0:-1:7]

    dates.append(list_dates)
    list_close_price = list_to_review[4:-1:7]

    return list_dates, list_close_price


# appened master lists
def append_master_lists():
    global list_dates, list_close_price
    for date in list_dates:
        dates.append(date)
    """for price in list_close_price:
        split = price.split(',')
        joined = split[0] + split[1]
        price_float = float(joined)
        sliced_close_price.append(price_float)"""


# Function to get current price data
def get_current_price():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    price = soup.find('div', {'class': 'cmc-details-panel-price jta9t4-0 fcilTk'}).find('span').text
    almost_finished_price = ''
    for char in price:
        if char.isdigit() == True:
            almost_finished_price += char
    finished_price = float(almost_finished_price) // 100
    return finished_price


def get_close_price(list_to_review):
    date = list_to_review.pop(0)
    date2 = list_to_review.pop(0)
    date3 = list_to_review.pop(0)
    date4 = list_to_review.pop(0)
    close = list_to_review[0:-1:7]


    real_close_price.append(close)
    # print(real_close_price)


i = 0


def close_price_to_float(list_to_review):
    global i
    for cell in list_to_review:
        for cell2 in cell:
            if len(cell2) > 6:
                split = cell2.split(',')
                joined = split[0] + split[1]
                price_float = float(joined)
                close_floats.append(price_float)

            else:
                small_float = float(cell2)
                close_floats.append(small_float)

import_table()

extract_close_prices(cells_in_table)

append_master_lists()
get_close_price(cells_in_table)
close_price_to_float(real_close_price)

## Creat a connection between our program and a MySQL database

db = mysql.connector.connect(
    host="localhost",
    user="root",

    database="Bitcoin_Prices"
)

mycursor = db.cursor()



mycursor.execute("CREATE TABLE date_price (date VARCHAR(20) PRIMARY KEY, price float)")

sqlprice = "INSERT INTO date_price (date, price) VALUES (%s, %s)"

for_database = []

for date,price in zip(dates, close_floats):
    if date != dates[0]:
        date_price = (date, price)
        for_database.append(date_price)
print(for_database)
mycursor.executemany(sqlprice,for_database)
'''for price in close_floats:
    mycursor.execute(sqlprice,price)
#mycursor.executemany(sqlFormula, tests)'''

db.commit()