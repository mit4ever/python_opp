class Square:
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return(f"Square: {self.length}")    
    def area(self):
        return self.length * self.length
    def perimeter (self):
        return self.length * 4

class Rectangular:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return(f"Rectangular: {self.width}, {self.length}")
    def area(self):
        return self.length * self.width
    def perimeter (self):
        return (self.length + self.width) *2
list1 = [Square(4), Square(7), Square(6), Square (5), Square(9),Rectangular(2,5),Rectangular(3,4),Rectangular(4,5),Rectangular(7,8),Rectangular(9,4)]
for obj in list1:
    print(obj,"Chu vi: " ,obj.perimeter(), "Diện tích: ",obj.area())
