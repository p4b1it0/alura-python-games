import adivinhacao
import forca

def escolhe_jogo():
    print("================================")
    print("===Bem-vindo ao menu de Jogos===")
    print("================================")

    print("(1) Forca (2) Adivinhação")
    escolher = int(input("Escollha seu jogo: "))

    if(escolher == 1):
        print("Vamos jogar a Forca!")
        forca.jogar()
    elif(escolher == 2):
        print("Vamos jogar Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()