
lista = []

lista.append("1")
lista.append("2")
lista.append("3")
lista.append("4")
lista.append("5")
print(lista)
print(len(lista))

def encontrar():

    n = input("Insira o numero a ser deletado : ")
    if  n  in lista :
        lista.remove(n)
        print("numero deletado com sucesso")
    else :
        print("numero nao existe")
        return n

encontrar()
print(lista)
lista.insert(5,"6")
print(lista)