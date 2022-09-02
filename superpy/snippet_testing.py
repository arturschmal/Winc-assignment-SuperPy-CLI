import os
import csv

product_name = 'apple'
# open file
with open("bought.csv", "r") as f:
    # pass the file object to reader()
    file_reader = csv.reader(f)
    # do this for all the rows
    for i in file_reader:
        if product_name in i:
            bought_id = i[0]
            print(bought_id)