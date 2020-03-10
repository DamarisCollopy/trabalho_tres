import random
ocorrencia = []
MAX = 100

for i in range(MAX) :
    ocorrencia.append(0)

for i in range(100) :
    resultado = random.randint(1,MAX)
    ocorrencia[resultado-1] += 1

print(ocorrencia)
print(sum(ocorrencia))