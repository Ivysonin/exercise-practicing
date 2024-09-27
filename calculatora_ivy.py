print ("============ CALCULATORA ============")

# Colocando variaveis de escolha !

adicao = 1
subtracao = 2
multiplicacao = 3
divisao = 4
operacao = int(input ("Escolha um operador: (1 para adição; 2 para subtração; 3 para multiplicação; 4 para divisão): "))

# Executando o que eu escolhi !

# SOMANDO 
if operacao == adicao :
    print ("===== SOMANDO =====")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    print (f"A soma de {num1} + {num2} = {num1 + num2}")
    input ("==============================")

# SUBTRAINDO
elif operacao == subtracao:
    print ("===== SUBTRAINDO =====")
    num3 = int(input ("Digite um número: "))
    num4 = int(input ("Digite outro número: "))
    print (f"A subtração de {num3} - {num4} = {num3 - num4}")
    input ("==============================")

# MULTIPLICANDO
elif operacao == multiplicacao:
    print ("===== MULTIPLICAÇÃO =====")
    num5 = int(input ("Digite um número: "))
    num6 = int(input ("Digite outro número: "))
    print (f"A multiplicação de {num5} x {num6} = {num5 * num6}")
    input ("==============================")

# DIVIDINDO
elif operacao == divisao:
    print ("===== DIVISÃO =====")
    num7 = float(input ("Digite um número: "))
    num8 = float(input ("Digite outro número: "))
    print (f"A divisão de {num7:.0f} / {num8:.0f} = {num7 / num8:.1f}")
    input ("==============================")

# NÃO SEGUIU INSTRUÇÕES
else:
    print ("===== Você não está seguindo as instruções =====")
    input ("==============================")