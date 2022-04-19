def jogar():
    print("================================")
    print("===Bem-vindo ao Jogo da Forca===")
    print("================================")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou E não acertou - Este é o Game Loop
    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() # estamos tratando a variável para limpar espaços em branco

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): # aqui compartamos a entrada sempre como se fosse letra maíuscula
                    letras_acertadas[index] = letra # aqui guardamos as letras existentes na lista
                index += 1
        else:
            erros += 1
        
        print(letras_acertadas)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        if(acertou):
            print("Parabéns, você ganhou!")
        else:
            print("Não foi desta vez!")

    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar()