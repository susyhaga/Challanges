#!/usr/bin/env python3
from math import pi
import sys


def help():
    print("It is necessary to inform the radius of the circle")
    print("Sintaxe:{} <raio>".format(sys.argv[0][2:]))


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print("Circle area is", area)


# """Improving Help function"""
