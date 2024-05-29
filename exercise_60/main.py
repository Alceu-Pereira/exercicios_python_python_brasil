class Square:
    def __self__(self, side_size):
        self.side_size = side_size

    def changeSizeValue(self, new_value):
        self.side_size = new_value

    def showSizeValue(self):
        return self.side_size
    
    def areaCalcule(self):
        return ((float(self.side_size)) ** 2)
    
my_square = Square()

my_square.side_size = 1.5


print(my_square.showSizeValue())

my_square.changeSizeValue(2)
print(my_square.areaCalcule())