def minmax(x, n):
    if n == 0:
        return x[n], x[n]
    if n == 1:
        if x[n] > x[n-1]:
            return x[n-1], x[n]
        else:
            return x[n], x[n-1]
    
    if x[n] > x[n-1]:
        m, M = x[n-1], x[n]
    else:
        m, M = x[n], x[n-1]
        
    for j in range(n-2): 
        i = n-2 - j
        if i < 2:
            if x[i] > M:
                M = x[i]
            if x[i] < m:
                m = x[i]
        else:
            if x[i] > x[i-1]:
                if x[i] > M:
                    M = x[i]
                if x[i-1] < m:
                    m = x[i-1]
            if x[i] < x[i-1]:
                if x[i-1] > M:
                    M = x[i-1]
                if x[i] < m:
                    m = x[i]
    return m, M

vet = [2,1]

print(minmax(vet, len(vet)-1))