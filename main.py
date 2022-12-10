import pygame
import tela

pygame.init()

def jogo_pilha():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        tela.tela_t.draw(tela.tela_jogo)
        tela.jogo.draw(tela.tela_jogo)

        tela.tela_t.update()
        tela.jogo.update()

        pygame.display.update()

if __name__ == "__main__":
    tela.menu()