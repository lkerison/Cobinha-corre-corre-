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
        self.attack_state = "idle"
        self.telegraph_timer = 0
        self.timer = 0

    def mover(self, alvo=None):
        self.timer += 1
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x <= 0 or self.x + self.tamanho >= LARGURA:
            self.vel_x *= -1
        if self.y <= 0 or self.y + self.tamanho >= ALTURA:
            self.vel_y *= -1

        if self.timer % 60 == 0:
            self.attack_state = "telegraph"
            self.telegraph_timer = 15

        if self.attack_state == "telegraph":
            self.telegraph_timer -= 1
            if self.telegraph_timer <= 0:
                self.attack_state = "idle"

    def desenhar(self):
        if self.attack_state == "telegraph":
            cor_base = (255, 220, 90)
            contorno = (255, 180, 0)
        else:
            cor_base = VERMELHO
            contorno = VERMELHO_ESCURO

        retangulo = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        sombra = pygame.Rect(self.x - 4, self.y - 4, self.tamanho + 8, self.tamanho + 8)

        pygame.draw.rect(TELA, (120, 15, 15), sombra, border_radius=10)
        pygame.draw.rect(TELA, cor_base, retangulo, border_radius=8)
        pygame.draw.rect(TELA, contorno, retangulo, width=3, border_radius=8)

        olho_1 = (self.x + self.tamanho * 0.3, self.y + self.tamanho * 0.35)
        olho_2 = (self.x + self.tamanho * 0.7, self.y + self.tamanho * 0.35)
        pygame.draw.circle(TELA, (20, 20, 20), (int(olho_1[0]), int(olho_1[1])), 3)
        pygame.draw.circle(TELA, (20, 20, 20), (int(olho_2[0]), int(olho_2[1])), 3)

        largura_barra = self.tamanho
        altura_barra = 6
        porcentagem = max(0, self.vida / self.vida_maxima)

        pygame.draw.rect(TELA, (90, 0, 0), (self.x, self.y - 12, largura_barra, altura_barra))
        pygame.draw.rect(TELA, (255, 160, 40), (self.x, self.y - 12, largura_barra * porcentagem, altura_barra))

    def colidiu_com_cabeca(self, cabeca):
        rect_cabeca = pygame.Rect(cabeca[0], cabeca[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        rect_boss = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        return rect_cabeca.colliderect(rect_boss)
