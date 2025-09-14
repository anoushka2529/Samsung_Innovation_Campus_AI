import math
import numpy as np

# Area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Area of a triangle (Heron's formula)
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Distance between two points (2D)
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


# Example usage
print("Circle area:", circle_area(5))
print("Triangle area:", triangle_area(3, 4, 5))
print("Rectangle perimeter:", rectangle_perimeter(2, 5))
print("Distance:", euclidean_distance((0, 0), (3, 4)))