import os
import glob
import importlib


def main():
    directory_path = input("Enter directory path of the files to scan *: ")
    itemsManuallyInsert = input(
        "Enter epcs manually (press ENTER if you want to skip): ")
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
            "Enter path of the file with the list of epcs*: ")
        fileExtension = input(
            "Filter scanning by file extension (eg: .txt)*: ")
        items = listOfItemsToScan(listOfItemsPath)
        scanItems(directory_path, items, fileExtension)


def listOfItemsToScan(path):
    arr = []
    with open(path) as file:
        line_count = 0
        for row in file:
            line_count += 1
            arr.append(row.strip())
    return arr


def scanItems(directory_path, epcList, fileExtension):
    print('scanning...')
    try:
        files = glob.glob(directory_path + '/**/*' +
                          fileExtension, recursive=True)
        line_count = 0
        for filename in files:
            path = filename
            for item in epcList:
                with open(path, 'rb') as f:
                    line_count += 1
                    if item in f.read().decode(errors='replace'):
                        print(item + " - " + filename)
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
