# importando uma bibliotaca

import random #aleátorio
numero_secreto = random.randint (1,100)

print ("===== Tentando acertar um número secreto entre (1,100) =====")
numero = int(input ("Digite um palpite: "))

# Sistema de loop até acerta o número correto 

while numero != numero_secreto:
    print ("===== Você não acertou o número, tente novamente =====")
    if numero < numero_secreto:
        print ("Dica: O número é maior !")
    else:
        print ("Dica: O número é menor !")
    numero = int(input ("Digite um palpite: "))

print (f"========== Parabéns! Você acertou o número secreto é {numero_secreto} ==========")