import csv

# functions for buying and selling
def buy_item(product_name, buy_date, buy_price, expiration_date):
    with open('bought.csv',"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)-1
        product_id = row_count + 1

    add_line = {'id': product_id, 'product_name': product_name, 'buy_date': buy_date, 'buy_price': buy_price, 'expiration_date': expiration_date}
    with open('bought.csv', mode='a') as f:
        field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()


def sell_item(product_name, sell_date, sell_price):
    with open('sold.csv',"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)-1
        product_id = row_count + 1

    with open("bought.csv", "r") as f:
        file_reader = csv.reader(f)
        for i in file_reader:
            if product_name in i:
                bought_id = i[0]

    add_line = {'id': product_id, 'bought_id': bought_id, 'product_name': product_name, 'sell_date': sell_date, 'sell_price': sell_price}
    with open('sold.csv', mode='a') as f:
        field_names = ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()