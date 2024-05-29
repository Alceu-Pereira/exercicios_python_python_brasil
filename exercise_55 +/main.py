def verifica_quadrado_magico(quadrado):
    # Verifica se a soma das linhas, colunas e diagonais é a mesma
    total = sum(quadrado[:3])
    for i in range(3):
        if sum(quadrado[i::3]) != total:  # Soma das colunas
            return False
        if sum(quadrado[i*3:(i+1)*3]) != total:  # Soma das linhas
            return False
    if quadrado[0] + quadrado[4] + quadrado[8] != total:  # Soma da diagonal principal
        return False
    if quadrado[2] + quadrado[4] + quadrado[6] != total:  # Soma da diagonal secundária
        return False
    return True

def gera_quadrados_magicos():
    quadrados_magicos = []
    numeros = list(range(1, 10))
    
    def backtrack(quadrado):
        if len(quadrado) == 9:
            if verifica_quadrado_magico(quadrado):
                quadrados_magicos.append(quadrado[:])  # Adiciona uma cópia do quadrado mágico encontrado
            return
        for num in numeros:
            if num not in quadrado:
                quadrado.append(num)
                backtrack(quadrado)
                quadrado.pop()  # Remove o último número para tentar outras combinações
    
    backtrack([])
    return quadrados_magicos

# Mostra todos os quadrados mágicos encontrados
for quadrado in gera_quadrados_magicos():
    print(quadrado[:3])
    print(quadrado[3:6])
    print(quadrado[6:])
    print()
