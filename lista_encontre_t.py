#Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente.
# Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)

t = []

t.append("1")
t.append("2")
t.append("3")
t.append("4")
t.append("5")
t.append("5")
print(t)
#Opção para inserir o numero na posiçao 0
t.insert(0,"0")
print(t)

# Encontra o numero na lista
def encontre() :

    n = input("Insira o numero a ser encontrado : ")
    print(t.count(n))


encontre()