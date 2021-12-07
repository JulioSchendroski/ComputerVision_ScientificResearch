class infoCarro:
    combustivel = 0 #Inicializa o objeto "combustivel" como zero
    def __init__(self,consumo): #É um método construtor, é chamado automaticamente quando um objeto dessa classe é criado
        self.consumo = consumo #self. separa uma instancia para cada obejto da classe, como x cópias de consumo para cada objeto
    def andar(self,quilometro=[]): #método "andar" com uma instancia self. e a quilometragem a ser inserida
        consumo = (quilometro/self.consumo)
        self.combustivel -= consumo
        print("O carro anda uma distância de {} quilometros".format(quilometro))
    
    def obterGasolina(self): #método na qual a função é apenas mostrar o combustivel da variável
         return self.combustivel
        
    
    def adicionaGasolina(self,gas=[]): #método adicionar gasolina
        self.combustivel += gas

carro = infoCarro(20) #Atribui à carro um novo objeto da classe "InfoCarro", pasasndo 10 como parâmetro do construtor.
print("O carro passa a andar neste exato ponto.")
carro.adicionaGasolina(20) #método que adiciona combustivel 
print('O nivel atual de gasolina é {} litros'.format(carro.obterGasolina()))
carro.andar(40) #chama o método com um parametro de quilometragem (distância)
print('O nivel atual de gasolina é {} litros'.format(carro.obterGasolina()))

