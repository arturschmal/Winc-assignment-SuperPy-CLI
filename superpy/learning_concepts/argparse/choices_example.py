# choices_example.py

import argparse

# # list of accepted values for the option
# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('-a', action='store', choices=['head', 'tail'])


# range of accepted values for the option
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', type=int, choices=range(1, 10))



args = my_parser.parse_args()

print(vars(args))