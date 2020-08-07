import os
import glob
import importlib

items = []


def main():
    directory_path = input("Enter directory path of the files to scan *: ")
    itemsManuallyInsert = input(
        "Enter items to search (eg: Hello world! , or press ENTER if you want to skip): ")
    itemsList = itemsManuallyInsert.split()
    checkItemsLenght(itemsList, directory_path)
    repeat()


def checkItemsLenght(itemsList, directory_path):
    if len(itemsList) > 0:
        fileExtension = input("Filter scanning by file extension (eg: .txt): ")
        items = itemsList
    else:
        listOfItemsPath = input(
            "Enter a path of a file with a list of elements you want to search*: ")
        fileExtension = input(
            "Choose the format of the files to scan (eg: .txt, .csv ...)*: ")
        items = listOfItemsToScan(listOfItemsPath)

    scanItems(directory_path, items, fileExtension)


def listOfItemsToScan(path):
    arr = []
    try:
        with open(path) as file:
            for row in file:
                arr.append(row.strip())
        return arr
    except:
        print('file not found - please make sure you specified a correct file path')


def scanItems(directory_path, epcList, fileExtension):
    try:
        files = glob.glob(directory_path + '/**/*' +
                          fileExtension, recursive=True)
        for filename in files:
            path = filename
            for item in epcList:
                with open(path, 'rb') as f:
                    if item in f.read().decode(errors='replace'):
                        print("Search for: " + item + " - Path: " + filename)
                        f.close()
    except:
        print("Operation Aborted")


def repeat():
    repeatOp = input("REPEAT OPERATION ? y/n ")
    if repeatOp == 'y':
        main()
    else:
        print('Process terminated')


if __name__ == '__main__':
    main()
