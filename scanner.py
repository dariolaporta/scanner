import os
import glob
import epcs
import importlib


def main():
    directory_path = input("ENTER DIRECTORY PATH: ")
    # filename = input("ENTER LIST OF EPCS: ")
    # epcList = filename.split()
    # print("epc list is ", epcList)
    # filename = raw_input("Choose a name of the file to extract: ")
    scan(directory_path)
    repeat()


def repeat():
    repeatOp = input("REPEAT OPERATION ? Y/N ")
    if repeatOp == 'Y':
        main()
    else:
        print('operation completed')


def scan(directory_path):
    files = glob.glob(directory_path + '/**/*.txt', recursive=True)
    for filename in files:
        path = filename
        for item in epcs.epcsList:
            with open(path) as f:
                if item in f.read():
                    print(item + " - " + filename + " ")
                    # report = open('report/' + name + '.txt', 'a')
                    # report.write(item + " - " + filename + " " +
                    #              "at line number:" + str(line_number))
                    # f.close()


if __name__ == '__main__':
    main()
