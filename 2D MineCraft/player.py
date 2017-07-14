class Player:

    def __init__(self, posX, posY, window):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.color = (1,1,1)
        self.size = 10
        self.jump = True
        self.direction = 'right'
        self.target = (0, 0)
        self.window = window

    def move(self, keys):
        self.velX = 0
        if keys['left'] or keys['a']:
            self.velX = -0.3
            self.direction = 'left'
        if keys['right'] or keys['d']:
            self.velX = 0.3
            self.direction = 'right'
        if (keys['up'] or keys['w']) and self.jump:
            self.velY = -0.3
            self.jump = False
            self.direction = 'up'
        if keys['down']:
            self.direction = 'down'

    def draw(self, shift):

        self.window.drawCircle(self.posX + shift[0], self.posY + shift[1], self.size, self.color[0], self.color[1], self.color[2])

    def update(self):
        if self.direction == 'left':
            self.target = (self.posX - 30, self.posY)
        if self.direction == 'right':
            self.target = (self.posX + 30, self.posY)
        if self.direction == 'up':
            self.target = (self.posX, self.posY - 30)
        if self.direction == 'down':
            self.target = (self.posX, self.posY + 30)