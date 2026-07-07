import pygame
import random
import sys

# Inicialização
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TAMANHO_BLOCO = 20

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game - Médio")

# FPS
clock = pygame.time.Clock()
FPS = 60

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (40, 40, 40)

# Fonte
fonte = pygame.font.SysFont("Arial", 25)


def desenhar_grade():
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(TELA, CINZA, (x, 0), (x, ALTURA))

    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(TELA, CINZA, (0, y), (LARGURA, y))


def mostrar_texto(texto, cor, x, y):
    render = fonte.render(texto, True, cor)
    TELA.blit(render, (x, y))


class Snake:
    def __init__(self):
        self.corpo = [
            [LARGURA // 2, ALTURA // 2],
            [LARGURA // 2 - TAMANHO_BLOCO, ALTURA // 2],
            [LARGURA // 2 - (TAMANHO_BLOCO * 2), ALTURA // 2]
        ]

        self.direcao = "RIGHT"
        self.nova_direcao = self.direcao
        self.crescer = False

    def mover(self):
        self.direcao = self.nova_direcao

        x, y = self.corpo[0]

        if self.direcao == "UP":
            y -= TAMANHO_BLOCO
        elif self.direcao == "DOWN":
            y += TAMANHO_BLOCO
        elif self.direcao == "LEFT":
            x -= TAMANHO_BLOCO
        elif self.direcao == "RIGHT":
            x += TAMANHO_BLOCO

        nova_cabeca = [x, y]
        self.corpo.insert(0, nova_cabeca)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def desenhar(self):
        for i, segmento in enumerate(self.corpo):
            cor = VERDE if i == 0 else (0, 180, 0)

            pygame.draw.rect(
                TELA,
                cor,
                (segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
            )

    def verificar_colisao(self):
        x, y = self.corpo[0]

        # Parede
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            return True

        # Corpo
        if self.corpo[0] in self.corpo[1:]:
            return True

        return False


class Comida:
    def __init__(self):
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self):
        x = random.randint(0, (LARGURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        y = random.randint(0, (ALTURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        return [x, y]

    def desenhar(self):
        pygame.draw.rect(
            TELA,
            VERMELHO,
            (self.posicao[0], self.posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

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
                    jogo()
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def jogo():
    snake = Snake()
    comida = Comida()

    pontos = 0
    velocidade_cobra = 8      # movimentos por segundo
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

       # Comer comida
        if snake.corpo[0] == comida.posicao:
            snake.crescer = True
            comida.posicao = comida.gerar_posicao()
            pontos += 10
            velocidade_cobra += 0.5

# Colisão
        if snake.verificar_colisao():
            tela_game_over(pontos)

           

        # Colisão
        if snake.verificar_colisao():
            tela_game_over(pontos)

        # Desenho
        TELA.fill(PRETO)

        desenhar_grade()
        snake.desenhar()
        comida.desenhar()
    
        mostrar_texto(f"Pontos: {pontos}", BRANCO, 10, 10)
        

        pygame.display.update()


if __name__ == "__main__":
    jogo()
