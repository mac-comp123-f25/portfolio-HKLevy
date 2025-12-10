import math

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print("Area =",area)
    print("Cost =",cost)

def rect_area(width, length):
    int_width = math.ceil(width)
    int_length = math.ceil(length)
    return int_width * int_length

def roof_cost(area, price):
    return area * price

estimate_green_roof(54.25, 32.8, 35)