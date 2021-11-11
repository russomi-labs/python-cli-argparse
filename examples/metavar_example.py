# python metavar_example.py -h
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-v',
                       '--verbosity',
                       action='store',
                       type=int,
                       metavar='LEVEL')

args = my_parser.parse_args()

print(vars(args))
