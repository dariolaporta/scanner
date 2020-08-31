#!/usr/bin/env python3
import os
from os import path
import glob
import importlib
import sys
from scanner import Scanner
import pyfiglet
import platform


def ascii_banner(banner):
    element = pyfiglet.figlet_format(banner)
    print(element)


# It collects infos ( directory , items ) typed by the users and then check items lenght
def run():
    try:
        is_mac_os = platform.platform().startswith('macOS')
        if is_mac_os == True:
            os.system('clear')
            ascii_banner("File -  Scanner")
        directory_path = input("Enter directory path of the files to scan *: ")
        existing_path = path.exists(directory_path)
        if existing_path == False:
            raise Exception("Path not valid")
        itemsManuallyInsert = input(
            "Enter items to search (eg: Hello world! , or press ENTER if you want to skip): ")
        itemsList = itemsManuallyInsert.split()
        _scan = Scanner(itemsList, directory_path)
        _scan.checkItemsLenght()
        repeat()
    # If user types CTRL + C takes an exception and exits the program
    except Exception as e:
        print(e)
        run()
    except KeyboardInterrupt:
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
