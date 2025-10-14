import random
player1 =input("nome do jogador 1:")
player2 =input("nome do jogador 2:")
letra_aleatoria = random.choice("abcdefghijklmnopqrstuvwxyz")
print(f"A letra escolhida foi: {letra_aleatoria}")
print("O jogo cham-se Stop, na proxima linha vou explicar as regras")
print("vais ter que escrever uma palavra que comece com a letra escolhida e que se encaixe no tema dado, o primeiro a pensar na palavra mete o nome do player")
resposta = input("o tema é: nome")
if resposta == player1:
    palavra1 = input("escreve a tua palavra")
    if palavra1[0] == letra_aleatoria:
        print("palavra valida")
    else:
        print("palavra invalida")
elif resposta == player2:
    palavra2 = input("escreve a tua palavra")
    if palavra2[0] == letra_aleatoria:
        print("palavra valida")
    else:
        print("palavra invalida")
else:
    print("jogador invalido")
 

print("terminou o jogo")