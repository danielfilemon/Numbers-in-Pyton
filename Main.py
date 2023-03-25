import random

# gerar um número aleatório entre 1 e 10
number = random.randint(1, 100)

# pedir ao jogador para adivinhar o número
guess = int(input("Adivinhe um número entre 1 e 100: "))

# verificar se o jogador acertou
if guess == number:
    print("Parabéns, você acertou!")
else:
    print("Ops, você errou. O número era", number)
