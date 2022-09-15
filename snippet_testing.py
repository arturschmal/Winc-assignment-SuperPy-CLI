import argparse
import csv
import os
from datetime import date, datetime, timedelta
from sp_functions import *
from prettytable import from_csv

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

# # pass args from subparser to function
# def buy(args):
#     with open('bought.csv',"r") as f:
#         reader = csv.reader(f,delimiter = ",")
#         data = list(reader)
#         row_count = len(data)-1
#         product_id = row_count + 1

#     add_line = {'id': product_id, 'product_name': args.product_name, 'buy_date': args.buy_date, 'buy_price': args.buy_price, 'expiration_date': args.expiration_date}
#     with open('bought.csv', mode='a') as f:
#         field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
#         writer = csv.DictWriter(f, fieldnames=field_names)
#         writer.writerow(add_line)
#     f.close()
#     print(f'\n✅ {args.product_name} was added to the stock\n')


# # create the top level parser
# parser = argparse.ArgumentParser(description='CLI for supermarket inventories')
# # parser.add_argument()
# subparsers = parser.add_subparsers(help='sub-command help')

# # create the parser for buying products
# buy_parser = subparsers.add_parser('buy', help='buy help')
# buy_parser.add_argument('product_name', action='store', help='The name of the product')
# buy_parser.add_argument('buy_date', action='store', help='The date on which the product is bought')
# buy_parser.add_argument('buy_price', action='store', help='The price paid for the product')
# buy_parser.add_argument('expiration_date', action='store', help='The date on which the product expires')
# buy_parser.set_defaults(func=buy)

# args = parser.parse_args()

# if args.func:
#     args.func(args)


# # write today's date to a textfile
# today = str(date.today())

# with open('date_file.txt', 'w') as file:
#     file.write(today)


# # modify the date in the textfile with a timedelta
# def advance_time(time_delta):
#     with open('date_file.txt', 'r') as file:
#         date_string = file.read()
#         format_string = '%Y-%m-%d'
        
#         advancetime = time_delta
#         new_date = (datetime.strptime(date_string, format_string)) + timedelta(days=advancetime)

#     with open('date_file.txt', 'w') as file:
#         file.write(new_date.strftime('%Y-%m-%d'))


# advance_time(-300)

# # check if csv files exist and create them if they don't exist
# def csv_check():
#     if not os.path.isfile('bought.csv'):
#         with open('bought.csv', mode='w') as csv_file:
#             fieldnames = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()
#         csv_file.close()

#     if not os.path.isfile('sold.csv'):
#         with open('sold.csv', mode='w') as csv_file:
#             fieldnames = ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price']
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()
#         csv_file.close()
    
# csv_check()

# with open('bought.csv', 'r', newline='') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             inventory = []
            
#             for line in csv_reader:
#                 if line['buy_price'] > str(1.2):
#                     print(line['product_name'])


# # check if format date is correct
# def validate_date(date_text: str):
#     try:
#         datetime.strptime(date_text, '%Y-%m-%d')
#     except ValueError:
#         raise ValueError(
#             'Incorrect date format, date should be given as yyyy-mm-dd')

#  def inventory(args):
#         print('inventory action')
#         if args.now is True:
#             d = today
#         if args.yesterday is True:
#             d = str(date.today() - delta1)
#         if args.date != None:
#             validate_date(args.date)
#             d = args.date

# with open('bought.csv') as table_file:
#     tab = from_csv(table_file)
#     print(tab)


# from prettytable import PrettyTable

# x = PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# x.align = "l"
# print(x)

# from csv import reader

# with open('bought.csv', 'r') as table_file:
#     csv_reader = csv.reader(table_file)
#     first_row = next(csv_reader)
#     for row in csv_reader:
#         print(row)

# with open("bought.csv", "r") as infile, open("temp.csv", "w") as outfile:
#    reader = csv.reader(infile)
#    next(reader, None)  # skip the headers
#    writer = csv.writer(outfile)
#    for row in reader:
#        # process each row
#        writer.writerow(row)



# reset_today()
# print(read_today())

# date_validation('2022-01-01')


# def optional(args):
#     if args.first_optional:
#         print('first optional')
#     if args.second_optional:
#         print('second optional')
#     else:
#         print('no optionals given')

# from argparse import RawTextHelpFormatter

# # create the top level parser
# parser = argparse.ArgumentParser(description='CLI for supermarket inventories', formatter_class=RawTextHelpFormatter)
# # parser.add_argument()
# subparsers = parser.add_subparsers()


# # test optional arguments parser
# optional_parser = subparsers.add_parser('optional', help='')
# optional_parser.add_argument('-f', '--first_optional', action='store_true', help='The amount of days for advancing the time')
# optional_parser.add_argument('-s', '--second_optional', action='store_true', help='Reset the date to today')
# optional_parser.set_defaults(func=optional)





# def date_validation(date):
#     try:
#         datetime.strptime(date, '%Y-%m-%d')
#     except ValueError:
#         print('Date is not in correct format. Enter date as yyyy-mm-dd')
#     else:
#         return date


# today = date_validation('1-1-2020')

# print(today)

#     inventory = []
#     with open('bought.csv', 'r', newline='') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for line in csv_reader:
#             if line['expiration_date'] >= today:
#                 inventory.append(list(line.items())[1][1])


# file_name =  'bought.csv'
# output_file = 'inventory_temp.csv'
# csv_file = open(file_name, 'r', newline='')

# ## note that the index of the year column is excluded
# column_indices = [1,3,4]
# with open(output_file, 'w', newline='') as fh:
#     reader = csv.reader(csv_file, delimiter=',')
#     tmp_row = []
#     for row in reader:
#        for col_inx in column_indices:
#            tmp_row.append(row[col_inx])
#     #    fh.write(','.join(tmp_row))
#     print(tmp_row)

# with open('sold_temp.csv') as f:
#     table = from_csv(f)
#     table.align = 'l'

# print(table)

# from fpdf import FPDF

# class revenue_PDF(FPDF):
#     def revenue_table(self, headings, rows, col_widths=(20, 40, 40, 40, 40, 40)):
#         for col_width, heading in zip(col_widths, headings):
#             self.cell(col_width, 7, heading, border=1, align="L")
#         self.ln()
#         for row in rows:
#             self.cell(col_widths[0], 6, row[0], border="LR", align="L")
#             self.cell(col_widths[1], 6, row[1], border="LR", align="L")
#             self.cell(col_widths[2], 6, row[2], border="LR", align="L")
#             self.cell(col_widths[3], 6, row[3], border="LR", align="L")
#             self.cell(col_widths[4], 6, row[4], border="LR", align="L")
#             self.cell(col_widths[5], 6, row[5], border="LR", align="L")
#             self.ln()
#         # Closure line:
#         self.cell(sum(col_widths), 0, "", border="T")


# def load_data_from_csv(csv_filepath):
#     headings, rows = [], []
#     with open(csv_filepath, encoding="utf8") as csv_file:
#         for row in csv.reader(csv_file, delimiter=","):
#             if not headings:  # extracting column names from first row:
#                 headings = row
#             else:
#                 rows.append(row)
#     return headings, rows


# col_names, data = load_data_from_csv("sold_temp.csv")
# pdf = revenue_PDF(orientation="L", unit="mm", format="A4")
# pdf.set_font("helvetica", size=10)
# pdf.add_page()
# pdf.inventory_table(col_names, data)
# pdf.output("revenue.pdf")
# pdf.ln(10)
# pdf.cell(txt=f'\n→ Revenue on {today} is €{revenue:.2f}\n')
# pdf.ln(5)
# pdf.cell(txt=f'→ Profit on {today} is €{profit:.2f}\n')

if not os.path.isdir('pdf_exports'):
    os.mkdir('pdf_exports')