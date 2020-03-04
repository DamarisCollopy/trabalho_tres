
from itertools import chain
global nome
global altura
global lista
altua = []
nome = []

def meu_switch():

    validacao = True
    x = 1
    while validacao :
        z = int(input("Menu : "
                      "\n 0 : Cadastro Aluno"
                      "\n 1 : Lista "
                      "\n 2 : Media Altura"
                      "\n 3 : Sair \n"))
        if z < x :
            inserir_dados()
        elif z == x :
            imprima_lista()
        elif z == 2 :
            calculo_media()
        elif z ==  3:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")


def inserir_dados():

    global nome
    global altura
    global lista
    nome = []
    altura = []

    x = 1

    while True :
        z = int(input("Desejar inserir alunos, \n 1 Sim, \n 2 Não \n"))
        if z == x:
            nome.append(input("Entre com o nome do Aluno:"))
            altura.append(float(input("Entre com a altura:")))
            lista = [nome, altura]
        elif z != 1 and z != 2:
            print("Numero Inválido !!!")
            inserir_dados()
        else :
            return


def imprima_lista() :
    text = ''
    for n, a in zip(nome, altura):
        text += '\nO Nome do aluno {} e sua altura {}'.format(n, a)
    print(text)


def calculo_media():

    global altura
    maior = max(altura)
    menor = min(altura)
    media = sum(altura)/len(altura)

    print("Menor altura" + "" + str(menor))
    print("Maior :" + "" +str(maior))
    print("Media :" + "" +str(media))
    imprima_lista()


if __name__ == "__main__":
    print (meu_switch())


