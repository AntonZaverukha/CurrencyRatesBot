import mysql.connector
import requests
from Rates import DBrequestNBU, DBrequestPrivat, DeleteData, NBUdata, Privatdata

# Створення консольного меню програми
menu_options = {
    1: 'Check Rates',
    2: 'Update Rates',
    3: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

# Функція для перевірки курсу популярних валют
def option1():
    print('NBU Rates: ')
    DBrequestNBU("USD")
    DBrequestNBU("EUR")
    DBrequestNBU("RUB")
    DBrequestNBU("PLN")
    print("Privat Rates: ")
    DBrequestPrivat("USD")
    DBrequestPrivat("EUR")
    DBrequestPrivat("RUR")
    DBrequestPrivat("BTC")

# Функція для оновлення даних про курс валют у базі даних
def option2():
    DeleteData()
    NBUdata()
    Privatdata()
    print("Rates updated")

# Цикл для вибору опції та коректної роботи меню
if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Please enter a number: ')

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            print('Exit completed')
            exit()
        else:
            print('Please enter a number between 1 and 3')
