import mysql.connector
import requests
from Rates import DBrequestNBU, DBrequestPrivat, DeleteData, NBUdata, Privatdata

menu_options = {
    1: 'Info',
    2: 'Update Rates',
    3: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print('NBU rates: ')
    DBrequestNBU("USD")
    DBrequestNBU("EUR")
    DBrequestNBU("RUB")
    DBrequestNBU("PLN")
    print("Privat Rates: ")
    DBrequestPrivat("USD")
    DBrequestPrivat("EUR")
    DBrequestPrivat("RUR")
    DBrequestPrivat("BTC")


def option2():
    DeleteData()
    NBUdata()
    Privatdata()
    print("Rates updated")


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            print('Exit completed')
            exit()
        else:
            print('Please enter a number between 1 and 3')
