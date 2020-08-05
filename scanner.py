import os
import glob
import epcs
import importlib


def main():
    directory_path = input("ENTER DIRECTORY PATH: ")
    filename = input("ENTER EPCS MANUALLY: ")
    epcList = filename.split()
    if epcList == []:
        scan(directory_path)
        repeat()
    else:
        scanEpcs(directory_path, epcList)
        repeat()


def scanEpcs(directory_path, epcList):
    print('scanEpcs')
    files = glob.glob(directory_path + '/**/*.txt', recursive=True)
    for filename in files:
        path = filename
        for item in epcList:
            with open(path, 'rb') as f:
                if item in f.read().decode(errors='replace'):
                    print(item + " - " + filename + " ")


def repeat():
    repeatOp = input("REPEAT OPERATION ? y/n ")
    if repeatOp == 'y':
        main()
    else:
        print('operation completed')


def scan(directory_path):
    print('scan')
    files = glob.glob(directory_path + '/**/*.txt', recursive=True)
    for filename in files:
        path = filename
        for item in epcs.epcsList:
            with open(path, 'rb') as f:
                if item in f.read().decode(errors='replace'):
                    print(item + " - " + filename + " ")
                    f.close()


if __name__ == '__main__':
    main()
