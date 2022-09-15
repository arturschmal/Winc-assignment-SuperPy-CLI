# SuperPy
## Command Line Interface software for supermarkets


This is SuperPy's user guide. SuperPy let's you manage your supermarket's inventory by purchasing and selling products, and generating inventory, expired product and revenue/profit reports.


### Overview of the commands you can use.
<hr>

 #### superpy
 At the start of a new SuperPy session you should run this command:
 ```
 python main.py superpy
 ```
This will ensure the program's internal date is set to the actual current date. It also checks if all necessary files and directories are present.

#### advance_time
With the "advancetime" command you can modify the current date. Use a positive value for dates in the future, a negative value for dates in the past.
E.g.: "python main.py advance_time -a 1" will change the current date to tomorrow.
E.g.: "python main.py advance_time -a -1 will change the current date to yesterday.
E.g.: "python main.py advance_time -r will reset the date to today’s date.
                        
    buy                 With the buy command you can add a product to the stock.
                        Submit the productname, the price for which it is bought and the expiration date
                        By default the buying date is set to the current day. To use another date for buying you can use the "advance_time" command to change the day.
                        E.g.: To add an apple bought for €0.50 with expiration date 2022-09-20:
                        "python main.py buy apple 0.5 2022-09-20"
                        
    sell                To sell a product enter the productname and the price for which it is sold. E.g:
                        "python main.py sell apple 1"
                        
    inventory           Print a report of all products in stock that have not expired
                        E.g.: To print the inventory for the current day:
                        "python main.py inventory"
                        E.g.: Use "-d" to print an inventory for another date:
                        "python main.py inventory -d 2022-09-10"
                        
    expired             Prints a report of expired products. By default it uses the current day as date.
                        E.g.: To print the inventory for the current day:
                        "python main.py expired"
                        E.g.: Use "-d" to print a report for another date:
                        "python main.py expired -d 2022-09-10"
                        
    revenue             Prints a revenue and profit report. By default it uses the current day as date.
                        E.g.: To print the inventory for the current day:
                        "python main.py expired"
                        E.g.: Use "-d" to print a report for another date:
                        "python main.py expired -d 2022-09-10"
