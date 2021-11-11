# python choices_ex.py -a 4
# python choices_ex.py -a 40
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', choices=['head', 'tail'])

args = my_parser.parse_args()
