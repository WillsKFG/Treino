#exercício 1 = a soma de todos os números do array
import array

numeros1 = array.array('i', [1,2,3,4,5])
soma = 0

for i in numeros1:
    soma += i

print('\na soma de tudo dá',soma)


#exercicio 2 = qual é o maior e qual o menor

import array
numeros2 = array.array('i', [7, 2, 9, 4, 1, 6])

menor = numeros2[0]
maior = numeros2[0]

for i in numeros2:
    if menor > i:
        menor = i
    elif maior < i:
        maior = i

print ('\no maior é:',maior, ', e o menor é:',menor)


#exercício 3 = quantos são pares ou ímpares

import array
numeros3 = array.array('i', [7, 2, 9, 4, 1, 6, 8])
par = 0
impar = 0

for i in numeros3:
    if i%2 == 0:
        par += 1
    else:
        impar += 1
print(f"\npar: {par} | impar: {impar}")

#exercício 4 = a junção de tudo

import array
numeros4 = array.array('i', [3, 7, 2, 9, 4, 1, 6, 8])

soma1 = 0
maior1 = numeros4[0]
menor1 = numeros4[0]
par1 = 0
impar1 = 0

#soma
for i in numeros4:
    soma1 += i

#maiormenor
for i in numeros4:
    if maior1 < i:
        maior1 = i
    elif menor1 > i:
        menor1 = i

#parimpar
for i in numeros4:
    if i%2 == 0:
        par1 += 1
    else:
        impar1 += 1

print(f'\nSoma: {soma1}')
print(f'Maior: {maior1} | Menor: {menor1}')
print(f"Par: {par1} | Ímpar: {impar1}\n")