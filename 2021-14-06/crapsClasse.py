import random as rd #importa bilbioteca random e define como rd
class Dice: #cria Classe "dice"
    def __init__(self): #Usa método construtor para criar uma variável "resultado"
        self.resultado = 0
        
    def throw(self): #Método para lançar o dado
        self.dice = rd.randint(2,12) #Gera numeor aleatório inteiro de 2 a 12 
        self.resultado  += self.dice #Soma o resulaod com os dado
        return self.resultado #Retorna resultado
