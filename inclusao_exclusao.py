#Criei uma variavel que é vista pelo programa todo, varivel global
global lista
lista = []

#fiz um switch para escolher as opções desejadas
#dentro do switch fiz um loop com while criei uma situcção usando uma booleana onde sempre será verdadeiro, quebro o codigo com o break usado na opção 3

def meu_switch():

    validacao = True
    x = 1
    while validacao :
        z = int(input("Menu : "
                      "\n 0 : Cadastro de itens"
                      "\n 1 : Imprimir Lista "
                      "\n 2 : Editar ou apagar lista"
                      "\n 3 : Sair \n"))
        if z < x :
            cadastro()
        elif z == x :
            imprime_lista()
        elif z == 2 :
            editar_apagar()
        elif z ==  3:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

#Fiz novamente um loop com while, como nao existe um do/while no python fiz um usando o true, com isso sempre a varivel z vai ser executado
# criei um mini menu, caso queira criar uma nova lista
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

# Imprime a lista
def imprime_lista() :

    global lista

    print(lista)

#Edita e apaga usando o loop um do/while forçado
# Opção com um mini menu
# Fiz um if que procura a palavra se ela existe e remove ela
def editar_apagar() :

    global lista

    x = 1
    while(True) :
        z = int(input("\n 1 Editar Lista, \n 2 Apagar Lista  \n 3 Sair \n"))
        if z == x :
            chave = input("Entre com o produto a ser alterado :")
            if  len([x for x in lista if x == chave]) :
                lista.remove(chave)
                print("Produto deletado da lista " + chave)
                break
            else :
                print("Produto não encontrado")
        elif z == 2 :
            lista.clear()
            print(lista)
            break
        else :
            print(" Processo encerrado !")
            return

# Main para executar o programa, chama o switch
if __name__ == "__main__":
    print (meu_switch())
