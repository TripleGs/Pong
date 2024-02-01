#Manages the player
class Player():
    def __init__(self, x, y):
        self.color = (255,255,255)
        self.size = (15, 60)
        self.x = x
        self.y = y
        self.score = 0
        self.rect = 0
