import os
from time import sleep
numero = 0
os.system("clear")
print("Caetano Mágico !")
print("================")
print("")
sleep(2)
print("Este aplicativo irá adivinhar seu pensamento.")
print("")
sleep(2)
print("Pense em um número de 0 a 15! Apenas pense!")
sleep(2)
print("")
x = input("Vamos continuar? (Aperte ENTER)")
os.system("clear")

# Verificação 1 **********************************************
print("1 - O número que você pensou está na lista abaixo?")
print("")
sleep(1)
print("1-3-5-7-9-11-13-15")
print
print ("[S] sim ou [N] não")
resposta = input()
resposta = resposta.upper()
if resposta == 'S':
    numero = numero + 1
sleep(1)
os.system("clear")

# Verificação 2 ********************************************
print("2 -  número que você pensou está na lista abaixo?")
print("")
sleep(1)
print("2-3-6-7-10-11-14-15")
print
print ("[S] sim ou [N] não")
resposta = input()
resposta = resposta.upper()
if resposta == 'S':
    numero = numero + 2
sleep(1)
os.system("clear")

# Verificação 3 ********************************************
print("3 - O número que você pensou está na lista abaixo?")
print("")
sleep(1)
print("4-5-6-7-12-13-14-15")
print
print ("[S] sim ou [N] não")
resposta = input()
resposta = resposta.upper()
if resposta == 'S':
    numero = numero + 4
sleep(1)
os.system("clear")

# Verificação 4 ********************************************
print("4 - O número que você pensou está na lista abaixo?")
print("")
sleep(1)
print("8-9-10-11-12-13-14-15")
print
print ("[S] sim ou [N] não")
resposta = input()
resposta = resposta.upper()
if resposta == 'S':
    numero = numero + 8
sleep(1)
os.system("clear")

print(" Hummmmmmm.............")
print("")
print("Agora vou adinhar o número que você pensou !")
print("")
print(" Hummmmmmm.............")
sleep(2)
os.system("clear")
print("VOCÊ PENSOU NO NÚMERO :")
sleep(1)
print(numero)
print("")
x = input("Sair! (Aperte ENTER)")