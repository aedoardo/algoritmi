def salario(arr): # complexity O(n)
    # ref https://www.geeksforgeeks.org/minimum-salary-hike-for-each-employee-such-that-no-employee-feels-unfair/
    sol = [1 for _ in range(0, len(arr))]
    
    sol[1] = 1
    for i in range(0, len(arr)):
        if i == 0:
            if arr[i] > arr[i+1]:
                sol[i] += 1
        
        elif i == len(arr) - 1:
            if arr[i] > arr[i-1]:
                sol[i] = sol[i-1] + 1
            else:
                sol[i] = sol[i-1] - 1
                
        else:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                sol[i] += 2
            elif arr[i] > arr[i+1] and arr[i] < arr[i-1]:
                sol[i] += 1
            elif arr[i] < arr[i+1] and arr[i] > arr[i-1]:
                sol[i] += 1
    return sol, sum(sol)

b = [1, 3, 5, 4] # expected output 1 2 3 2
print(salario(b))

def indice(arr, i, j):
    # ref: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf 2.17
    if i > j:
        return "None"
    
    if i == j and arr[i] == i:
        return arr[i], i
    
    if arr[i] == i:
        return arr[i]
    
    m = (i+j)//2
    
    if arr[m] == m:
        return arr[m], m
    
    if m > arr[m]:
        return indice(arr, i, m-1)
    
    return indice(arr, m+1, j)

# complexity: T(n) = T(n/2) + O(1) = O(logn)
    
c = [0]
print(indice(c, 0, len(c)-1))

def majority(arr, i, j):
    # majority element ref: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf 2.23
    if i > j:
        return None
    
    if i == j:
        return arr[i]
    
    m = (i+j)//2
    
    l = majority(arr, i, m-1) # elemento di sx
    r = majority(arr, m+1, j) # elemento di dx
    
    if l == r:
        return l
    
    lc = rc = 0
    for i in range(i, j+1):
        if arr[i] == l:
            lc += 1
        elif arr[i] == r:
            rc += 1
    
    if lc > rc:
        return l
    
    return r


d = [0,0,0,0,0,0,1,2,2,2,3,2,2,2,2,2,4,5,5,5,5,5,5,55,6666,6666,6666,6666,6666,6666,6666,6666,6666, 5, 5, 5,5,5,5,5]
print(majority(d, 0, len(d)-1))
    
    


