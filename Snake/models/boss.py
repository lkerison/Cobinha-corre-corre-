import pygame
from configures import ALTURA, LARGURA, TAMANHO_BLOCO, TELA, VERMELHO, VERMELHO_ESCURO


class Boss:

    def __init__(self):
        
        self.tamanho = TAMANHO_BLOCO * 2
        self.x = LARGURA // 2 - self.tamanho // 2
        self.y = 100
        self.vida_maxima = 5
        self.vida = self.vida_maxima
        self.vel_x = TAMANHO_BLOCO
        self.vel_y = TAMANHO_BLOCO

    def mover(self):
        
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x <= 0 or self.x + self.tamanho >= LARGURA:
            self.vel_x *= -1
        if self.y <= 0 or self.y + self.tamanho >= ALTURA:
            self.vel_y *= -1

    def desenhar(self):
        retangulo = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        pygame.draw.rect(TELA, VERMELHO_ESCURO, retangulo, border_radius=6)
        pygame.draw.rect(TELA, VERMELHO, retangulo, width=3, border_radius=6)

        
        largura_barra = self.tamanho
        altura_barra = 6
        porcentagem = max(0, self.vida / self.vida_maxima)

        pygame.draw.rect(
            TELA, (100, 0, 0), (self.x, self.y - 10, largura_barra, altura_barra)
        )
        pygame.draw.rect(
            TELA,
            (0, 255, 0),
            (self.x, self.y - 10, largura_barra * porcentagem, altura_barra),
        )

    def colidiu_com_cabeca(self, cabeca):
        
        rect_cabeca = pygame.Rect(
            cabeca[0], cabeca[1], TAMANHO_BLOCO, TAMANHO_BLOCO
        )
        rect_boss = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        return rect_cabeca.colliderect(rect_boss)
