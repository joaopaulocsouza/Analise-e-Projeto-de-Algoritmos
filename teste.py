def f(v,n):
    #Base
    if(n == 0):
        if v[n]%2 == 0: 
            return True
        else:
            return False
    
    #Hipotese
    return (v, n-1)

    return V

vet = [1,3,5,7,9]
print(f(vet, len(vet)-1))