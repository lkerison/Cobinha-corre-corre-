import os
import sys
import pygame
from configures import BRANCO, FPS, LARGURA, PRETO, TELA, VERDE, clock
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

def jogo():
    snake = Snake()
    comida = Comida()
    boss = None

    pontos = 0
    fase = 1
    velocidade_cobra = 8
    tempo_movimento = 0

    # Metas de pontos para concluir cada fase
    META_FASE_1 = 5  # 5 comidas
    META_FASE_2 = 7  # 7 comidas

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

            if fase == 3 and boss:
                boss.mover()

            tempo_movimento = 0

            # Lógica de pontuação e progresso
            if snake.corpo[0] == comida.posicao:
                snake.crescer = True
                comida.posicao = comida.gerar_posicao(snake.corpo)
                pontos += 1
                velocidade_cobra += 0.5

                # Transição da Fase 1 para a Fase 2
                if fase == 1 and pontos >= META_FASE_1:
                    tela_transicao_fase(1)
                    fase = 2
                    pontos = 0  # Zera os pontos
                    velocidade_cobra = 10
                    snake = Snake()
                    comida = Comida()

                # Transição da Fase 2 para a Fase 3 (Boss)
                elif fase == 2 and pontos >= META_FASE_2:
                    tela_transicao_fase(2)
                    fase = 3
                    pontos = 0  # Zera os pontos
                    boss = Boss()
                    snake = Snake()
                    comida = Comida()

                # Dano no Boss durante a Fase 3
                elif fase == 3 and boss:
                    boss.vida -= 1
                    if boss.vida <= 0:
                        tela_vitoria()
                        return

            # Colisão com o Boss
            colidiu_com_boss = (
                fase == 3 and boss and boss.colidiu_com_cabeca(snake.corpo[0])
            )

            # Colisão com paredes ou corpo
            if snake.verificar_colisao() or colidiu_com_boss:
                reiniciar = tela_game_over(pontos)

                if reiniciar:
                    snake = Snake()
                    comida = Comida()
                    boss = None
                    pontos = 0
                    fase = 1
                    velocidade_cobra = 8
                else:
                    return

        # Desenhar elementos
        if fase == 1:
            TELA.blit(fundo_fase1, (0, 0))
        elif fase == 2:
            TELA.blit(fundo_fase2, (0, 0))
        desenhar_grade()
        snake.desenhar()
        comida.desenhar()

        if fase == 3 and boss:
            boss.desenhar()

        mostrar_texto(f"Pontos: {pontos}  |  Fase: {fase}", BRANCO, 10, 10)
        pygame.display.update()
