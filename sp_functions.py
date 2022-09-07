import os
import csv
import argparse
from datetime import date, datetime, timedelta
from prettytable import from_csv


# write today's date to a textfile
def today():
    if not os.path.isfile('date_file.txt'):
        today = str(date.today())
        with open('date_file.txt', 'w') as file:
            file.write(today)
        file.close()


# modify the date in the textfile with a timedelta
def advance_time(args):
    with open('date_file.txt', 'r') as file:
        date_string = file.read()
        format_string = '%Y-%m-%d'
    if args.advancetime == 'reset':
        new_date = (datetime.strptime(date_string, format_string)) + timedelta(days=0)
    else: 
        advancetime = int(args.advancetime)
        new_date = (datetime.strptime(date_string, format_string)) + timedelta(days=advancetime)

    with open('date_file.txt', 'w') as file:
        file.write(new_date.strftime('%Y-%m-%d'))


# check if csv files exist and create them if they don't exist
def csv_check():
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


# functions for buying and selling
def buy(args):
    with open('bought.csv',"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)-1
        product_id = row_count + 1

    add_line = {'id': product_id, 'product_name': args.product_name, 'buy_date': args.buy_date, 'buy_price': args.buy_price, 'expiration_date': args.expiration_date}
    with open('bought.csv', mode='a') as f:
        field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()
    print(f'\n✅ {args.product_name} was added to the stock\n')


def sell(args):
    with open('sold.csv',"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)-1
        product_id = row_count + 1

    with open("bought.csv", "r") as f:
        file_reader = csv.reader(f)
        for i in file_reader:
            if args.product_name in i:
                bought_id = i[0]

    add_line = {'id': product_id, 'bought_id': bought_id, 'product_name': args.product_name, 'sell_date': args.sell_date, 'sell_price': args.sell_price}
    with open('sold.csv', mode='a') as f:
        field_names = ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()
    print(f'\n✅ {args.product_name} was sold\n')


# functions for generating reports
# def inventory(args):
#     try:
#         datetime.strptime(args.date, '%Y-%m-%d')
#     except ValueError:
#         raise ValueError('Date is not in correct format. Enter date as yyyy-mm-dd')

#     date = datetime.strptime(args.date, '%Y-%m-%d')

#     with open('bought.csv', 'r', newline='') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for line in csv_reader:
#             if line['expiration_date'] >= date.strftime('%Y-%m-%d'):
#                 print(line)


def inventory(args):
    try:
        datetime.strptime(args.date, '%Y-%m-%d')
        date = datetime.strptime(args.date, '%Y-%m-%d')
        with open('bought.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if line['expiration_date'] >= date.strftime('%Y-%m-%d'):
                    print(line)
    except ValueError:
        print('Date is not in correct format. Enter date as yyyy-mm-dd')