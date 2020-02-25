import forca
import adivinhacao


def esolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    return int(input("Qual jogo?"))


def menu():
    jogo = esolher_jogo()

    if jogo == 1:
        print("Jogando Forca...")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação...")
        adivinhacao.jogar()

    print("Fim do jogo")


if __name__ == "__main__":
    menu()
    