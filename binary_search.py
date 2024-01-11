import math

def search(A, p, q, z):
    #Base 
    if p == q:
        if A[p] == z:
            return z
        else:
            return False
    else:
        m = math.floor((p+q)/2)
        if z <= A[m]:
            #T(n/2)
            return search(A, p, m, z)
        else:
            #T(n/2)
            return search(A,m+1,q,z)

vet = [1,2,3,4,5,6,7,8,9,10,11,30,31,32,45,46,47,48,49,50,70,91,92,93,94,95,96,97,98,99,100]

print(search(vet, 0, len(vet)-1, 50))