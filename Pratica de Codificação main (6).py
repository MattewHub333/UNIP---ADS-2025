#Soma de dois numeros 
num = int(input('Escreva o primeiro numero'))
num2 = int(input('Escreva o segundo numero'))
soma = num + num2
print(f'O resultado é {soma}')

#Divisão de um numero e multiplicação
n = float(input('Escreva o primeiro valor'))
n2 = float(input('Escreva o segundo valor'))
n3 = float(input('Escreva o terceiro valor'))
r = n / n2 * n3

print(f'O resultado dessa conta {r} é')

#Velocidade média
import sys
    
def calculaVelocidadeMedia(distancia, tempo):
    return distancia / tempo
    
def main():
    d = float(input('Valor da distancia: '))
    t = float(input('Valor do tempo: '))
    velocidademedia = calculaVelocidadeMedia(d, t)
    print(f'A velocidade média {velocidademedia} é: ')
    
if __name__=="__main__":
    main()
    
#Saber se um numero e positivo, negativo ou igual a 0
n = int(input('Digite o primeiro valor'));

if n > 0:
    print('O valor e positivo')
if n < 0:
    print('O valor e negativo')
if n == 0:
    print('O valor é igual a zero')

