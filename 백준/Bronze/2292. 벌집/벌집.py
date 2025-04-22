N=int(input())

if N==1:
    print(1)
else:
    n=2
    while True:
        lower_bound = 1+(3*(n-1)*(n-2))
        upper_bound = lower_bound + 6*(n-1)
        
        if lower_bound < N <= upper_bound:
            print(n)
            break
    
        n += 1