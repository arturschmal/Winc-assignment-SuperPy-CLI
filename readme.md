# SuperPy
## Command Line Interface software for supermarkets


This is SuperPy's user guide. SuperPy let's you manage your supermarket's inventory by purchasing and selling products, and generating inventory, expired product and revenue/profit reports.

### Requirements
<hr>

SuperPy makes use of a couple of third party libraries that you should install:

#### PrettyTable
```
pip install prettytable
```

#### FPDF
```
pip install fpdf2
```


### Overview of the commands
<hr>

 #### superpy
 At the start of a new SuperPy session you should run this command:
 ```
 python main.py superpy
 ```
This will ensure the program's internal date is set to the actual current date. It also checks if all necessary files and directories are present.

#### advance_time
With the "advancetime" command you can modify the current date. Use a positive value for dates in the future, a negative value for dates in the past.

To shift the date 1 day forward
```
python main.py advance_time -a 1
```
To shift the day 1 day backwards
```
python main.py advance_time -a -1
```

To reset the date to today's actual date
```
python main.py advance_time -r
```


#### buy
With the buy command you can add a product to the stock.
Submit the productname, the price for which it is bought and the expiration date
By default the buying date is set to the current day. To use another date for buying you can use the "advance_time" command to change the current date.
Note that you should always enter dates in YYYY-MM-DD format.

To add an apple bought for €0.50 with expiration date 2022-09-20:
```
python main.py buy apple 0.5 2022-09-20
```

#### sell
To sell a product enter the productname and the price for which it is sold. E.g:
```
python main.py sell apple 1
```

#### inventory
Prints a report of all products in stock that have not expired.
To print the inventory for the current day:
```
python main.py inventory
```

Use "-d" to print an inventory for a custom date:
```
python main.py inventory -d 2022-09-10
```

#### expired
Prints a report of expired products. By default it uses the current day as date.
To print the inventory for the current day.
```
python main.py expired
```
Use "-d" to print a report for another date.
```
python main.py expired -d 2022-09-10
```
                        
#### revenue
Prints a revenue and profit report. By default it uses the current day as date.
To print the inventory for the current day.
```
python main.py revenue
```
Use "-d" to print a report for another date.
```
python main.py revenue -d 2022-09-10
```

### Save reports as PDF
<hr>

 
When you have generated a report using the inventory, expired or revenue reports you will be asked of you'd like to save the report as a PDF.
Press `y` to do so, or `n` to decline.
