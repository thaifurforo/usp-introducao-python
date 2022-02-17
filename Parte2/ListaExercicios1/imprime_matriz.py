def imprime_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    for l in range(num_linhas):
        for c in range(num_colunas):
            if c == num_colunas-1:
                print(matriz[l][c], end='\n')
            else:
                print(matriz[l][c], end=' ')

