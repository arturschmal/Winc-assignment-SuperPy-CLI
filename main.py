# Imports
import os
import argparse
from argparse import RawTextHelpFormatter
import csv
from datetime import date, datetime, timedelta
from sp_functions import *
from prettytable import PrettyTable

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

def main():
    write_today()
    csv_check()

    # create the top level parser
    parser = argparse.ArgumentParser(description='CLI for supermarket inventories', formatter_class=RawTextHelpFormatter)
    # parser.add_argument()
    subparsers = parser.add_subparsers()

    # create the parser for advance time
    advancetime_parser = subparsers.add_parser('advance_time', 
                                        help='With the "advancetime" command you can modify the current date. Use a positive value for dates in the future, a negative value for dates in the past.'
                                        '\nE.g.: "advance time -1" will change the current date to yesterday.'
                                        '\nE.g.: "advance time reset" will reset the date to today’s date.'
                                        '\n——————————————————————————————\n')
    advancetime_parser.add_argument('-a', '--advancetime', action='store', help='The amount of days for advancing the time')
    advancetime_parser.add_argument('-r', '--reset', action='store_true', help='Reset the date to today')
    advancetime_parser.set_defaults(func=advance_time)

    # create the parser for buying products
    buy_parser = subparsers.add_parser('buy', 
                                        help='With the buy command you can add a product to the stock.'
                                        '\nE.g.: buy [Product name] [Buy date (YYY-MM-DD)] [Buy price] [Expiration date YYY-MM-DD]'
                                        '\n——————————————————————————————\n')
    buy_parser.add_argument('product_name', action='store', help='The name of the product')
    # buy_parser.add_argument('buy_date', action='store', help='The date on which the product is bought')
    buy_parser.add_argument('buy_price', action='store', help='The price paid for the product')
    buy_parser.add_argument('expiration_date', action='store', help='The date on which the product expires')
    buy_parser.set_defaults(func=buy)

    # create the parser for selling products
    sell_parser = subparsers.add_parser('sell', help='The sell command adds the sell price to the revenue and removes the item from the inventory.')
    sell_parser.add_argument('product_name', action='store', help='The name of the product')
    sell_parser.add_argument('sell_date', action='store', help='The date on which the product is bought')
    sell_parser.add_argument('sell_price', action='store', help='The price paid for the product')
    sell_parser.set_defaults(func=sell)

    # create the parser for the inventory
    inventory_parser = subparsers.add_parser('inventory', help='inventory help')
    inventory_parser.add_argument('-a', '--advancetime', action='store', help='The amount of days for advancing the time')
    inventory_parser.add_argument('-d', '--date', action='store', help='Set a custom date')
    inventory_parser.set_defaults(func=inventory)

    args = parser.parse_args()

    if args.func:
        args.func(args)

if __name__ == "__main__":
    main()
