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

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

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

            file_mv = input(
                "Would you like to move scanned files in an internal directory? (y/n): ")
            self.scanItems(fileExtension, file_mv)
        except Exception as e:
            print(e)
            self.checkItemsLenght()

    def compose_response(self, item, num, path, line, name_dir, file_mv):
        if file_mv == 'y':
            a = path.split("/")
            file_name = a[-1]
            dest_path = f'./Reports/{name_dir}/{file_name}'
            shutil.copyfile(path, dest_path)
        print('-' * 100)
        print('ELEMENT: ', item)
        print('-' * 100)
        print('')
        print('FOUND AT LINE:', num, ',', 'FILE:', path)
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

    # Scan collected items
    def scanItems(self, fileExtension, file_mv):
        # Adding a nice banner
        with open("report_backup.csv", 'w'):
            pass
        self.get_year_time()
        print('')
        print('SCANNING FILES ... Please wait')
        print('')
        name_dir = f'report_{datetime.datetime.now()}_{self.get_random_string(8)}'
        if file_mv == 'y':
            os.mkdir(f'./Reports/{name_dir}')
        is_mac_os = platform.platform().startswith('macOS')
        try:
            files = glob.glob(self.directory + '/**/*' +
                              fileExtension, recursive=True)
            found_elements = []
            scanned_files = []
            f = open(f"./Reports/items_{self.get_year_time()}.csv", "a")
            for filename in files:
                path = filename
                scanned_files.append(path)
                for item in self.items:
                    with open(path) as myFile:
                        for num, line in enumerate(myFile, 1):
                            if item in line:
                                found_elements.append(item)
                                self.compose_response(
                                    item, num, path, line, name_dir, file_mv)
                                f.write(line)
                                f2 = open(f"report_backup.csv", "a")
                                f2.write(line)
                                f2.close()
            f.close()

            if is_mac_os == True:
                self.ascii_banner("Completed")
            else:
                print('Completed !!!')
            print('TOTAL ELEMENTS FOUND:', str(len(found_elements)))
            print('TOTAL FILES SCANNED:', str(len(scanned_files)))
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
