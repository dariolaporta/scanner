import os
import glob
import epcs


def main():
    directory_path = raw_input("Enter the directory path: ")
    filename = raw_input("Insert list of epcs: ")
    epcList = filename.split()
    # print("epc list is ", epcList)
    # filename = raw_input("Choose a name of the file to extract: ")
    scan(directory_path, filename, epcList)
    print('operation completed')


def scan(directory_path, name, epcList):
    line_number = 0
    for filename in os.listdir(directory_path):
        path = directory_path + '/' + filename
        if filename.endswith(".txt"):
            for item in epcList:
                with open(path) as f:
                    if item in f.read():
                        line_number += 1
                        print(item + " - " + filename + " " +
                              "at line number:" + str(line_number))
                        # report = open('report/' + name + '.txt', 'a')
                        # report.write(item + " - " + filename + " " +
                        #              "at line number:" + str(line_number))
                        # f.close()


if __name__ == '__main__':
    main()
