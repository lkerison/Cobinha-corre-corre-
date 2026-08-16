import pygame
import sys

pygame.init()
TELA = pygame.display.set_mode((800, 600))

# a tela do menu e as cores do dele 
LARGURA = 800
ALTURA = 600

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('snake game')

clock = pygame.time.Clock()

PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
VERDE = (50 , 200, 80)
VERDE_CLARO = (100, 255, 120)
CINZA = (80, 80, 80)
CINZA_CLARO = (120, 120, 120)

fonte_titulo = pygame.font.SysFont('Arial',60, bold=True)
fonte_botao = pygame.font.SysFont('Arial',28, bold=True)
fonte_creditos= pygame.font.SysFont('Arial',24)

    
def desenha_texto(texto, fonte,cor, x, y,):
    superficie = fonte.render (texto,True, cor )
    retangulo = superficie.get_rect(center=(x, y))
    TELA.blit(superficie, retangulo)


def desenha_botao(texto, x , y , lagura, altura):
    mouse = pygame.mouse.get_pos()

    retangulo = pygame.Rect(x, y, lagura, altura)

    if retangulo.collidepoint(mouse):
        cor = VERDE_CLARO
    else:
        cor = VERDE

    pygame.draw.rect(TELA, cor, retangulo, border_radius=10)
    pygame.draw.rect(TELA, BRANCO, retangulo, 2, border_radius=10)

    desenha_texto(
        texto,
        fonte_botao,
        PRETO,
        retangulo.centerx,
        retangulo.centery
    )
    return retangulo

def menu():
    while True:
        TELA.fill(PRETO)

        desenha_texto(
            "SNAKE GAME",
            fonte_titulo,
            VERDE, 
            LARGURA // 2,
            120
        )

        botao_iniciar = desenha_botao(
            "INICIAL JOGO",
            250,
            220,
            300,
            60
        )


        botao_creditos = desenha_botao(
            'creditos',
            250,
            300,
            300,
            60
        )

        botao_sair = desenha_botao(
            'sair',
            250,
            380,
            300,
            60
        )
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:

                    if botao_iniciar.collidepoint(evento.pos):
                        return 'jogo'

                    if botao_creditos.collidepoint(evento.pos):
                        return 'creditos'

                    if botao_sair.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()
        clock.tick(60) 

def creditos():
    while True:

        TELA.fill(PRETO)

        desenha_texto(
            'CREDITOS',
            fonte_creditos,
            VERDE,
            LARGURA // 2,
            100
        )
        desenha_texto(
            'desenvolvido por kerison',
            fonte_creditos,
            BRANCO,
            LARGURA //2,
            220
        )
        desenha_texto(
            'KERISON',
            fonte_creditos,
            BRANCO,
            LARGURA //2,
            270
        )
        desenha_texto(
            'LUCAS',
            fonte_creditos,
            BRANCO,
            LARGURA //2,
            310
        )
        botao_voltar = desenha_botao(
            'VOLTAR',
            250,
            430,
            300,
            60
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
        clock.tick(60)                