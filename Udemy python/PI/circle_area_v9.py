#!/usr/local/bin/env python3
from math import pi


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    radius = input('Informe the radius: ')
    area = circle(radius)
    print(f"Circle area is{area}")


# """Returning function"""
