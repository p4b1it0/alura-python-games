import random

def jogar():
    print("================================")
    print("===Bem-vindo ao Jogo da Forca===")
    print("================================")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    # palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]  # List Comprehension

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou E não acertou - Este é o Game Loop
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        # estamos tratando a variável para limpar espaços em branco
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):  # aqui compartamos a entrada sempre como se fosse letra maíuscula
                    # aqui guardamos as letras existentes na lista
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        print(letras_acertadas)

        if("_" not in letras_acertadas):
            print("Parabéns, você ganhou!")
            break
        elif(erros == 6):
            print("Não foi desta vez!")
        else:
            continue

    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar()
