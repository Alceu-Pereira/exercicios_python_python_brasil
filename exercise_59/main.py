class Ball:
    def __self__(self, color, circle, feedstock):
        self.color = color
        self.circle = circle
        self.feedstock = feedstock

    def changeColor(self, newcolor):
        self.color = newcolor

    def showColor(self):
        print(self.color)


my_ball = Ball()

my_ball.color = 'Blue'
my_ball.circle = '1.2'
my_ball.feedstock = 'plastic'

# my_ball.changeColor('Red')

my_ball.showColor()