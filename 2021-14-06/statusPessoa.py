class Atributos: #Cria classe "Atributos"
    def __init__(self,nome,idade,altura,peso): #Método construtor de instâncias
        self.nome = nome #Define nome para um nova instância
        self.idade = idade  #Define idade para um nova instância
        self.altura = altura  #Define altura para um nova instância
        self.peso = peso  #Define peso para um nova instância

    def envelhecer(self): #Método para acrescentar 1 ano a cada chamada da idade
        if self.idade < 21: #Caso a idade do objeto "Pessoa" for menor que 21 anos, a cada chamada de envelhecer é adicionado 0.05 na altura
            self.altura += 0.05 
        self.idade+=1  #Acrescenta 1 ano a cada chamada do método
    def crescer(self, metros): #Acrescenta x metros no objeto altura
        self.altura += metros
    def emagrecer(self, kilos): #Acrescenta x kilos no objeto apeso
        self.peso -= kilos
    def engordar(self, kilos): #Diminui x kilos no objeto peso
        self.peso += kilos

pessoa1 = Atributos('Julio', 15, 1.8, 65.4) #Atribui o objeto à classe "Atributos"
pessoa1.envelhecer() #Chama método evelhecer sem parametros, já que só é possivel envelhecer de ano em ano
pessoa1.engordar(3) #Método de engordar, no exemplo em questão 3 kilos como parâmetro
pessoa1.crescer(0.01) #Método crescer e 0.01 centimetros
print('O nome da pessoa é {}, sua idade é de {} anos, altualmente mede {} metros de altura, e pesa {} klios'.format(pessoa1.nome, pessoa1.idade, pessoa1.altura, pessoa1.peso))