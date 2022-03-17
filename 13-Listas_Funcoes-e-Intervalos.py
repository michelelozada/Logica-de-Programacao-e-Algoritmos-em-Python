# 1 - Imprima na tela uma lista de números que vá de 0 a 20.
numeros = list(range(21))
print(numeros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 2 - Remova da lista o número 0.
numeros.remove(0)
print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 3 - Identifique o primeiro e último elemento da lista.
primeiro = print(numeros[0]) # primeiro elemnto -> 1
ultimo = print(numeros[-1]) # último elemento -> 20

# 4 - Retorne qual o número de elementos que a lista possui.
numero_elementos = print(len(numeros)) # número de elementos desta lista -> 20

# 5 - Consegue criar duas sublistas ao separar os números pares dos ímpares?
pares = print(numeros[1::2]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
impares = print(numeros[::2]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 6 - Imprima a lista original de números em ordem inversa.
inversao = print(numeros[::-1]) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 7 - Transforme os números de 1 a 10 da lista original em algarismos romanos. Os demais números devem permanecer inalterados.
numeros [:10] = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
print(numeros)
# numeros = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 8 - Retomando a lista original, insira o número subsequente esperado no final da lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros.append(21)
print(numeros)
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# 9 - Agora insira o intervalo dos 4 números subsequentes esperados no fim da lista.
numeros.extend([22,23,24,25])
print(numeros)
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# 10 - Escreva um algoritmo que responda se os números 16 e 32 estão presentes nesta lista.
teste = int(input('Qual número deseja verificar se está na lista? '))
if teste in numeros:
    print (f'O número {teste} está nesta lista.')
else:
    print(f'O número {teste} não está nesta lista.')

'''
> Qual número deseja verficar se está na lista? 16
    O número 16 está nesta lista.

> Qual número deseja verficar se está na lista? 32
    O número 32 não está nesta lista.
'''