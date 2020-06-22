class spaceship:
    def __init__(self, image, X, Y, speedX, speedY, health, CHP, angle, rotation):
        self.image = image
        self.X = X
        self.Y = Y
        self.speedX = speedX
        self.speedY = speedY
        self.health = health
        self.CHP = CHP
        self.angle = angle
        self.rotation = rotation
class bullet:
    def __init__(self, image, X, Y, speed, X_change, Y_change, ready, angle, rotation):
        self.image = image
        self.X = X
        self.Y = Y
        self.speed = speed
        self.X_change = X_change
        self.Y_change = Y_change
        self.ready = ready
        self.angle = angle
        self.rotation = rotation
class barrier:
    def __init__(self, image, X, Y, health, CHP):
        self.image = image
        self.X = X
        self.Y = Y
        self.health = health
        self.CHP = CHP