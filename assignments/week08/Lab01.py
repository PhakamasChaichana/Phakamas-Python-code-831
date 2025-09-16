"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class rectangle :
    def __init__(self,length,width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width

    def get_perimeter(self):
        return 2 *(self._length + self._width)

    def issquare(self):
        return self._length == self._width

rect = rectangle(10, 5)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.issquare())