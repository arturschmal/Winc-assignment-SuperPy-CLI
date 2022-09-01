import csv
import os


# # Read csv file and get row values as strings from list indexes
# with open('bought.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')
# csv_file.close()


# # Read csv rows as dictionaries and get dictionary values as strings from keys
# with open('bought.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["id"]} {row["product_name"]} {row["buy_date"]} {row["buy_price"]} {row["expiration_date"]}')
#         line_count += 1
#     print(f'Processed {line_count} lines.')
# csv_file.close()


# # Read csv rows as dictionaries format
# with open('bought.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(row)
#         line_count += 1
#     print(f'Processed {line_count} lines.')
# csv_file.close()


# # Simplest form of reading an csv file, print as strings
# with open('bought.csv', newline='') as f:
#     reader = csv.reader(f, delimiter='|')
#     for row in reader:
#         print(', '.join(row))
# f.close()


# Simplest form of reading an csv file use a different delimiter char
# with open('bought.csv', 'r') as f:
#     csv = csv.reader(f, delimiter=',')
#     for row in csv:
#         print(' | '.join(row))
# f.close()


# # Append a new row to a cvs file with a list as input
# add_line = ['000', 'Cheese', '2022-02-04', '0.00', '2022-05-19']
# with open('bought.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(add_line)
# f.close()


# Write data to a new csv file
# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
#     writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
# csv_file.close()


# Append a new row to a cvs file with a dict as input
add_line = {'id': '101010', 'product_name': 'shampoo', 'buy_date': '2022-01-01', 'buy_price': '2.29', 'expiration_date': '2023-12-12'}
with open('bought.csv', mode='w') as f:
    field_names = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writerow(add_line)
f.close()


# Overwrite a specific field value
# reading the CSV file
text = open("bought.csv", "r")
  
#join() method combines all contents of csvfile.csv and formed as a string
text = ''.join([i for i in text]) 

if 'typeface' in text:
    # search and replace the contents
    text = text.replace('typeface', 'conditioner')
    print('Value updated!')
else:
    print('Value does not exist')
  
# output.csv is the output file opened in write mode
x = open("bought.csv","w")
  
# all the replaced text is written in the output.csv file
x.writelines(text)
x.close()