from site import check_enableusersite
import random

def jogar():
    print("================================")
    print("Bem-vindo ao Jogo de Adivinhação")
    print("================================")

    # Criar as variáveis do jogo
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    placar = 1000

    # Validar dificuldade
    print("Escolha a dificuldade do jogo")
    print("[1] fácil [2] médio [3] difícil")
    dificuldade = int(input("Digite a dificuldade:  "))

    if(dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 5

    # Criar o laço de repetição do jogo
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}.".format(rodada, tentativas))
        print("Você deve chutar números entre 1 e 100.")
        chute = int(input("Digite o seu número:  "))

        if(chute > 100 or chute <= 0):
            print("Você escolheu um número inválido.")
            continue

        if(chute == numero_secreto):
            print("Parabéns, você acertou e fez {} pontos!".format(placar))
            break
        else:
            if (chute > numero_secreto):
                print("Tente um número MENOR.")
            elif(chute < numero_secreto):
                print("Tente um número MAIOR.")
        diferenca = abs(numero_secreto - chute)
        placar = placar - diferenca

        if(rodada == tentativas):
            print("O jogo acabou e você perdeu!")


if(__name__ == "__main__"):
    jogar()
