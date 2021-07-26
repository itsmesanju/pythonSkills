def myPow(x, n):
        
        if x == 0:
            return 0
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n % 2 == 0:
            return myPow(x, n//2) ** 2
        else:
            return myPow(x, n//2) * myPow(x, (n//2) + 1)
            
