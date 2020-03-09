
global lista
lista = []


def meu_switch():

    validacao = True
    x = 1
    while validacao :
        z = int(input("Menu : "
                      "\n 0 : Cadastro de itens"
                      "\n 1 : Imprimir Lista "
                      "\n 3 : Editar lista"
                      "\n 4 : Apagar lista"
                      "\n 5 : Sair \n"))
        if z < x :
            cadastro()
        elif z == x :
            imprime_lista()
        elif z == 3 :
            editar()
        elif z == 4 :
            apagar()
        elif z ==  5:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

def cadastro() :

    global lista
    lista = []

    x = 1
    lista.append(input("Entre com uma nova lista"))

    while(True) :
        z = int(input("Desejar inserir mais uma lista de produtos, \n 1 Sim, \n 2 Não \n"))
        if z == x :
            lista.append(input("Entre com uma nova lista"))
        elif z != 1 and z != 2:
            print("Entre com numeros validos!")
            cadastro()
        else :
            return

def imprime_lista() :

    global lista

    print("Lista  :" + str(lista))

def editar() :



    chave = input("Entre com o produto a ser deletado :")
    if chave in lista:
        print("Produto deletado da lista " + chave)
        lista.remove(chave)
    else:
        print("Produto não encontrado")

def apagar() :

    global lista

    lista.clear()
    print("Lista  :" + str(lista))




if __name__ == "__main__":
    print (meu_switch())
