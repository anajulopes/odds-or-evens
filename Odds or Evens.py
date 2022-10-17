#Esse programa escolhe aleatóriamente um número de 1-100 e diz se ele é par ou ímpar.

#
#

import random #importa o módulo "random"

num = (range(1,100)) # Delimita o alcance em 100
count = 1 #A contagem de vezes começa em 1

while count <= 10: #vai repetir 10 vezes
    x = (random.choice(num)) # Escolhe aleatóriamente um número entre 1 e 100
    y = (x % 2) # calcula o resto do número aleatório dividido por 2

    if y == 0: #se o resto for 0 o número é par
        print(x , "é par") #mostra o resultado
        count += 1 #aumenta a contagem em 1
    else: #se o resto nao for 0 o número é impar
        print(x , "é ímpar") #mostra o resultado
        count += 1 #aumenta a contagem em 1
