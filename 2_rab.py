x={2,3,4,1,2,4,5}
def Repeat(x): 
    l = len(x) 
    repeated = [] 
    for i in range(l): 
        k = i + 1
        for j in range(k, l): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated
 
