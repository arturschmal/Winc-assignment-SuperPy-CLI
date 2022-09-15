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

    # create the top level parser
    parser = argparse.ArgumentParser(description='\n--------------------------------------------------------------------------------------------\n'
                                    '\nSuperPy: CLI for supermarket inventories\n'
                                    '\n--------------------------------------------------------------------------------------------\n'
                                    '\n💡 Run the command "python main.py superpy" before starting  new session\n\n' 
                                    '\n--------------------------------------------------------------------------------------------\n', 
                                    formatter_class=RawTextHelpFormatter)
    # parser.add_argument()
    subparsers = parser.add_subparsers()

    # create the parser for starting superpy
    superpy_parser = subparsers.add_parser('superpy', 
                                        help='Start superpy with the command "python main.py superpy"'
                                        '\n\n')
    superpy_parser.set_defaults(func=superpy)

    # create the parser for advance time
    advancetime_parser = subparsers.add_parser('advance_time', 
                                        help='With the "advancetime" command you can modify the current date. Use a positive value for dates in the future, a negative value for dates in the past.'
                                        '\nE.g.: "python main.py advance_time -a 1" will change the current date to tomorrow.'
                                        '\nE.g.: "python main.py advance_time -a -1 will change the current date to yesterday.'
                                        '\nE.g.: "python main.py advance_time -r will reset the date to today’s date.'
                                        '\n\n')
    advancetime_parser.add_argument('-a', '--advancetime', action='store', help='The amount of days for advancing the time')
    advancetime_parser.add_argument('-r', '--reset', action='store_true', help='Reset the date to today')
    advancetime_parser.set_defaults(func=advance_time)

    # create the parser for buying products
    buy_parser = subparsers.add_parser('buy', 
                                        help='With the buy command you can add a product to the stock.'
                                        '\nSubmit the productname, the price for which it is bought and the expiration date'
                                        '\nBy default the buying date is set to the current day. To use another date for buying you can use the "advance_time" command to change the day.'
                                        '\nE.g.: To add an apple bought for €0.50 with expiration date 2022-09-20:'
                                        '\n"python main.py buy apple 0.5 2022-09-20"'
                                        '\n\n')
    buy_parser.add_argument('product_name', action='store', help='The name of the product')
    buy_parser.add_argument('buy_price', action='store', help='The price paid for the product')
    # buy_parser.add_argument('-b', '--buy_date', action='store', help='The date on which the product is bought')
    buy_parser.add_argument('expiration_date', action='store', help='The date on which the product expires')
    buy_parser.set_defaults(func=buy)

    # create the parser for selling products
    sell_parser = subparsers.add_parser('sell', 
                                        help='To sell a product enter the productname and the price for which it is sold. E.g:'
                                        '\n"python main.py sell apple 1"'
                                        '\n\n')
    sell_parser.add_argument('product_name', action='store', help='The name of the product')
    # sell_parser.add_argument('sell_date', action='store', help='The date on which the product is bought')
    sell_parser.add_argument('sell_price', action='store', help='The price for which the product was sold')
    sell_parser.set_defaults(func=sell)

    # create the parser for the inventory report
    inventory_parser = subparsers.add_parser('inventory', 
                                            help='Print a report of all products in stock that have not expired'
                                            '\nE.g.: To print the inventory for the current day:'
                                            '\n"python main.py inventory"'
                                            '\nE.g.: Use "-d" to print an inventory for another date:'
                                            '\n"python main.py inventory -d 2022-09-10"'
                                            '\n\n')
    inventory_parser.add_argument('-d', '--date', action='store', help='Set a custom date for the inventory report')
    inventory_parser.set_defaults(func=inventory)

    # create the parser for the expired products report
    expired_parser = subparsers.add_parser('expired', 
                                        help='Prints a report of expired products. By default it uses the current day as date.'
                                        '\nE.g.: To print the inventory for the current day:'
                                        '\n"python main.py expired"'
                                        '\nE.g.: Use "-d" to print a report for another date:'
                                        '\n"python main.py expired -d 2022-09-10"'
                                        '\n\n')
    expired_parser.add_argument('-d', '--date', action='store', help='Set a custom date')
    expired_parser.set_defaults(func=expired)

    # create the parser for the revenue report
    revenue_parser = subparsers.add_parser('revenue', 
                                        help='Prints a revenue and profit report. By default it uses the current day as date.'
                                        '\nE.g.: To print the inventory for the current day:'
                                        '\n"python main.py expired"'
                                        '\nE.g.: Use "-d" to print a report for another date:'
                                        '\n"python main.py expired -d 2022-09-10"'
                                        '\n\n')
    revenue_parser.add_argument('-d', '--date', action='store', help='Set a custom date for the revenue report')
    revenue_parser.set_defaults(func=revenue)

    args = parser.parse_args()

    if args.func:
        args.func(args)

if __name__ == "__main__":
    main()
