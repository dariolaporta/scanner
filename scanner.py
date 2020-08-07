import os
import glob
import importlib


def main():
    directory_path = input("Enter directory path of the files to scan *: ")
    itemsManuallyInsert = input(
        "Enter items to search (eg: Hello world! , or press ENTER if you want to skip): ")
    itemsList = itemsManuallyInsert.split()
    checkItemsLenght(itemsList, directory_path)
    print('Operation Completed')
    repeat()


def checkItemsLenght(itemsList, directory_path):
    if len(itemsList) > 0:
        fileExtension = input("Filter scanning by file extension (eg: .txt): ")
        scanItems(directory_path, itemsList, fileExtension)
    else:
        listOfItemsPath = input(
            "Enter a path of a file with a list of elements you want to search*: ")
        fileExtension = input(
            "Choose the format of the files to scan (eg: .txt, .csv ...)*: ")
        items = listOfItemsToScan(listOfItemsPath)
        scanItems(directory_path, items, fileExtension)


def listOfItemsToScan(path):
    arr = []
    with open(path) as file:
        for row in file:
            arr.append(row.strip())
    return arr


def scanItems(directory_path, epcList, fileExtension):
    print('scanning...')
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
        print("Something went wrong")


def repeat():
    repeatOp = input("REPEAT OPERATION ? y/n ")
    if repeatOp == 'y':
        main()
    else:
        print('Process terminated')


if __name__ == '__main__':
    main()
