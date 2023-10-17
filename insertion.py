import math

def swap(X1, X2):
    aux = X2
    X2 = X1
    X1 = aux
    print(X1, X2)

def insertion(X, I, F):
    if F-I == 1:
        if X[F] < X[I]:
            swap(X[F], X[I])
    else:
        insertion(X, I, F-1)
        while X[F] < X[F-1] and F >= 0:
            swap(X[F], X[F-1])
            F = F-1

vet = [9,12,4,5,71,2,4,5,78]
insertion(vet, 0, len(vet) - 1)
print(vet)