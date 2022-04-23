import random


def jogar():

    imprime_mensagem_inicial()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou E não acertou - Este é o Game Loop
    while(not enforcou and not acertou):

        chute = captura_chute()

        if(chute in palavra_secreta):
            valida_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        print(letras_acertadas)

        if("_" not in letras_acertadas):
            imprime_mensagem_ganhou()
            break
        elif(erros == 6):
            imprime_mensagem_perdeu()
            break
        else:
            continue

    print("Fim do jogo!")

# Funções

def imprime_mensagem_ganhou():
    print("Parabéns, você ganhou!")

def imprime_mensagem_perdeu():
    print("Não foi desta vez!")

def valida_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):  # aqui compartamos a entrada sempre como se fosse letra maíuscula
            # aqui guardamos as letras existentes na lista
            letras_acertadas[index] = letra
        index += 1

def captura_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_inicial():
    print("================================")
    print("===Bem-vindo ao Jogo da Forca===")
    print("================================")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()
