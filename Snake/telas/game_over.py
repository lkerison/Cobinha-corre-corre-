import sys
import pygame
from configures import ALTURA, BRANCO, LARGURA, PRETO, TELA, VERDE, VERMELHO


def desenha_texto_centralizado(texto, fonte, cor, y):
    """Renderiza o texto centralizado horizontalmente na tela."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(LARGURA // 2, y))
    TELA.blit(superficie, retangulo)


def tela_game_over(pontos):

    pygame.event.clear()


    fonte_titulo = pygame.font.SysFont("Arial", 54, bold=True)
    fonte_pontos = pygame.font.SysFont("Arial", 30)
    fonte_instrucoes = pygame.font.SysFont("Arial", 24, bold=True)

    while True:
        TELA.fill(PRETO)


        desenha_texto_centralizado("GAME OVER", fonte_titulo, VERMELHO, 160)
        desenha_texto_centralizado(
            f"Pontuação Final: {pontos}", fonte_pontos, BRANCO, 240
        )

        desenha_texto_centralizado(
            "aperte R para recomeça a fase",
            fonte_instrucoes,
            VERDE,
            330,
        )
        desenha_texto_centralizado(
            "aperte atecla Q pra volta ao menu",
            fonte_instrucoes,
            BRANCO,
            380,
        )

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
