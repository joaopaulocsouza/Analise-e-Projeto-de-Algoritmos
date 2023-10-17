def search(A, n, z):
    print(n)
    if n == 0:
        if A[n] == z:
            return z
        else:
            return False
    else:
        if A[n] == z:
            return z
        else:
            return search(A, n-1,z)
        
vet = [0,1,2,3,4,5,6,7,8]

print(search(vet, len(vet)-1, 8))