class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        #Use a f-string to format your string representation
        return f'<{self.x},{self.x}>'
    def __eq__(self, other):
        if not isinstance(other, Coordinate):
               raise TypeError('An instance of class Coordinate is expected')
        return self.x == other.x and self.y == other.y


c1 = Coordinate(5, 5)
c2 = Coordinate(6, 6)

print(c1)
print(c2)
print(c1 == c1)
print(c1 == c2)
#print(c1 == 1)