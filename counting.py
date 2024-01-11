import math

def counting(A, B, k):
    C = []
    for i in range(k+1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1] 
    print(C)
    for j in range(0,len(A)-1):
        i = len(A) - j-1
        B[C[A[i]]-1] = A[i]
        C[A[i]-1] = C[A[i]-1]-1

vet = [1,6,2,3,5,7,8,9,1,0]
B = vet

counting(vet, B, max(vet))

print(vet, B)
