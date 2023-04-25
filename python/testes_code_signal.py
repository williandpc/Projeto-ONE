def solution(sequence):
    contador = 0
    menor = min(sequence)
    for indice, numero in enumerate(sequence):
        if contador > 1:
            break
        if indice == 0:
            if numero >= sequence[indice + 1]:
                contador += 1
                del sequence[indice]     
        if indice < len(sequence) - 1 and indice != 0:
            while sequence[indice - 1] >= numero <= sequence[indice + 1]:
                contador += 1
                del sequence[indice]
                if indice == 0 or not indice <= len(sequence) - 2 or contador > 1:
                    break
            while sequence[indice - 1] == numero:
                contador += 1
                del sequence[indice]
                if indice == 0 or indice < len(sequence) - 2 or contador > 1:
                    break
        if indice == len(sequence) - 1 and sequence[indice - 1] >= numero:
            contador += 1
            del sequence[indice]   
    solucao = True
    if contador > 1:
        solucao = False
    return solucao, sequence, contador

print(solution([1, 3, 2, 1]))