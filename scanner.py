#!/usr/bin/env python3
import os
from os import path
import glob
import pyfiglet
import importlib
import platform


class Scanner:
    def __init__(self, items, directory):
        self.items = items
        self.directory = directory

    def ascii_banner(self, banner):
        element = pyfiglet.figlet_format(banner)
        print(element)
    # Check collected items lenght
    # If items.lenght > 0 the list has been manually typed
    # If the opposite occours , the list was uploaded from a file

    def checkItemsLenght(self):
        try:
            if len(self.items) > 0:
                fileExtension = input(
                    "Filter scanning by file extension (eg: .txt): ")
            else:
                listOfItemsPath = input(
                    "Enter a path of a file with a list of elements you want to search*: ")
                existing_path = path.exists(listOfItemsPath)
                if existing_path == False:
                    raise Exception("Path not valid")
                fileExtension = input(
                    "Choose the format of the files to scan (eg: .txt, .csv ...)*: ")
                if fileExtension.lower().endswith(('.txt', '.csv')) == False:
                    raise Exception("Not a valid extension")
                self.items = self.listOfItemsToScan(listOfItemsPath)

            self.scanItems(fileExtension)
        except Exception as e:
            print(e)
            self.checkItemsLenght()

    def compose_response(self, item, num, path, line):
        print('-' * 100)
        print('ELEMENT: ', item)
        print('-' * 100)
        print('')
        print('FOUND AT LINE:', num, ',', 'FILE:', path)
        print('')
        print(line)

    # Scan collected items
    def scanItems(self, fileExtension):
        # Adding a nice banner
        print('')
        print('SCANNING FILES ... Please wait')
        print('')
        is_mac_os = platform.platform().startswith('macOS')
        try:
            files = glob.glob(self.directory + '/**/*' +
                              fileExtension, recursive=True)
            found_elements = []
            for filename in files:
                path = filename
                for item in self.items:
                    with open(path) as myFile:
                        for num, line in enumerate(myFile, 1):
                            if item in line:
                                found_elements.append(item)
                                self.compose_response(item, num, path, line)

            if is_mac_os == True:
                self.ascii_banner("Completed")
            else:
                print('Completed !!!')
            print('TOTAL ELEMENTS FOUND:', str(len(found_elements)))
        except Exception as e:
            print("Operation Aborted: ", e)

    # In case the list of item was uploaded by a file
    # Appends each read line of the file in an Array and then returns it.
    def listOfItemsToScan(self, path):
        arr = []
        try:
            with open(path) as file:
                for row in file:
                    arr.append(row.strip())
            return arr
        except:
            print(
                'file not found - please make sure you specified a correct file path')
