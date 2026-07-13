#Atividade da Semana 1 do Projeto Egrégora da Equipe de Redes Neurais. Parte A e B
#Esse arquivo contém a classe do neurônio. A inicialização cria um peso e um bias aleatórios. O cálculo
#de saída segue a fórmula: Saída = (Entradas*Pesos) + Bias. A função de ativação escolhida foi a degrau,
#sendo positiva e igual a 1 para valores iguais ou maiores que 0 e é 0 para valores negativos

import random

class Neuronio:
    def __init__(self, num_entradas):
        #Inicializa pesos e bias com valores aleatórios entre -1 e 1
        self.pesos = [random.uniform(-1.0, 1.0) for _ in range(num_entradas)]
        self.bias  = random.uniform(-1.0, 1.0)

    def ativacao_degrau(self, valor):
        #Retorna 1 se o valor for maior ou igual a 0 e 0 caso o contrário
        return 1 if valor >= 0 else 0
    
    def calcular_saida(self, entradas):
        #Saída = (entradas * pesos) + bias
        soma = self.bias

        for i in range(len(entradas)):
            soma += entradas[i]*self.pesos[i]
        
        return self.ativacao_degrau(soma)
