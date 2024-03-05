'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''

n1 = int(input('Digite um número'))
n2 = int(input('Digite mais um número'))


if n1 > n2:
    print(n1,' é maior')
else:
    print(n2,' é maior')