#Manages the ball
class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 7
        self.color = (0,0,0)
        self.rect = 0
        self.modx = -5
        self.mody = 0
