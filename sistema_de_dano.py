print ("===== Derrote seu oponente =====")
hp_adversario = int(input ("Digite o hp do seu oponente: "))

while hp_adversario > 0:
    ataque = input ("Digite 'atacar' para causar dano no seu oponente: ")
    if ataque == "atacar" :
        dano = 10
        hp_adversario -= dano
        print (f"Você causou {dano} de dano. HP do oponente {hp_adversario}")
    else:
        break

if hp_adversario == 0:
    print ("===== Parabéns! Você derrotou seu oponente =====")
else:
    print ("===== Você não conseguiu, talvez na próxima ! =====")