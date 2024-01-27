#!/usr/bin/python3
import sys


def fact(num):
    """find 2 factors for a given number"""
    f1 = 2
    while(num % f1):
        if (f1 <= num):
            f1 += 1

    f2 = num // f1
    return (f2, f1)


if len(sys.argv) != 2:
    sys.exit("Wrong usage: {} <file_path>".format(sys.argv[0]))

fileraw = sys.argv[1]

file = open(fileraw, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    factor2, factor1 = fact(num)
    print("{}={}*{}".format(num, factor2, factor1))
