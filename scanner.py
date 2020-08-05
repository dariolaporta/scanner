import os
import glob
import epcs
import importlib


def main():
    directory_path = input("ENTER DIRECTORY PATH: ")
    filename = input("ENTER EPCS MANUALLY: ")
    fileExtension = input("ENTER FILE EXTENSION (eg: .txt): ")
    epcList = filename.split()
    if epcList == []:
        scan(directory_path, fileExtension)
        repeat()
    else:
        scanEpcs(directory_path, epcList, fileExtension)
        repeat()


def scanEpcs(directory_path, epcList, fileExtension):
    try:
        files = glob.glob(directory_path + '/**/*' +
                          fileExtension, recursive=True)
        for filename in files:
            path = filename
            for item in epcList:
                with open(path, 'rb') as f:
                    if item in f.read().decode(errors='replace'):
                        print(item + " - " + filename + " ")
                        f.close()
    except:
        print("Something went wrong")


def repeat():
    repeatOp = input("REPEAT OPERATION ? y/n ")
    if repeatOp == 'y':
        main()
    else:
        print('operation completed')


def scan(directory_path, fileExtension):
    try:
        files = glob.glob(directory_path + '/**/*' +
                          fileExtension, recursive=True)
        for filename in files:
            path = filename
            for item in epcs.epcsList:
                with open(path, 'rb') as f:
                    if item in f.read().decode(errors='replace'):
                        print(item + " - " + filename + " ")
                        f.close()
    except:
        print("Something went wrong")


if __name__ == '__main__':
    main()
