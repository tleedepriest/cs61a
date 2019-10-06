def is_prime(n):
    i = 2 
    if n == 0 or n == 1 or n == 2:
        return False
    else:
        while i < n:
            if n%i == 0:
                return False
            else:
                i = i + 1
        return True 
