#!/usr/bin/env python3
from math import pi


def circle(radius):
    print('Circle area', pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Informe the radius: ')
    circle(radius)


#""" No return function"""
