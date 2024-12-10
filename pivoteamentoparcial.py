def pivoteamento_parcial(A, b):
    n = len(A)
    multiplicadores = []  # Para armazenar os multiplicadores

    # Combinar a matriz A com o vetor b (matriz aumentada)
    for i in range(n):
        A[i].append(b[i])

    for k in range(n - 1):
        # Encontrar o índice do maior valor absoluto na coluna k
        max_i = max(range(k, n), key=lambda i: abs(A[i][k]))
        if max_i != k:
            # Trocar as linhas k e max_i
            A[k], A[max_i] = A[max_i], A[k]
            print(f"Trocando linha {k} com linha {max_i}")

        print(f"\nIteração {k + 1}: Pivô escolhido é A[{k}][{k}] = {A[k][k]}")
        print("Matriz após troca de linhas:")
        for row in A:
            print(row)

        # Eliminação para zerar elementos abaixo do pivô
        for i in range(k + 1, n):
            fator = A[i][k] / A[k][k]
            multiplicadores.append((i, k, fator))
            for j in range(k, n + 1):  # n+1 inclui a coluna do vetor b
                A[i][j] -= fator * A[k][j]

        print("Matriz após eliminação:")
        for row in A:
            print(row)

    print("\nMultiplicadores (m_ij):")
    for m in multiplicadores:
        print(f"m_{m[0] + 1}{m[1] + 1} = {m[2]}")

    # Substituição regressiva para encontrar a solução
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (A[i][n] - soma) / A[i][i]

    return x


# Exemplo de uso
A = [
    [2, 1, 1, 0],
    [4, 3, 3, 1],
    [8, 7, 9, 5],
    [6, 7, 9, 8]
]
b = [1, 2, 4, 5]

solucao = pivoteamento_parcial(A, b)
print("\nSolução do sistema:", solucao)
