import pygame

from configures import (
    TELA,
    LARGURA,
    ALTURA,
    TAMANHO_BLOCO,
    CINZA,
    fonte
)


def desenhar_grade():
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(TELA, CINZA, (x, 0), (x, ALTURA))

    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(TELA, CINZA, (0, y), (LARGURA, y))


def mostrar_texto(texto, cor, x, y):
    render = fonte.render(texto, True, cor)
    TELA.blit(render, (x, y))