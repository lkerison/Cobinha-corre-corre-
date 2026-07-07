import pygame
pygame.init()


LARGURA = 800
ALTURA = 600
TAMANHO_BLOCO = 20

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game - Médio")


clock = pygame.time.Clock()
FPS = 60


PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (40, 40, 40)


fonte = pygame.font.SysFont("Arial", 25)