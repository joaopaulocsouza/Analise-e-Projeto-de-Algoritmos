import math

def intercala(v, E, m, D):
    aux = v
    i = E
    j = m+1
    k = 0
    
    while i <= m and j <= D:
        if v[i] < v[j]:
            aux[k] = v[i]
            i += 1
        else:
            aux[k] = v[j]
            j += 1
        k += 1
    
    print(aux)


def merge(v, E, D):
    if E < D:
        m = math.floor((E+D)/2)
        merge(v, E, m)
        merge(v, m+1, D)
        intercala(v, E, m, D)
        
vec = [4,4,2,5,8,9,13,5,1,3,4]

merge(vec, 0, len(vec)-1)

print(vec)