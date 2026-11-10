import os
import sys
import pygame
from configures import BRANCO, FPS, LARGURA, PRETO, TELA, TAMANHO_BLOCO, VERDE, clock
from models.boss import Boss
from models.comida import Comida
from models.snake import Snake
from telas.game_over import tela_game_over
from utils.desenho import desenhar_grade, mostrar_texto
from configures import TELA, LARGURA, ALTURA


def desenha_texto_centralizado(texto, fonte, cor, y):
    """Auxiliar para exibir texto centralizado na tela."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(LARGURA // 2, y))
    TELA.blit(superficie, retangulo)


def tela_transicao_fase(fase_concluida):
    """Tela intermediária que exige ação do jogador para avançar."""
    pygame.event.clear()
    fonte_titulo = pygame.font.SysFont("Arial", 46, bold=True)
    fonte_instrucao = pygame.font.SysFont("Arial", 24, bold=True)

    while True:
        TELA.fill(PRETO)

        desenha_texto_centralizado(
            f"FASE {fase_concluida} CONCLUÍDA!", fonte_titulo, VERDE, 220
        )
        desenha_texto_centralizado(
            "aperte ESPAÇO para passa de fase",
            fonte_instrucao,
            BRANCO,
            340,
        )

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    return


def tela_vitoria():
    """Tela exibida ao derrotar o Boss final."""
    pygame.event.clear()
    fonte_titulo = pygame.font.SysFont("Arial", 46, bold=True)
    fonte_instrucao = pygame.font.SysFont("Arial", 24, bold=True)

    while True:
        TELA.fill(PRETO)

        desenha_texto_centralizado(
            "VOCÊ DERROTOU O BOSS!", fonte_titulo, VERDE, 220
        )
        desenha_texto_centralizado(
            "aperte ESPAÇO para voltar ao Menu",
            fonte_instrucao,
            BRANCO,
            340,
        )

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    return

#essa parte do codigo é referente a o fundo da fase#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_FUNDO = os.path.join(BASE_DIR,"assets", "fundo")

fundo_fase1 = pygame.image.load(os.path.join(PASTA_FUNDO,"fase1.png")).convert()
fundo_fase1 = pygame.transform.scale(fundo_fase1, (LARGURA , ALTURA))

fundo_fase2 = pygame.image.load(os.path.join(PASTA_FUNDO, "fase2.png")).convert()
fundo_fase2 = pygame.transform.scale(fundo_fase2, (LARGURA, ALTURA))

fundo_fase3 = pygame.image.load(os.path.join(PASTA_FUNDO, "fase3.png")).convert()
fundo_fase3 = pygame.transform.scale(fundo_fase3, (LARGURA, ALTURA))

def colisao_boss_com_snake(boss, snake):
    if not boss or not snake:
        return False

    rect_boss = pygame.Rect(boss.x, boss.y, boss.tamanho, boss.tamanho)

    for segmento in snake.corpo:
        rect_segmento = pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        if rect_boss.colliderect(rect_segmento):
            return True

    return False



def desenhar_hud(pontos, fase, boss=None):
    painel = pygame.Surface((300, 34), pygame.SRCALPHA)

    pygame.draw.rect(
        painel,
        (10, 15, 25, 175),
        (0, 0, 300, 34),
        border_radius=10
    )

    pygame.draw.rect(
        painel,
        (100, 150, 190, 180),
        (0, 0, 300, 34),
        width=1,
        border_radius=10
    )

    fonte = pygame.font.SysFont("Arial", 16, bold=True)

    texto = f"PONTOS: {pontos}   |   FASE: {fase}"

    if boss:
        texto += f"   |   BOSS: {max(0, boss.vida)}"

    superficie = fonte.render(texto, True, BRANCO)

    retangulo = superficie.get_rect(
        center=(150, 17)
    )

    painel.blit(superficie, retangulo)

    TELA.blit(
        painel,
        ((LARGURA - 300) // 2, 3)
    )


limites_fases = {
 1: pygame.Rect(40, 40, 720, 520),
 2: pygame.Rect(40, 40, 720, 520),
 3: pygame.Rect(60, 40, 680, 520),
}


def jogo():
    configuracao_fases = {
        1: {"meta": 4, "velocidade": 7, "fundo": fundo_fase1},
        2: {"meta": 6, "velocidade": 9, "fundo": fundo_fase2},
        3: {"meta": None, "velocidade": 11, "fundo": fundo_fase3},
    }

    def preparar_fase(nova_fase):
        nonlocal snake, comida, boss, pontos, velocidade_cobra, fase
        fase = nova_fase
        snake = Snake()
        comida = Comida(limite_mapa=limites_fases[nova_fase], obstaculos=[])
        velocidade_cobra = configuracao_fases[nova_fase]["velocidade"]
        pontos = 0
        boss = Boss() if nova_fase == 3 else None

    def resetar_partida():
        preparar_fase(1)

    snake = Snake()
    comida = Comida(limite_mapa=limites_fases[1], obstaculos=[])
    boss = None
    pontos = 0
    fase = 1
    velocidade_cobra = configuracao_fases[1]["velocidade"]
    tempo_movimento = 0

    while True:
        dt = clock.tick(FPS)
        tempo_movimento += dt

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    snake.definir_direcao("UP")
                elif evento.key == pygame.K_DOWN:
                    snake.definir_direcao("DOWN")
                elif evento.key == pygame.K_LEFT:
                    snake.definir_direcao("LEFT")
                elif evento.key == pygame.K_RIGHT:
                    snake.definir_direcao("RIGHT")

        if tempo_movimento >= 1000 / velocidade_cobra:
            snake.mover()

            if fase == 3 and boss:
                boss.mover(snake.corpo[0])

            tempo_movimento = 0

            if snake.corpo[0] == comida.posicao:
                snake.crescer = True
                comida.posicao = comida.gerar_posicao(snake.corpo)
                if comida.posicao is None:
                    tela_vitoria()
                    return
                pontos += 1
                velocidade_cobra = min(velocidade_cobra + 0.2, 14)

                if fase == 1 and pontos >= configuracao_fases[1]["meta"]:
                    tela_transicao_fase(1)
                    preparar_fase(2)

                elif fase == 2 and pontos >= configuracao_fases[2]["meta"]:
                    tela_transicao_fase(2)
                    preparar_fase(3)

                elif fase == 3 and boss:
                    boss.vida -= 1
                    if boss.vida <= 0:
                        tela_vitoria()
                        return

            colidiu_com_boss = fase == 3 and colisao_boss_com_snake(boss, snake)

            limite_mapa = limites_fases[fase]

            if snake.verificar_colisao(limite_mapa) or colidiu_com_boss:
                reiniciar = tela_game_over(pontos)

                if reiniciar:
                  resetar_partida()
                else:
                     return

        TELA.blit(configuracao_fases[fase]["fundo"], (0, 0))
        desenhar_grade()
        snake.desenhar()
        comida.desenhar()

        if fase == 3 and boss:
            boss.desenhar()

        desenhar_hud(pontos, fase, boss)
        pygame.display.update()
