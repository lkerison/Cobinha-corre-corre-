import pygame
import sys
from utils.desenho import mostrar_texto

from configures import (
    TELA,
    PRETO,
    BRANCO,
    VERDE,
    VERMELHO
)

from utils.desenho import mostrar_texto

def tela_game_over(pontos):
    while True:
        TELA.fill(PRETO)

        mostrar_texto("GAME OVER", VERMELHO, 320, 220)
        mostrar_texto(f"Pontos: {pontos}", BRANCO, 340, 270)
        mostrar_texto("R - Reiniciar", VERDE, 320, 330)
        mostrar_texto("Q - Sair", VERDE, 350, 370)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
             if evento.key == pygame.K_r:
                return True

            elif evento.key == pygame.K_q:
                return False