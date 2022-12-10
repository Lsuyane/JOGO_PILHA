import pygame


class Tela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.back = pygame.image.load("img/back.png")
        self.ajuda = pygame.image.load("img/ajuda.png")
        self.nivel = pygame.image.load("img/nivel1.png")
        self.carne = pygame.image.load("img/carne.png")
        self.tomate = pygame.image.load("img/tomate.png")
        self.prato = pygame.image.load("img/prato.png")
        self.queijo = pygame.image.load("img/queijo.png")
        self.pao = pygame.image.load("img/pao.png")

        self.back = pygame.transform.scale(self.back, (900, 600))
        self.ajuda = pygame.transform.scale(self.ajuda, (850, 600))
        self.nivel = pygame.transform.scale(self.nivel, (900, 600))


        self.image = self.back

        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def setSize(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.rect.topleft = (self.x, self.y)
