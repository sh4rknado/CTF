#!/bin/python

import csv

if __name__ == "__main__":
    value = ""
    
    with open('data-extracted') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            value += row[3]

    print(value)
