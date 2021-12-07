import random as rd

def Craps():
    dice = rd.randint(2,12)
    print('\nO resultado da soma dos dados  é : {} '.format(dice))
    if dice == 7 or dice == 11:
        print('\nVoce ganhou de primeira ! ')
    elif dice == 2 or dice == 3 or dice == 12:
        print('\nCraps !')  
    else:
        return dice    

ponto = Craps()

print('\n*****CRAPS*****')


while(True):
    opc = input('\nDigite "throw" para jogar novamente os dados\n')
    if opc != 'throw':
        break
    ponto = Craps()
    if ponto == 7:
        print('\nVocê tirou 7 antes de seu ponto T_T')
        break
    else:
        print('\nO valor de seu ponto é : {} portanto você ganhou !!'.format(ponto))
        break