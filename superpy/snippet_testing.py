import os
import csv
import argparse


# # read the id from bought.csv and copy it to bought_id in sold.csv
# product_name = 'apple'
# # open file
# with open("bought.csv", "r") as f:
#     # pass the file object to reader()
#     file_reader = csv.reader(f)
#     # do this for all the rows
#     for i in file_reader:
#         if product_name in i:
#             bought_id = i[0]
#             print(bought_id)

# pass args from subparser to function
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


# create the top level parser
parser = argparse.ArgumentParser(description='CLI for supermarket inventories')
# parser.add_argument()
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for buying products
buy_parser = subparsers.add_parser('buy', help='buy help')
buy_parser.add_argument('product_name', action='store', help='The name of the product')
buy_parser.add_argument('buy_date', action='store', help='The date on which the product is bought')
buy_parser.add_argument('buy_price', action='store', help='The price paid for the product')
buy_parser.add_argument('expiration_date', action='store', help='The date on which the product expires')
buy_parser.set_defaults(func=buy)

args = parser.parse_args()

if args.func:
    args.func(args)