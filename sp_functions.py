from asyncore import read
import os
import csv
import argparse
from datetime import date, datetime, timedelta
from prettytable import from_csv
from fpdf import FPDF


# reset the day to today check csv files
def superpy(args):
    reset_today()
    dir_check()
    csv_check()
    today = read_today()
    print(f'\nSuperpy is ready for use. Today’s date is {today}.\n')


# DATE ———————————————————————————————————————————————————————————————

# if not present write today's date to 'datefile.txt'
def write_today():
    if not os.path.isfile('date_file.txt'):
        today = str(date.today())
        with open('date_file.txt', 'w') as file:
            file.write(today)
        file.close()


# resets the date in 'datefile.txt' to today's actual date
def reset_today():
    today = str(date.today())
    with open('date_file.txt', 'w') as file:
        file.write(today)
    file.close()


# modify the date in 'datefile.txt' with a timedelta
def advance_time(args):
    with open('date_file.txt', 'r') as file:
        date_string = file.read()
        format_string = '%Y-%m-%d'
    
    with open('date_file.txt', 'w') as file:
        if args.reset == True:
            reset_today()
            print(f'\n→ Today’s date is reset to {date.today()}\n')
        else: 
            advancetime = int(args.advancetime)
            new_date = (datetime.strptime(date_string, format_string)) + timedelta(days=advancetime)
            file.write(new_date.strftime('%Y-%m-%d'))
            print(f'\n→ The current date is shifted to {new_date.strftime("%Y-%m-%d")}\n')


# read the date from 'datefile.txt'
def read_today():
    with open('date_file.txt', 'r') as file:
        date_string = file.read()
        format_string = '%Y-%m-%d'
        today = (datetime.strptime(date_string, format_string))
    return today.strftime('%Y-%m-%d')


def date_validation(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('❗️❗️❗️Date format should be yyyy-mm-dd')
        return None


# CSV ———————————————————————————————————————————————————————————————

# check if csv files exist and create them if they don't exist
def csv_check():
    if not os.path.isfile('bought.csv'):
        with open('bought.csv', mode='w') as csv_file:
            fieldnames = ['id', 'product_name', 'buy_price', 'buy_date', 'expiration_date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        csv_file.close()

    if not os.path.isfile('sold.csv'):
        with open('sold.csv', mode='w') as csv_file:
            fieldnames = ['id', 'product_name', 'sell_date', 'buy_price', 'sell_price', 'profit']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        csv_file.close()

def dir_check():
    if not os.path.isdir('pdf_exports'):
        os.mkdir('pdf_exports')

def load_data_from_csv(csv_filepath):
                    headings, rows = [], []
                    with open(csv_filepath, encoding="utf8") as csv_file:
                        for row in csv.reader(csv_file, delimiter=","):
                            if not headings:  # extracting column names from first row:
                                headings = row
                            else:
                                rows.append(row)
                    return headings, rows


# BUY AND SELL ———————————————————————————————————————————————————————————————

# add products to 'bought.csv'
def buy(args):
    try:
        datetime.strptime(args.expiration_date, '%Y-%m-%d')
    except ValueError:
        print('❗️❗️❗️Date format should be yyyy-mm-dd')
        return None
    
    with open('bought.csv',"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)-1
        product_id = row_count + 1
    
    with open('bought.csv', mode='a') as f:
        date = read_today()
        add_line = {'id': product_id, 
            'product_name': args.product_name, 
            'buy_price': "{:.2f}".format(float(args.buy_price)),
            'buy_date': date,  
            'expiration_date': args.expiration_date}
        field_names = ['id', 'product_name', 'buy_price', 'buy_date', 'expiration_date']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()

    print(f'\n✅ {args.product_name} was added to the stock\n')


# add sold product to sold.csv and store same id as product has in 
def sell(args):
    # try:
    #     datetime.strptime(args.sell_date, '%Y-%m-%d')
    # except ValueError:
    #     print('\n❗️❗️❗️Date format should be yyyy-mm-dd\n')
    #     return None 
    today = read_today()
    sell_item = []

    with open('bought.csv', 'r+', newline='') as csv_file:
        temp_lines = []
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            temp_lines.append(line)

        for row in temp_lines:
            if args.product_name == row['product_name']:
                if row['expiration_date'] > today:
                    print(today)
                    sell_item.append(row)
                    keys = temp_lines[0].keys()
                    temp_lines.remove(row)
                    if len(sell_item) == 1:
                        break

        # print(f'temp_lines: {temp_lines}')
        # print(sell_item)
    if len(sell_item) == 0:
        print('\n→ Product is not in stock.\n') 
    else:  
        id = sell_item[0]['id']
        buy_price = float(sell_item[0]['buy_price'])
        sell_date = read_today()
        add_line = {'id': id, 'product_name': args.product_name, 'sell_date': sell_date, 'buy_price': "{:.2f}".format(float(buy_price)), 'sell_price': "{:.2f}".format(float(args.sell_price)), 'profit': "{:.2f}".format(float(args.sell_price) - buy_price)}
        with open('sold.csv', mode='a') as f:
            field_names = ['id', 'product_name', 'sell_date', 'buy_price', 'sell_price', 'profit']
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writerow(add_line)
        
        print(f'\n✅ {args.product_name} was sold\n')

        # keys = temp_lines[0].keys()
    
        with open('bought.csv', 'w') as file:
            csvwriter = csv.DictWriter(file, keys)
            csvwriter.writeheader()
            csvwriter.writerows(temp_lines)



# REPORTS ———————————————————————————————————————————————————————————————

# inventory report from today's date or custom date
def inventory(args):
    if args.date:
        try:
            datetime.strptime(args.date, '%Y-%m-%d')
            today = args.date
        except ValueError:
            print('\n❗️❗️❗️Date format should be yyyy-mm-dd\n')
            return None
    else:
        today = read_today()

    inventory = []
    with open('bought.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['expiration_date'] >= today:
                inventory.append(line)

        with open('inventory_temp.csv', mode='w') as f:
            field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for line in inventory:
                writer.writerow(line)

        print(f'\n→ Inventory on {today}\n')
        with open('inventory_temp.csv') as f:
            table = from_csv(f)
            table.align = 'l'
    
    print(table)
    print('\n')

    export_question = input('Do you want to export the report to a PDF file?\n'
                             'Enter "y" for yes or "n" for no:  ')
    export_question = export_question.lower()

    if export_question == 'y':
        class inventory_PDF(FPDF):
            def inventory_table(self, headings, rows, col_widths=(20, 40, 40, 40, 40)):
                for col_width, heading in zip(col_widths, headings):
                    self.cell(col_width, 7, heading, border=1, align="L")
                self.ln()
                for row in rows:
                    self.cell(col_widths[0], 6, row[0], border="LR", align="L")
                    self.cell(col_widths[1], 6, row[1], border="LR", align="L")
                    self.cell(col_widths[2], 6, row[2], border="LR", align="L")
                    self.cell(col_widths[3], 6, row[3], border="LR", align="L")
                    self.cell(col_widths[4], 6, row[4], border="LR", align="L")
                    self.ln()
                # Closure line:
                self.cell(sum(col_widths), 0, "", border="T")

        load_data_from_csv("inventory_temp.csv")

        col_names, data = load_data_from_csv("inventory_temp.csv")
        pdf = inventory_PDF(orientation="L", unit="mm", format="A4")
        pdf.set_font("helvetica", size=10)
        pdf.add_page()
        pdf.cell(txt=f'Inventory on {today}')
        pdf.ln(10)
        pdf.inventory_table(col_names, data)
        pdf_name = 'inventory_' + today
        pdf.output("./pdf_exports/"f'{pdf_name}.pdf')

        print(f'\n\nThe file {pdf_name}.pdf report exported to the "pdf_exports" directory\n\n')
        
    if export_question == 'n':
        print(f'\n\nNo report was exported.\n\n')


def expired(args):
    if args.date:
        try:
            datetime.strptime(args.date, '%Y-%m-%d')
            today = args.date
        except ValueError:
            print('❗️❗️❗️Date format should be yyyy-mm-dd')
            return None
    else:
        today = read_today()

    expired = []
    with open('bought.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['expiration_date'] < today:
                expired.append(line)
        
        if len(expired) < 1:
            print(f'\n→ There are no expired products\n')
        else:
            with open('expired_temp.csv', mode='w') as f:
                field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                for line in expired:
                    writer.writerow(line)

                print(f'\n→ The following products are expired\n')

            with open('expired_temp.csv') as f:
                table = from_csv(f)
                table.align = 'l'
    
            print(table)

            export_question = input('Do you want to export the report to a PDF file?\n'
                             'Enter "y" for yes or "n" for no:  ')
            export_question = export_question.lower()

            if export_question == 'y':
                class expired_PDF(FPDF):
                    def expired_table(self, headings, rows, col_widths=(20, 40, 40, 40, 40)):
                        for col_width, heading in zip(col_widths, headings):
                            self.cell(col_width, 7, heading, border=1, align="L")
                        self.ln()
                        for row in rows:
                            self.cell(col_widths[0], 6, row[0], border="LR", align="L")
                            self.cell(col_widths[1], 6, row[1], border="LR", align="L")
                            self.cell(col_widths[2], 6, row[2], border="LR", align="L")
                            self.cell(col_widths[3], 6, row[3], border="LR", align="L")
                            self.cell(col_widths[4], 6, row[4], border="LR", align="L")
                            self.ln()
                        # Closure line:
                        self.cell(sum(col_widths), 0, "", border="T")

                load_data_from_csv("expired_temp.csv")

                col_names, data = load_data_from_csv("expired_temp.csv")
                pdf = expired_PDF(orientation="L", unit="mm", format="A4")
                pdf.set_font("helvetica", size=10)
                pdf.add_page()
                pdf.cell(txt=f'All expired products on {today}')
                pdf.ln(10)
                pdf.expired_table(col_names, data)
                pdf_name = 'expired_products_' + today
                pdf.output("./pdf_exports/"f'{pdf_name}.pdf')

                print(f'\n\nThe file {pdf_name}.pdf report exported to the "pdf_exports" directory\n\n')
                
            if export_question == 'n':
                print(f'\n\nNo report was exported.\n\n')


# revenue report
def revenue(args):
    if args.date:
        try:
            datetime.strptime(args.date, '%Y-%m-%d')
            today = args.date
        except ValueError:
            print('❗️❗️❗️Date format should be yyyy-mm-dd')
            return None
    else:
        today = read_today()
    
    revenue = 0.00
    profit = 0.00
    sold_products = []
    with open('sold.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['sell_date'] == today:
                revenue += float(line['sell_price'])
                profit += float(line['profit'])
                sold_products.append(line)
        if revenue == 0:
            print(f'\n→ No revenue on {today}\n')
        else:
            with open('sold_temp.csv', mode='w') as f:
                field_names = ['id', 'product_name', 'sell_date', 'buy_price', 'sell_price', 'profit']
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                for line in sold_products:
                    writer.writerow(line)

                print(f'\n→ Sold products on {today}:\n')
                
            with open('sold_temp.csv') as f:
                table = from_csv(f)
                table.align = 'l'
            
            print(table)
            print(f'\n→ Revenue on {today} is €{revenue:.2f}\n')
            print(f'→ Profit on {today} is €{profit:.2f}\n')

            export_question = input('Do you want to export the report to a PDF file?\n'
                             'Enter "y" for yes or "n" for no:  ')
            export_question = export_question.lower()

            if export_question == 'y':
                class revenue_PDF(FPDF):
                    def revenue_table(self, headings, rows, col_widths=(20, 40, 40, 40, 40, 40)):
                        for col_width, heading in zip(col_widths, headings):
                            self.cell(col_width, 7, heading, border=1, align="L")
                        self.ln()
                        for row in rows:
                            self.cell(col_widths[0], 6, row[0], border="LR", align="L")
                            self.cell(col_widths[1], 6, row[1], border="LR", align="L")
                            self.cell(col_widths[2], 6, row[2], border="LR", align="L")
                            self.cell(col_widths[3], 6, row[3], border="LR", align="L")
                            self.cell(col_widths[4], 6, row[4], border="LR", align="L")
                            self.cell(col_widths[5], 6, row[5], border="LR", align="L")
                            self.ln()
                        # Closure line:
                        self.cell(sum(col_widths), 0, "", border="T")

                load_data_from_csv("sold_temp.csv")

                col_names, data = load_data_from_csv("sold_temp.csv")
                pdf = revenue_PDF(orientation="L", unit="mm", format="A4")
                pdf.set_font("helvetica", size=10)
                pdf.add_page()
                pdf.revenue_table(col_names, data)
                pdf.ln(10)
                pdf.cell(txt=f'Total revenue on {today} is {revenue:.2f}\n')
                pdf.ln(7)
                pdf.cell(txt=f'Total profit on {today} is {profit:.2f}\n')
                pdf_name = 'revenue_' + today
                pdf.output("./pdf_exports/"f'{pdf_name}.pdf')

                print(f'\n\nThe file {pdf_name}.pdf report exported to the "pdf_exports" directory\n\n')
                
            if export_question == 'n':
                print(f'\n\nNo report was exported.\n\n')



                

