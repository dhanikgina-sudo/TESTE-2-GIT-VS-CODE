import random
import pycountry
import threading
paises = [country.name.lower() for country in pycountry.countries]
# Nenhum print aqui — a lista é criada, mas não mostrada
print("Bem vindo ao jogo do Stop")
players = int(input("Quantos jogadores vão jogar?: "))
nomes_jogadores = []
for i in range(players):
    nome = input(f"Digite o nome do jogador {i + 1}: ")
    nomes_jogadores.append(nome)
print("Os jogadores são:", nomes_jogadores)
letra_aleatoria = random.choice("abcdefghijklmnopqrstuvwxyz")
print(f"A letra escolhida foi: {letra_aleatoria}")
print("As regras para jogar sao simples, o jogador que pensar primeiro numa palavra correta, terá de escrever o seu nome e de seguida clica enter e terá um tempo de 15 segundos para o escrever, cada resposta correta ganha se pontos")
print("Observação: As respostas têm de estar em minúsculas e sem acentos. E são em inglês")
tempo_acabou = False
def tempo_esgotado(nome):
    global tempo_acabou
    print(f"\n⏰ Tempo esgotado para {nome}!")
    tempo_acabou = True
while True:
    tempo_acabou = False
    resposta1 = input(f" Introduza o seu nome se sabe um país que comece com a letra {letra_aleatoria}: ")
    if resposta1 in nomes_jogadores:
        # Inicia temporizador de 15 segundos
        timer = threading.Timer(15, tempo_esgotado, [resposta1])
        timer.start()

        resposta_final = input(f"{resposta1}, escreva um país que comece com a letra {letra_aleatoria}: ")

        timer.cancel()  # cancela o temporizador se respondeu a tempo
        if tempo_acabou:
            continue  # volta ao início do loop se o tempo esgotou
        
        if resposta_final in paises and resposta_final.startswith(letra_aleatoria):
            print(f"✅ Correto! {resposta1} ganhou 10 pontos.")
            break  # Sai do loop após uma resposta correta
        else:
            print(f"❌ Errado! '{resposta_final}' não é um país válido ou não começa com '{letra_aleatoria}'.")
    else:
        print("❌ Esse nome não está entre os jogadores!")
        continue
    