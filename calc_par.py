def par(v, n):
    #BASE
    if n == 1:
        if v[0]%2 ==0:
            return True
        else:
            return False

    #Hipótese
    V = (v, n-1)

    #Passo

vet = [1,3,41,5,61,7,83]

print(par(vet, len(vet)))