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
        self.tempo_entre_ataques = 90
        self.duracao_telegraph = 18

    def iniciar_telegraph(self):
        self.attack_state = "telegraph"
        self.telegraph_timer = self.duracao_telegraph

    def mover(self, alvo=None):
        self.timer += 1
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x <= 40 or self.x + self.tamanho >= LARGURA - 40:
            self.vel_x *= -1
        if self.y <= 40 or self.y + self.tamanho >= ALTURA - 80:
            self.vel_y *= -1

        if self.attack_state == "telegraph":
            self.telegraph_timer -= 1
            if self.telegraph_timer <= 0:
                self.attack_state = "idle"
                self.timer = 0
                return

        if self.timer >= self.tempo_entre_ataques:
            self.iniciar_telegraph()

    def desenhar(self):
        if self.attack_state == "telegraph":
            cor_base = (255, 220, 90)
            contorno = (255, 180, 0)
            brilho = 1 + abs((self.telegraph_timer % 8) - 4) * 0.15
        else:
            cor_base = VERMELHO
            contorno = VERMELHO_ESCURO
            brilho = 1

        retangulo = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        sombra = pygame.Rect(self.x - 4, self.y - 4, self.tamanho + 8, self.tamanho + 8)

        pygame.draw.rect(TELA, (120, 15, 15), sombra, border_radius=10)
        pygame.draw.rect(TELA, cor_base, retangulo, border_radius=8)
        pygame.draw.rect(TELA, contorno, retangulo, width=3, border_radius=8)

        if self.attack_state == "telegraph":
            linha = pygame.Rect(self.x - 6, self.y - 6, self.tamanho + 12, self.tamanho + 12)
            pygame.draw.rect(TELA, (255, 235, 150), linha, 2, border_radius=12)

        olho_1 = (self.x + self.tamanho * 0.3, self.y + self.tamanho * 0.35)
        olho_2 = (self.x + self.tamanho * 0.7, self.y + self.tamanho * 0.35)
        pygame.draw.circle(TELA, (20, 20, 20), (int(olho_1[0]), int(olho_1[1])), max(2, int(3 * brilho)))
        pygame.draw.circle(TELA, (20, 20, 20), (int(olho_2[0]), int(olho_2[1])), max(2, int(3 * brilho)))

        largura_barra = self.tamanho
        altura_barra = 6
        porcentagem = max(0, self.vida / self.vida_maxima)

        pygame.draw.rect(TELA, (90, 0, 0), (self.x, self.y - 12, largura_barra, altura_barra))
        pygame.draw.rect(TELA, (255, 160, 40), (self.x, self.y - 12, largura_barra * porcentagem, altura_barra))

    def colidiu_com_cabeca(self, cabeca):
        rect_cabeca = pygame.Rect(cabeca[0], cabeca[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        rect_boss = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        return rect_cabeca.colliderect(rect_boss)
