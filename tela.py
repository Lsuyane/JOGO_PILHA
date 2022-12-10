import pygame
from imgs import Tela
from pygame.locals import *
from game import Play
from main import jogo_pilha

pygame.init()

tela_jogo = pygame.display.set_mode((900, 600))
tela = Tela()
tela_t = pygame.sprite.Group()
tela_t.add(tela)

font = pygame.font.Font('visitor2.ttf', 52)

pygame.display.set_caption("BURGUER")
clock = pygame.time.Clock()


def botton():
    mousex, mousey = pygame.mouse.get_pos()
    click = False

    iniciar = pygame.Rect(300, 150, 240, 55)
    ajuda = pygame.Rect(300, 150, 240, 55)
    sair = pygame.Rect(300, 150, 240, 55)
    retornarnmenu = pygame.Rect(300, 150, 240, 55)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    if iniciar.collidepoint((mousex, mousey)):
        if click:
            assert True
    if ajuda.collidepoint((mousex, mousey)):
        if click:
            assert True
    if sair.collidepoint((mousex, mousey)):
        if click:
            assert True
    if retornarnmenu.collidepoint((mousex, mousey)):
        if click:
            assert True

def orientacao():
    global click
    tela.image = tela.ajuda
    tela_t.draw(tela_jogo)

    font = pygame.font.Font('visitor2.ttf', 32)
    mousex, mousey = pygame.mouse.get_pos()

    retornarmenu = pygame.Rect(300, 500, 240, 55)
    pygame.draw.rect(tela_jogo, (230, 210, 100), retornarmenu)

    if retornarmenu.collidepoint((mousex, mousey)):
        pygame.draw.rect(tela_jogo, (255, 200, 100), retornarmenu)
        if click:
            menu()
            pygame.display.flip()
    write('MENU', font, (110, 110, 110), tela_jogo, 420, 525)

    click = False
    pygame.display.update()
    rodar = True
    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or click == True:
                rodar = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    rodar = False

def mennu():
    global clock
    clock.tick(5)

def write(text, font, color, surface, x, y):
    texto = font.render(text, 1, color)
    textt = texto.get_rect()
    textt.center = (x, y)
    surface.blit(texto, textt)

def menu():
    global click


    while True:
        tela.image = tela.back
        tela_t.draw(tela_jogo)

        mennu()
        m = pygame.Rect(0, 30, 1000, 40)
        pygame.draw.rect(tela_jogo, (230, 210, 100), m)
        write('MONTE SEU HAMBURGUER!', font, (110, 110, 110), tela_jogo, 430, 50)

        mousex, mousey = pygame.mouse.get_pos()

        iniciar = pygame.Rect(300, 150, 240, 55)
        ajuda = pygame.Rect(300, 250, 240, 55)
        sair = pygame.Rect(300, 350, 240, 55)

        pygame.draw.rect(tela_jogo, (230, 210, 100), iniciar)
        pygame.draw.rect(tela_jogo, (230, 210, 100), ajuda)
        pygame.draw.rect(tela_jogo, (230, 210, 100), sair)

        if iniciar.collidepoint((mousex, mousey)):
            pygame.draw.rect(tela_jogo, (255, 200, 100), iniciar)
            if click:
                pao_1 = Play(1, 1)
                paoint_1 = Play(2, 1)
                carne_1 = Play(3, 1)
                queijo_1 = Play(4, 1)

                jogo.empty()
                jogo.add(pao_1, paoint_1, carne_1, queijo_1)

                tela.image = tela.nivel
                tela.setSize(0, 0)
                tela_t.add(tela)
                jogo_pilha()

        if ajuda.collidepoint((mousex, mousey)):
            pygame.draw.rect(tela_jogo, (255, 200, 100), ajuda)
            if click:
                orientacao()

        if sair.collidepoint((mousex, mousey)):
            pygame.draw.rect(tela_jogo, (255, 200, 100), sair)
            if click:
                pygame.quit()

        write('Iniciar', font, (110, 110, 110), tela_jogo, 420, 175)
        write('Ajuda', font, (110, 110, 110), tela_jogo, 420, 275)
        write('Sair', font, (110, 110, 110), tela_jogo, 420, 375)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        pygame.display.flip()


pao_1 = Play(1, 1)
paoint_1 = Play(2, 1)
carne_1 = Play(3, 1)
queijo_1 = Play(4, 1)

jogo = pygame.sprite.Group()
jogo.add(pao_1, paoint_1, carne_1, queijo_1)



