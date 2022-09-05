# Imports
import os
import argparse
import csv
from datetime import date
from sp_functions import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# get the current working directory
current_directory = os.getcwd()


# check if csv files exist and create them if they don't exist
if not os.path.isfile('bought.csv'):
    with open('bought.csv', mode='w') as csv_file:
        fieldnames = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    csv_file.close()

if not os.path.isfile('sold.csv'):
    with open('sold.csv', mode='w') as csv_file:
        fieldnames = ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    csv_file.close()

def main():
    # write today's date to a textfile
    today = str(date.today())
    with open('today.txt', 'w') as file:
        file.write(today)
        # create the top level parser
        parser = argparse.ArgumentParser(description='CLI for supermarket inventories')
        # parser.add_argument()
        subparsers = parser.add_subparsers()
    
    # create the parser for buying products
    buy_parser = subparsers.add_parser('buy', 
                                        help='With the buy command you can add a product to the stock.\nE.g.: buy [Product name] [Buy date (YYY-MM-DD)] [Buy price] [Expiration date YYY-MM-DD]')
    buy_parser.add_argument('product_name', action='store', help='The name of the product')
    buy_parser.add_argument('buy_date', action='store', help='The date on which the product is bought')
    buy_parser.add_argument('buy_price', action='store', help='The price paid for the product')
    buy_parser.add_argument('expiration_date', action='store', help='The date on which the product expires')
    buy_parser.set_defaults(func=buy)

    # create the parser for selling products
    sell_parser = subparsers.add_parser('sell', help='sell help')
    sell_parser.add_argument('product_name', action='store', help='The name of the product')
    sell_parser.add_argument('sell_date', action='store', help='The date on which the product is bought')
    sell_parser.add_argument('sell_price', action='store', help='The price paid for the product')
    sell_parser.set_defaults(func=sell)


    args = parser.parse_args()

    if args.func:
        args.func(args)

if __name__ == "__main__":
    main()
