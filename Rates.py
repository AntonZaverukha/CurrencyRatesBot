import mysql.connector
import requests
from pprint import pprint

# Парсинг json'ів
response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
json_obj = response.json()

responsePrivat = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
json_obj_privat = responsePrivat.json()

# Підключення до бази даних
connection = mysql.connector.connect(host='localhost',
                                     database='CurrencyRates',
                                     user='root',
                                     password='Zudule10',
                                     port=3306)
assert connection.is_connected()
db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)


def DeleteData():
    Delete_data = """truncate table RatesNBU """
    Delete_data_privat = """truncate table RatesPrivat """
    cursor.execute(Delete_data)
    cursor.execute(Delete_data_privat)
    connection.commit()

# Занесення інформації з банківських API у базу даних
def NBUdata():
    for json_rate in json_obj:
        sql = "INSERT INTO RatesNBU (Number, Name ,Rate, CC, Date ) VALUES(%s, %s, %s, %s, %s);"
        values = [json_rate['r030'], json_rate['txt'], json_rate['rate'], json_rate['cc'], json_rate['exchangedate']]
        cursor.execute(sql, values)
        connection.commit()


def Privatdata():
    for json_rate_privat in json_obj_privat:
        sql = "INSERT INTO RatesPrivat (Base_CC, Buy, CC, Sale) VALUES(%s, %s, %s, %s);"
        values_privat = [json_rate_privat['base_ccy'], json_rate_privat['buy'], json_rate_privat['ccy'],
                         json_rate_privat['sale']]
        cursor.execute(sql, values_privat)
        connection.commit()

# Запити назви та поточного курсу валют з бази даних
def DBrequestNBU(ChooseCC):
    mydb = mysql.connector.connect(
        host='localhost',
        database='CurrencyRates',
        user='root',
        password='Zudule10',
        port=3306
    )
    mycursor = mydb.cursor()

    if ChooseCC == "USD":
        mycursor.execute("SELECT CC, Rate From RatesNBU where CC = 'USD'")
        myresult = mycursor.fetchall()
        pprint(myresult)
    else:
        if ChooseCC == "EUR":
            mycursor.execute("SELECT CC, Rate From RatesNBU where CC = 'EUR'")
            myresult = mycursor.fetchall()
            pprint(myresult)
        else:
            if ChooseCC == "RUB":
                mycursor.execute("SELECT CC, Rate From RatesNBU where CC = 'RUB'")
                myresult = mycursor.fetchall()
                pprint(myresult)
            else:
                if ChooseCC == "PLN":
                    mycursor.execute("SELECT CC, Rate From RatesNBU where CC = 'PLN'")
                    myresult = mycursor.fetchall()
                    pprint(myresult)


def DBrequestPrivat(ChooseCC):
    mydb = mysql.connector.connect(
        host='localhost',
        database='CurrencyRates',
        user='root',
        password='Zudule10',
        port=3306
    )
    mycursor = mydb.cursor()

    if ChooseCC == "USD":
        mycursor.execute("SELECT CC, Buy FROM RatesPrivat where CC ='USD'")
        myresult = mycursor.fetchall()
        pprint(myresult)
    else:
        if ChooseCC == "EUR":
            mycursor.execute("SELECT CC, Buy FROM RatesPrivat where CC ='EUR'")
            myresult = mycursor.fetchall()
            pprint(myresult)
        else:
            if ChooseCC == "RUR":
                mycursor.execute("SELECT CC, Buy FROM RatesPrivat where CC ='RUR'")
                myresult = mycursor.fetchall()
                pprint(myresult)
            else:
                if ChooseCC == "BTC":
                    mycursor.execute("SELECT CC, Buy FROM RatesPrivat where CC ='BTC'")
                    myresult = mycursor.fetchall()
                    pprint(myresult)

# connection.close()
#         print("MySQL connection is closed")
