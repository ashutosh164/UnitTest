from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError('Radius not be negative')
    return pi*(r**2)













