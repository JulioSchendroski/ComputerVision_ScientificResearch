#import sys
#sys.path.append('C:\\Codes\\Thiago')
from  crapsClasse import Dice #importa o arquivo "crapsClasse" e a classe "Dice"


jogador = Dice() #Cria-se a instância do objeto "Jogador"
print('\n*****CRAPS*****\n')

jogador.throw() #Chama o método "throw" para gear numero aleatório de 1 a 6 duas vezes (2,12)
print('A soma dos dados do jogador é : {}'.format(jogador.resultado)) #Mostra o resultado da soma dos dados com formatador
if jogador.resultado == 7 or jogador.resultado == 11: #condicional para o resultado obtido nos numeros dos dados
    print('Ganhou de primeira ')
elif jogador.resultado == 2 or jogador.resultado == 3 or jogador.resultado == 12: #Else para o resultado dos dados
    print('Craps ! ')

while True : #Laço para reptir lançamento dos dados
    input('Pressione qualquer tecla para continuar : \n') #input para o usuário pressionar qualquer tecla   
    jogador.throw() #Chama novamente método throw
    if jogador.resultado == 7: #condicional caso resultado for 7
        print('Tirou 7 antes do ponto :::: DICE !!!')
        break
    else : #Condicional em repetição até tirar o mesmo valor que foi gerado ao usar throw
        print('Ganhou!!')
        break
