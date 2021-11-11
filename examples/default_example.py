# python default_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', default='42')

args = my_parser.parse_args()

print(vars(args))