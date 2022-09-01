# nargs example

import argparse

# # nargs requires exactly 3 arguments
# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('--input', action='store', type=int, nargs=3)
# args = my_parser.parse_args()
# print(args.input)


# # nargs accepts a single value which can be optional
# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input', action='store', nargs='?', default='My default value')
# args = my_parser.parse_args()
# print(args.input)


# # nargs accepts flexible number of values and gathers them in a list
# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input', action='store', nargs='*', default='My default value')
# args = my_parser.parse_args()
# print(args.input)


# # nargs accepts variable number of values but needs at least one specified
# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input', action='store', nargs='+')
# args = my_parser.parse_args()
# print(args.input)

# nargs accepts variable number of values but needs at least one specified
my_parser = argparse.ArgumentParser()
my_parser.add_argument('first', action='store')
my_parser.add_argument('others', action='store', nargs=argparse.REMAINDER)


args = my_parser.parse_args()
print('first = %r' % args.first)
print('others = %r' % args.others)
