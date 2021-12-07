class InfoCarros: #Determina a classe "InfoCarros"
    gas = 0 #Varial de escopo global
    def __init__(self,carros=[],consumo=[]): # Construtor que se inicia automaticamente para instâncias os objetos
        self.consumo = consumo # objeto "consumo", que recebe a instância "consumo" atrevés da função "self"
        self.carros = carros # objeto "carros", que recebe a instância "consumo" atrevés da função "self"
        self.combustivel = [0 for indice in consumo] # objeto que irá instância cada objeto "carro" e "consumo", utilizado de uma lista comprehension, usando um for para cada instância do consumo 

    def andar(self,quilometros): # Método para a ação "andar" usando como parâmetro a distância a ser percorrida
        for indice,quilometro  in enumerate(quilometros): # Utilizando uma repetição usando a função "enumerate" para indentificar cada objeto durante o looping, definindo mais de um carro
            self.combustivel[indice] -= quilometro / self.consumo[indice] # Por estar tratando com mais de uma instância ao mesmo tempo, utiliza-se o self
            print(f'O consumo de gasolina no carro foi de {self.carros[indice]} é {quilometro / self.consumo[indice]} litros') #Comando de output como modo diferente de formatar strings
            

    def obterGasolina(self): # Método "obterGasolina" para identificar a quantidade de gasolina de cada objeto declarado no Método "__init__"
        for indice,carro in enumerate(self.carros): # Novamente uma repetição com enumerate para mostrar com numeradores do index de cada elemento
            print(f'O combustivel atual do carro {carro} é : {self.combustivel[indice]} litros')

    def adicionaGasolina(self,gas): # Método de adicionar gasolina com a quantidade como parâmetro, definida como "gas" declarada globalmente
        for indice,quantidade in enumerate(gas):
            self.combustivel[indice] += quantidade # Faz a soma do combustivel de cada objeto com a quantidade definida pelo usuário

listaCar = InfoCarros(carros=['carro 1','carro 2','carro 3'],consumo=[30,40,50]) # Define todos objetos da classe "InfoCarros"
listaCar.adicionaGasolina(gas=[80,120,60]) # Chama-se o método "adicionaGasolina" com os parametros em formato de lista
listaCar.obterGasolina() # Comando de output chamando o método sem parâmetros
print('OS Carros passa a andar a partir desse ponto')
listaCar.andar([500,500,500]) # Passando como parâmetros a quantidade de quilômetros "500km"
listaCar.obterGasolina() # Novamente comando de output para mostrar a quantidade de combustivel pós os objetos percorrerem a distância declarada.

