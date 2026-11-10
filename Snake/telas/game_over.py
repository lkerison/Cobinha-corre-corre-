import sys
import pygame
from configures import (
    BRANCO,
    CINZA,
    CINZA_CLARO,
    LARGURA,
    PRETO,
    TELA,
    VERMELHO,
    VERMELHO_ESCURO,
)


def desenha_texto_centralizado(texto, fonte, cor, y):
    """Renderiza o texto centralizado horizontalmente na tela."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(LARGURA // 2, y))
    TELA.blit(superficie, retangulo)


def desenha_botoes_instrucoes(x, y, largura, altura, texto, cor, destaque=False):
    """Desenha uma caixa de instrução com destaque visual."""
    retangulo = pygame.Rect(x, y, largura, altura)
    cor_borda = destaque and (100, 255, 140) or CINZA_CLARO

    pygame.draw.rect(TELA, (18, 18, 18), retangulo, border_radius=12)
    pygame.draw.rect(TELA, cor_borda, retangulo, width=2, border_radius=12)

    superficie = pygame.font.SysFont("Arial", 24, bold=True).render(texto, True, cor)
    rect_texto = superficie.get_rect(center=retangulo.center)
    TELA.blit(superficie, rect_texto)


def tela_game_over(pontos):
    """Exibe a tela final com mensagem impactante e opções claras."""
    pygame.event.clear()

    fonte_titulo = pygame.font.SysFont("Arial", 64, bold=True)
    fonte_pontos = pygame.font.SysFont("Arial", 32, bold=True)
    fonte_aviso = pygame.font.SysFont("Arial", 22)

    while True:
        TELA.fill(PRETO)

        painel = pygame.Rect(LARGURA // 2 - 260, 90, 520, 380)
        sombra = painel.move(10, 12)
        pygame.draw.rect(TELA, (10, 10, 10), sombra, border_radius=24)
        pygame.draw.rect(TELA, (35, 35, 35), painel, border_radius=24)
        pygame.draw.rect(TELA, VERMELHO, painel, width=3, border_radius=24)

        # Título com efeito de sombra
        texto_sombra = fonte_titulo.render("GAME OVER", True, VERMELHO_ESCURO)
        posicao_sombra = texto_sombra.get_rect(center=(LARGURA // 2 + 4, 186 + 4))
        TELA.blit(texto_sombra, posicao_sombra)

        texto_titulo = fonte_titulo.render("GAME OVER", True, VERMELHO)
        posicao_titulo = texto_titulo.get_rect(center=(LARGURA // 2, 180))
        TELA.blit(texto_titulo, posicao_titulo)

        texto_pontos = fonte_pontos.render(f"Pontuação final: {pontos}", True, BRANCO)
        rect_pontos = texto_pontos.get_rect(center=(LARGURA // 2, 255))
        TELA.blit(texto_pontos, rect_pontos)

        texto_aviso = fonte_aviso.render("A jornada acabou, mas a partida pode recomeçar!", True, (200, 200, 200))
        rect_aviso = texto_aviso.get_rect(center=(LARGURA // 2, 305))
        TELA.blit(texto_aviso, rect_aviso)

        largura_botoes = 360
        altura_botoes = 46
        x_botoes = LARGURA // 2 - largura_botoes // 2
        desenha_botoes_instrucoes(x_botoes, 405, largura_botoes, altura_botoes, "Q - VOLTAR AO MENU", BRANCO)

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
