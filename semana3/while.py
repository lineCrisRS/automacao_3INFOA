#Estrutura de condição - While
##Repete enquanto a condição for verdadeira
'''
#Sintaxe
while condicao:
   comando1
   comando2
   comandoN
'''
print("Exemplo 1: ==========")
i = 5
while i < 10:
    print(i)
    i = i + 1

print("Exemplo 2: ===========")


nomes = [] #cria uma lista vazia (sem nomes)
while True: #repete para sempre
    nome = input("Digite o nome: ")
    nomes.append(nome) #adiciona o nome na lista
    if nome == "fim": #se o nome for igual a fim
        print(nomes)
        break        #para o laço de repetição
