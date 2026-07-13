#É o ponto de entrada do programa (Parte C e D).Ele lê o arquivo de texto, instancia a rede,
#percorre os exemplos gerando classificações e exibe o erro total e erro médio no final

from rede import Rede

def ler_dataset(caminho_arquivo):
    #Parte C: Leitura do dataset sem bibliotecas externas
    dataset = []

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            #Lê todo o conteúdo e divide por espaços ou quebra de linhas
            conteudo = arquivo.read().strip().split()

            for item in conteudo:
                if item:
                    #Vê se o formato é o experado (,)
                    valores = item.split(',')

                    if len(valores) == 3:
                        x = float(valores[0])
                        y = float(valores[1])
                        tipo = int(valores[3])
                        dataset.append(([x,y], tipo))
    
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado")

    return dataset

def main():
    # Carrega os dados do arquivo DatSet.txt
    dados = ler_dataset('DatSet.txt')
    
    if not dados:
        print("Nenhum dado para processar. Verifique seu arquivo DatSet.txt.")
        return

    # Parte D: Inicializar a rede 
    rede_neural = Rede()
    
    erro_total = 0
    quantidade_exemplos = len(dados)

    print("--- Resultados da Inferência ---")
    
    # Percorrer todos os exemplos do dataset
    for entradas, resposta_correta in dados:
        # 1. Ler entradas 
        # 2 e 3. Executar a rede e gerar classificação
        classificacao = rede_neural.inferencia(entradas)
        
        # 4. Comparar com a resposta correta e calcular o erro (Parte E)
        erro = rede_neural.calcular_erro_quadratico(classificacao, resposta_correta)
        erro_total += erro
        
        print(f"Entrada: {entradas} | Previsto: {classificacao} | Real: {resposta_correta} | Erro: {erro}")

    # Exibição final das métricas de erro
    erro_medio = erro_total / quantidade_exemplos

    print("\n--- Métricas de Erro ---")
    print(f"Erro Total: {erro_total}")
    print(f"Erro Médio: {erro_medio:.4f}")

if __name__ == "__main__":
    main()

