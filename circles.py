from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError('Radius not be negative')
    return pi*(r**2)


# radii = [2,0,-3,2+3j,True,'radius']
# message = 'Area of circles with r = {radius} is {area}'
#
# for r in radii:
#     a = circle_area(r)
#     # print(message.format(radius=r, area=a))
#     print(f'Area of circles with r = {r} is {a}')










