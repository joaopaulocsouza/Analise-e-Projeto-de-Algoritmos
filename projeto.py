def ordena(v,n): #n-1
    #Base
    if n == 0:
        return True
    
    max_index = n
    for j in range(0, n+1): #n-1
        i = n - j
        if v[i] > v[n]: # Θ(n) Ο(2n) Ω(1)
            max_index = i
    if max_index != n:
        v[max_index], v[n] = v[n], v[max_index]
    ordena(v,n-1)

vet = [9,1,2,5,7,3,2,4,1]

ordena(vet, len(vet)-1)
print(vet)