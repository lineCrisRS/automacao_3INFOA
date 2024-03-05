'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

i = 5
while i < 10:
    print(i)
    i = i + 1


matriculas = [] #cria uma lista vazia (sem matriculas)
while True: #repete para sempre
    matricula = int(input('Digite um número'))
    matriculas.append(matricula) #adiciona o matricula na lista
    if matricula == 0 : #se o matricula for igual a 0
        print(matriculas, 'feitas')
        break        #para o laço de repetição