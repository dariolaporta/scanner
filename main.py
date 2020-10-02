#!/usr/bin/env python3
import os
from os import path
import glob
import importlib
import sys
from scanner import Scanner
import pyfiglet
import platform
import utils
translations = utils.get_translations()


def ascii_banner(banner):
    element = pyfiglet.figlet_format(banner)
    print(element)


def run():
    try:
        os.system('clear')
        ascii_banner("File -  Scanner")
        directory_path = input(translations['DIRECTORY'])
        existing_path = path.exists(directory_path)
        if existing_path == False:
            raise Exception(translations["NOT_VALID_PATH"])
        itemsManuallyInsert = input(translations["ITEMS_TO_SEARCH"])
        itemsList = itemsManuallyInsert.split()
        _scan = Scanner(itemsList, directory_path)
        _scan.checkItemsLenght()
        repeat()
    # If user types CTRL + C takes an exception and exits the program
    except Exception as e:
        print(f'Error: {e}')
        run()
    except KeyboardInterrupt:
        print(translations["EXIT"])
        sys.exit()


# Asks the user to repeat operation or not
def repeat():
    print('')
    repeatOp = input(translations["REPEAT"])
    if repeatOp == 'y':
        run()
    else:
        print(translations["TERMINATED_PROCESS"])


if __name__ == '__main__':
    run()
