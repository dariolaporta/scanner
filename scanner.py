#!/usr/bin/env python3
import os
from os import path
import glob
import pyfiglet
import importlib
import platform
import shutil
import random
import string
import datetime
import utils
translations = utils.get_translations()


class Scanner:
    def __init__(self, items, directory):
        self.items = items
        self.directory = directory
        self.found_elements = []
        self.scanned_files = []
        self.path_file_found = ''

    def checkItemsLenght(self):
        # Check collected items lenght
        # If items.lenght > 0 the list has been manually typed
        # If the opposite occours , the list was uploaded from a file
        try:
            if len(self.items) > 0:
                fileExtension = input(translations["EXTENSION"])
            else:
                listOfItemsPath = input(translations["ENTER_PATH"])
                existing_path = path.exists(listOfItemsPath)
                if existing_path == False:
                    raise Exception(translations["NOT_VALID_PATH"])
                fileExtension = input(translations["FORMAT"])
                if fileExtension.lower().endswith(('.txt', '.csv')) == False:
                    raise Exception(translations["NOT_VALID_EXTENSION"])
                self.items = self.listOfItemsToScan(listOfItemsPath)
            # Scan Items
            file_mv = input(translations["MOVE_FILE"])
            self.scanItems(fileExtension, file_mv)
        except Exception as e:
            print(e)
            self.checkItemsLenght()

    def scanItems(self, fileExtension, file_mv):
        # Scan collected items
        # Adding a nice banner
        with open("report_backup.csv", 'w'):
            pass
        self.get_year_time()
        print('')
        print(translations["SCANNING_WAIT"])
        print('')
        name_dir = f'report_{datetime.datetime.now()}_{self.get_random_string(8)}'
        if file_mv == 'y':
            os.mkdir(f'./Reports/{name_dir}')
        try:
            files = glob.glob(self.directory + '/**/*' +
                              fileExtension, recursive=True)
            f = open(f"./Reports/items_{self.get_year_time()}.csv", "a")
            for filename in files:
                self.path_file_found = filename
                self.scanned_files.append(self.path_file_found)
                # TODO: try to replace the below code with a map(lambda p: myFunc(p, additionalArgument), pages)
                for item in self.items:
                    self.find_items(item, name_dir, file_mv, f)
            f.close()
            self.ascii_banner("Completed")
            print(translations["FOUND"], str(len(self.found_elements)))
            print(translations["SCANNED"], str(len(self.scanned_files)))
        except Exception as e:
            print(translations["ABORTED_OPERATION"], e)

    def find_items(self, item, name_dir, file_mv, f):
        with open(self.path_file_found) as myFile:
            for num, line in enumerate(myFile, 1):
                # if item in line and self.path_file_found.endswith('success.csv'):
                if item in line:
                    self.found_elements.append(item)
                    self.compose_response(
                        item, num, self.path_file_found, line, name_dir, file_mv)
                    f.write(line)
                    f2 = open(f"report_backup.csv", "a")
                    f2.write(line)
                    f2.close()

    def compose_response(self, item, num, path, line, name_dir, file_mv):
        if file_mv == 'y':
            a = self.path_file_found.split("/")
            file_name = a[-1]
            dest_path = f'./Reports/{name_dir}/{file_name}'
            shutil.copyfile(self.path_file_found, dest_path)
        print('-' * 100)
        print('ELEMENT: ', item)
        print('-' * 100)
        print('')
        print('FOUND AT LINE:', num, ',', 'FILE:', self.path_file_found)
        print('')
        print(line)

    def get_year_time(self):
        date = datetime.date.today()
        time = datetime.datetime.now().strftime("%H:%M:%S")
        date_conv = str(date)
        time_conv = str(time)
        a = date_conv.split('-')
        b = time_conv.split(':')
        return f'{"_".join(a)}_{"_".join(b)}'

    def listOfItemsToScan(self, listOfItemsPath):
        # In case the list of item was uploaded by a file
        # Appends each read line of the file in an Array and then returns it.
        arr = []
        try:
            with open(listOfItemsPath) as file:
                for row in file:
                    arr.append(row.strip())
            return arr
        except:
            print(translations["FILE_NOT_FOUND"])

    def ascii_banner(self, banner):
        element = pyfiglet.figlet_format(banner)
        print(element)

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
