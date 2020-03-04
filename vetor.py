
v = []
nome = []

def vetor(v) :

    for i in range (5) :
        v.append(input("Numeros" + str(i +1)))

def leia_nome(nome) :

    for i in range (10) :
        print("Escreva letras")
        nome.append(input("Letra : " + str(i + 1)))

    nome.reverse()
    print(nome)

vetor(v)
print(v)
leia_nome(nome)