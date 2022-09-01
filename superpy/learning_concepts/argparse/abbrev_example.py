import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('--input', action='store', type=int, required=True)
# my_parser.add_argument('--id', action='store', type=int)

# args = my_parser.parse_args()

my_parser = argparse.ArgumentParser(allow_abbrev=False) 
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(f'INPUT: {args.input}', f'ID: {args.id}')