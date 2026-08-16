from telas.jogos import jogo
from telas.menu import menu, creditos


if __name__ == "__main__":

    while True:

        tela_atual = menu()

        if tela_atual == "jogo":
            jogo()

        elif tela_atual == "creditos":
            creditos()
