# superpy technical report

### __use of subparsers__
The superpy program works with subparsers so that every functionality has it's own set of positional or optional arguments.
At the start of a new session the first parser "superpy" command should be run. This checks if all necesarry files are in place, and if not it creates them, and if in a previous sessions the date was manipulated with the time delta in the advance_time parser, it resets the date to today's date.
<br><br>
### __use of csv files__
There are two important files that let's you keep track of products and sales: `bought.csv` and `sold.csv`.
Whenever a product is added to the inventory with the `buy` parser it is added with a unique product id number to the `bought.csv` file.
The `bought.csv` file is also used to print an inventory report on a specific date, and to print a report of which products are expired.
When a product is sold with the `sell` parser, it checks `bought.csv` if the product is there and if it has not expired. It then adds this product to `sold.csv` and removes the product from `bought.csv`. If there are multiple items of the same product in stock it picks the first item from `bought.csv`.
When a report is made with the `inventory`, `expired` or `revenue` parser, the data for the report is copied to a temporary file that is used to print a table in the terminal or to save the data as a pdf file.
<br><br>
### __save to pdf__
The program makes use of the `fpdf2` library to export the data from `inventory`, `expired` and `revenue` reports that are stored in the temp csv files to a pdf file in the `pdf_exports` directory.

