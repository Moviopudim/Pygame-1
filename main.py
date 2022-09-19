import pygame, sys
from pygame.locals import *


def main():

    #Inicializa as libs
    pygame.init()
    pygame.font.init()

    #cores
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)

    #variavel que dita o tamnho vertical da tela
    screen_size_x = 900

    #variavel dos pontos
    points = 0

    #atribui a posição x e y a variaveis
    y = 100
    x = screen_size_x / 2

    #velocidade do pleyer
    speed = 0

    #aceleração
    acceleration = 0.001

    #atribui a fonte a uma variavel
    font = pygame.font.Font("freesansbold.ttf", 32)

    #inicializa a tela
    screen = pygame.display.set_mode((screen_size_x, 900), 0, 32)

    #loop (quase)infinito
    while True:
        #define o texto que será blitado
        text = font.render(str(points), False, (0, 255, 0))

        #atribui a função de teclas a uma variavel
        keys = pygame.key.get_pressed()

        #pinta a tela de bracop a cada frame
        screen.fill(white)

        #desenha o player
        pygame.draw.rect(screen, blue, (x, y, 100, 100))

        #gravidade
        y += speed
        speed += acceleration

        #colisão super foda de 2 linhas
        if y >= 600:
            speed=0

        #blita o texto nos valores x e y do player
        screen.blit(text, (x, y))

        for event in pygame.event.get():
            #evento de pulo e pontos
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    speed = -0.5
                    points += 1
            
            #evento que encerra tudo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #printa, no console, a posição do player
        print(f"PosX: {x} PosY: {y}")

        #atualiza o display a cada segundo
        pygame.display.update()


if __name__ == '__main__':
    main()
