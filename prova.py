import csv

path = '/Users/temera/Desktop/epcs.txt'
item = '0000000000000040EB96938'
arr = []
with open(path) as file:
    line_count = 0
    for row in file:
        line_count += 1
        arr.append(row.strip())
