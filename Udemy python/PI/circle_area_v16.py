#!/usr/bin/env python3
from math import pi
import sys
import errno


class TerninalColor:
    ERROR = '\033[91m'
    NORMAL = '\33[0m'


def help():
    print("It is necessary to inform the radius of the circle")
    print("Sintaxe:{} <raio>".format(sys.argv[0][2:]))


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print(TerninalColor.ERROR + "The radius should be a numeric value" +
              TerninalColor.NORMAL)
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    area = circle(radius)
    print("Circle area is", area)


# """ Highlighting An Error Message""
