import os
import glob
import importlib
import sys
from scanner import Scanner
import pyfiglet


# It collects infos ( directory , items ) typed by the users and then check items lenght
def run():
    try:
        os.system('clear')
        ascii_banner = pyfiglet.figlet_format("FILE   SCANNER")
        print(ascii_banner)
        directory_path = input("Enter directory path of the files to scan *: ")
        itemsManuallyInsert = input(
            "Enter items to search (eg: Hello world! , or press ENTER if you want to skip): ")
        itemsList = itemsManuallyInsert.split()
        _scan = Scanner(itemsList, directory_path)
        _scan.checkItemsLenght()
        repeat()
    # If user types CTRL + C takes an exception and exits the program
    except KeyboardInterrupt as error:
        print("\nExiting Program !!!!")
        sys.exit()


# Asks the user to repeat operation or not
def repeat():
    repeatOp = input("REPEAT OPERATION ? y/n ")
    if repeatOp == 'y':
        run()
    else:
        print('Process terminated')


if __name__ == '__main__':
    run()
