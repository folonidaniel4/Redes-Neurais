#Este arquivo cria a rede utilizando o neurônio e implementa a métrica de erro (Erro Quadrático). Parte E
#A rede vai precisar de duas entradas, pois terão os pontos X e Y

from neuronio import Neuronio

class Rede:

    def __init__(self):
        #Inicializa a rede com um neurônio de duas entradas (coordenadas x e y)
        self.neuronio = Neuronio(num_entradas=2)
    
    def inferencia(self, entradas):
        #Executa a rede para uma dada entrada
        return self.neuronio.calcular_saida(entradas)
    
    def calcular_erro_quadratico(self, previsto, real):
        #Retorna o erro quadrático para uma única amostra (real - previsto)
        return (real - previsto) ** 2
