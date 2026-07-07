import pygame
import sys
from utils.desenho import desenhar_grade, mostrar_texto

from configures import (
    TELA,
    FPS,
    clock,
    PRETO,
    BRANCO
)

from models.snake import Snake
from models.comida import Comida

from utils.desenho import (
    desenhar_grade,
    mostrar_texto
)

from telas.game_over import tela_game_over

def jogo():
    snake = Snake()
    comida = Comida()

    pontos = 0
    velocidade_cobra = 8      
    tempo_movimento = 0

    while True:
        dt = clock.tick(FPS)
        tempo_movimento += dt

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and snake.direcao != "DOWN":
                    snake.nova_direcao = "UP"

                elif evento.key == pygame.K_DOWN and snake.direcao != "UP":
                    snake.nova_direcao = "DOWN"

                elif evento.key == pygame.K_LEFT and snake.direcao != "RIGHT":
                    snake.nova_direcao = "LEFT"

                elif evento.key == pygame.K_RIGHT and snake.direcao != "LEFT":
                    snake.nova_direcao = "RIGHT"

        if tempo_movimento >= 1000 / velocidade_cobra:
            snake.mover()
            tempo_movimento = 0


        if snake.corpo[0] == comida.posicao:
            snake.crescer = True
            comida.posicao = comida.gerar_posicao()
            pontos += 10
            velocidade_cobra += 0.5


        if snake.verificar_colisao():
            reiniciar = tela_game_over(pontos)

            if reiniciar:
                return jogo()
            else:
                pygame.quit()
                sys.exit()




        TELA.fill(PRETO)

        desenhar_grade()
        snake.desenhar()
        comida.desenhar()
    
        mostrar_texto(f"Pontos: {pontos}", BRANCO, 10, 10)
        

        pygame.display.update()
