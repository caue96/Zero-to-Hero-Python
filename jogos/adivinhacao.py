import random


def abertura():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")


def escolher_nivel():
    print("Qual nível de dificuldade")
    print("(1) Fácil    (2) Médio   (3) Difícil")

    return int(input("Defina o nível: "))


def adivinhar_numero(rodada, total_tentativas):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)

    return int(chute_str)


def erro_chute(chute):  
    while (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        
        chute = int(chute_str)

        continue


def jogar():
    abertura()

    numero_secreto = random.randrange(1, 100)
    total_tentativas = 0
    pontos = 450

    nivel = escolher_nivel()

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        chute = adivinhar_numero(rodada, total_tentativas)

        erro_chute(chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


if (__name__ == "__main__"):
    jogar()