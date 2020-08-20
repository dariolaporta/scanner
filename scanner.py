import os
import glob
import importlib


class Scanner:
    def __init__(self, items, directory):
        self.items = items
        self.directory = directory

    # Check collected items lenght
    def checkItemsLenght(self):
        if len(self.items) > 0:
            fileExtension = input(
                "Filter scanning by file extension (eg: .txt): ")
        else:
            listOfItemsPath = input(
                "Enter a path of a file with a list of elements you want to search*: ")
            fileExtension = input(
                "Choose the format of the files to scan (eg: .txt, .csv ...)*: ")
            self.items = self.listOfItemsToScan(listOfItemsPath)

        self.scanItems(fileExtension)

    # Scan collected items
    def scanItems(self, fileExtension):
        # Adding a nice banner
        print('-' * 100)
        print('SCANNING FILES ... Please wait')
        print('-' * 100)
        try:
            files = glob.glob(self.directory + '/**/*' +
                              fileExtension, recursive=True)
            for filename in files:
                path = filename
                for item in self.items:
                    with open(path, 'rb') as f:
                        if item in f.read().decode(errors='replace'):
                            print("FOUND: " + item +
                                  " AT PATH: " + filename)
                            f.close()
        except:
            print("Operation Aborted")

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
