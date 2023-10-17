

def selection(v, n):
    #Base
    if n == [0]:
        return 
    else:
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if v[j] < v[min_index]:
                    min_index = j
            v[i], v[min_index] = v[min_index], v[i]

vet = [9,1,4,2,90,8,4,3,19,23,12,13,14,15,16] 
selection(vet, len(vet))
print(vet) 
