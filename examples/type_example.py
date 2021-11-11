# python type_example.py -a 42
# python type_example.py -a "that's a string"
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', type=int)

args = my_parser.parse_args()

print(vars(args))