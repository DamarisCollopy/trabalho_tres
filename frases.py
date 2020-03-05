
#Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)

global text

def meu_switch():

    validacao = True
    x = 1
    while validacao :

        z = int(input("Menu : "
                      "\n 0 : Inserir texto"
                      "\n 1 : Procurar Indice "
                      "\n 2 : Sair \n"))
        if z < x :
            inserir_texto()
        elif z == x :
            procurar_texto()
        elif z ==  2:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

def inserir_texto() :

    global text
    sair = "sair"
# Inserir texto e validação obrigando digitar o texto
    while(True) :
        text = input("Escreva o seu texto : \n")
        if len(text) == 0 :
            print("Erro digite um texto!")
            continue
        elif text in sair :
            print("Fim do programa")
        else :
            return


def procurar_texto() :

    global text

    print(text.count(input("Devolve a posição da palavra")))
    print(text.find(input("Devolve se a palavra existe")))

    nome = input("Entre com a palavra a ser procurada :")

    if nome in text :
        print(nome)
    else :
        print("Palavra não encontrado")



if __name__ == "__main__":
    print (meu_switch())
