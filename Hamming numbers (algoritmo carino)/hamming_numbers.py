def hamming(n: int) -> int:
    hamming = [1] * n  # Lista per i primi n numeri Hamming
    i2 = i3 = i5 = 0  # Contatori per l'esponente di 2, 3 e 5
    
    next_2, next_3, next_5 = 2, 3, 5  # Prossimo risultato se moltiplicassimo _x

    for i in range(1, n):
        
        hamming[i] = min(next_2, next_3, next_5)

        
        if hamming[i] == next_2:
            i2 += 1
            next_2 = hamming[i2] * 2
        if hamming[i] == next_3:
            i3 += 1
            next_3 = hamming[i3] * 3
        if hamming[i] == next_5:
            i5 += 1
            next_5 = hamming[i5] * 5

    return hamming[-1] 