import pygame

pygame.init()


LARGURA = 800
ALTURA = 600
TAMANHO_BLOCO = 20


TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()
FPS = 60


PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
VERDE = (50, 200, 80)
VERDE_CLARO = (100, 255, 120)
VERMELHO = (230, 50, 50)
VERMELHO_ESCURO = (180, 30, 30)
CINZA = (40, 40, 40)
CINZA_CLARO = (120, 120, 120)


fonte = pygame.font.SysFont("Arial", 25)
fonte_titulo = pygame.font.SysFont("Arial", 60, bold=True)
fonte_botao = pygame.font.SysFont("Arial", 28, bold=True)
fonte_creditos = pygame.font.SysFont("Arial", 24)
