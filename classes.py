class spaceship:
    def __init__(self, image, X, Y, speedX, speedY, health, CHP):
        self.image = image
        self.X = X
        self.Y = Y
        self.speedX = speedX
        self.speedY = speedY
        self.health = health
        self.CHP = CHP
class bullet:
    def __init__(self, image, X, Y, speedX, speedY, ready):
        self.image = image
        self.X = X
        self.Y = Y
        self.speedX = speedX
        self.speedY = speedY
        self.ready = ready
class barrier:
    def __init__(self, image, X, Y, health, CHP):
        self.image = image
        self.X = X
        self.Y = Y
        self.health = health
        self.CHP = CHP