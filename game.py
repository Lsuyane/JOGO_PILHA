import pygame as pg

class Play(pg.sprite.Sprite):
    def __init__(self, ing, nivel):
        super().__init__()

        if nivel == 1:
            if ing == 1:
                self.x = 290
                self.image = pg.image.load("img/pao.png")
                self.velo = 1

            elif ing == 2:
                self.x = 375
                self.image = pg.image.load("img/paoinf.png")
                self.velo = 4

            elif ing == 3:
                self.x = 575
                self.image = pg.image.load("img/queijo.png")
                self.velo = 3

            elif ing == 4:
                self.x = 675
                self.image = pg.image.load("img/carne.png")
                self.velo = 2

        else:
            if ing == 1:
                self.x = 290
                self.image = pg.image.load("img/carne.png")
                self.velo = 2

            elif ing == 2:
                self.x = 375
                self.image = pg.image.load("img/tomate.png")
                self.velo = 3

            elif ing == 3:
                self.x = 575
                self.image = pg.image.load("img/queijo.png")
                self.velo = 5

            elif ing == 4:
                self.x = 375
                self.image = pg.image.load("img/paoinf.png")
                self.velo = 3

            else:
                self.x = 660
                self.image = pg.image.load("img/pao.png")
                self.velo = 3

        self.y = 650/2

        self.width = 140
        self.height = 150

        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.y += self.velo

        if self.y < 8:
            self.y = 200
            self.velo *= -1

        elif self.y + self.height > 750:
            self.y = 650 - self.height
            self.velo *= -1
