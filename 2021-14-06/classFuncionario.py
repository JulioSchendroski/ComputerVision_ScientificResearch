class Funcionario:
    def __init__(self,nome,salario): #Método construtor, com dois parametros para as instâncias 
        self.nome = nome #instância nome
        self.salario = salario #instancia salário

    def mostraInfoFuncionario(self): #Método de mostras informações do funcionário específico
        print('O funcionário {} recebe atualmente RS${} reais '.format(self.nome,self.salario)) #formtador com self.

    def acrescimoSalario(self,porcento): #Método para acrescentar porcentagem definida por parametro para o salário
        self.salario = self.salario + (self.salario * (porcento / 100))

    def mudarSalario(self,novo):
        self.salario = novo

funcionario1 = Funcionario('Julio', 3500.00) #Atribuindo a Classe "Funcionários" para a variável Funcionário1 

funcionario1.mostraInfoFuncionario()
print(funcionario1.salario) #Mostra salário original
funcionario1.acrescimoSalario(15) #Acresce 15% do salário atual
print(funcionario1.salario) #Mostra salário atualizado
funcionario1.mostraInfoFuncionario() #Mostra todas informações novamente
funcionario1.mudarSalario(4026.00)
funcionario1.mostraInfoFuncionario()