def sell(args):
    with open("bought.csv", "r") as f:
        file_reader = csv.reader(f)
        for item in file_reader:
            if args.product_name in item:
                id = item[0]
                buy_price = float(item[3])

    add_line = {'id': id, 'product_name': args.product_name, 'sell_date': args.sell_date, 'buy_price': buy_price, 'sell_price': args.sell_price, 'profit': float(args.sell_price) - buy_price}
    with open('sold.csv', mode='a') as f:
        field_names = ['id', 'product_name', 'sell_date', 'buy_price', 'sell_price', 'profit']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writerow(add_line)
    f.close()
    print(f'\n✅ {args.product_name} was sold\n')


def sell(args):
    product_stock = []
    with open('bought.csv', 'r+', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if args.product_name == line['product_name']:
                product_stock.append(line)
                if len(product_stock) == 1:
                    break
        new_lines = []
        for line in csv_reader:
            new_lines.append(line)
        print(new_lines)


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

    with open('sold.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['sell_date'] == today:
                revenue += float(line['sell_price'])
        if revenue == 0:
            print(f'\n→ No revenue on {today}\n')
        else:
            print(f'\n→ Revenue on {today} is €{revenue}\n')