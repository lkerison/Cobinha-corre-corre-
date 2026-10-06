import pygame
import sys
import os

from configures import (
    TELA,
    LARGURA,
    ALTURA,
    BRANCO,
    VERDE,
    PRETO,
    clock,
    FPS,
    fonte_creditos
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASTA_ASSETS = os.path.join(BASE_DIR, "assets")
PASTA_SPRITES = PASTA_ASSETS


fundo = pygame.image.load(
    os.path.join(PASTA_ASSETS, "fundo_menu.png")
).convert()

fundo = pygame.transform.scale(
    fundo,
    (LARGURA, ALTURA)
)


def carregar_sprite(nome):

    caminho = os.path.join(
        PASTA_SPRITES,
        nome
    )

    imagem = pygame.image.load(caminho).convert_alpha()

    imagem = pygame.transform.smoothscale(
        imagem,
        (300, 95)
    )

    return imagem


jogar_normal = carregar_sprite("jogar_normal.png")
jogar_hover = carregar_sprite("jogar_hover.png")
jogar_click = carregar_sprite("jogar_clicado.png")

creditos_normal = carregar_sprite("creditos_normal.png")
creditos_hover = carregar_sprite("creditos_hover.png")
creditos_click = carregar_sprite("creditos_clicado.png")

sair_normal = carregar_sprite("sair_normal.png")
sair_hover = carregar_sprite("sair_hover.png")
sair_click = carregar_sprite("sair_clicado.png")


def desenha_texto(texto, fonte, cor, x, y):

    superficie = fonte.render(
        texto,
        True,
        cor
    )

    retangulo = superficie.get_rect(
        center=(x, y)
    )

    TELA.blit(
        superficie,
        retangulo
    )


def desenhar_botao(
    normal,
    hover,
    click,
    x,
    y,
    mouse
):

    largura = normal.get_width()
    altura = normal.get_height()

    area = pygame.Rect(
        x,
        y,
        largura,
        altura
    )

    if area.collidepoint(mouse):

        posicao_y = y - 8

        TELA.blit(
            hover,
            (x, posicao_y)
        )

    else:

        TELA.blit(
            normal,
            (x, y)
        )

    return area


def menu():

    x = (LARGURA - 300) // 2

    botao_jogar = pygame.Rect(
        x,
        275,
        300,
        95
    )

    botao_creditos = pygame.Rect(
        x,
        375,
        300,
        95
    )

    botao_sair = pygame.Rect(
        x,
        475,
        300,
        95
    )

    while True:

        TELA.blit(
            fundo,
            (0, 0)
        )

        mouse = pygame.mouse.get_pos()

        desenhar_botao(
            jogar_normal,
            jogar_hover,
            jogar_click,
            x,
            275,
            mouse
        )

        desenhar_botao(
            creditos_normal,
            creditos_hover,
            creditos_click,
            x,
            375,
            mouse
        )

        desenhar_botao(
            sair_normal,
            sair_hover,
            sair_click,
            x,
            475,
            mouse
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:

                    if botao_jogar.collidepoint(evento.pos):
                        return "jogo"

                    elif botao_creditos.collidepoint(evento.pos):
                        return "creditos"

                    elif botao_sair.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()

        clock.tick(FPS)


def creditos():

    botao_voltar = pygame.Rect(
        250,
        430,
        300,
        60
    )

    while True:

        TELA.blit(
            fundo,
            (0, 0)
        )

        camada = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        camada.fill(
            (0, 0, 0, 160)
        )

        TELA.blit(
            camada,
            (0, 0)
        )

        desenha_texto(
            "CRÉDITOS",
            fonte_creditos,
            VERDE,
            LARGURA // 2,
            100
        )

        desenha_texto(
            "DESENVOLVIDO POR",
            fonte_creditos,
            BRANCO,
            LARGURA // 2,
            220
        )

        desenha_texto(
            "KERISON",
            fonte_creditos,
            BRANCO,
            LARGURA // 2,
            270
        )

        desenha_texto(
            "LUCAS",
            fonte_creditos,
            BRANCO,
            LARGURA // 2,
            310
        )

        mouse = pygame.mouse.get_pos()

        if botao_voltar.collidepoint(mouse):

            pygame.draw.rect(
                TELA,
                VERDE,
                botao_voltar,
                border_radius=10
            )

        else:

            pygame.draw.rect(
                TELA,
                PRETO,
                botao_voltar,
                border_radius=10
            )

        pygame.draw.rect(
            TELA,
            BRANCO,
            botao_voltar,
            2,
            border_radius=10
        )

        desenha_texto(
            "VOLTAR",
            fonte_creditos,
            BRANCO,
            botao_voltar.centerx,
            botao_voltar.centery
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:

                    if botao_voltar.collidepoint(evento.pos):
                        return

        pygame.display.flip()

        clock.tick(FPS)
