def primeNumbers(n):
    """returns a list of prime numbers"""
    primes = []
    if type(n)!=int:
        raise TypeError
    elif n <=1: 
        return primes
    else:
        for i in range(2,n+1):
            isprime=True
            for num in primes:
                if(i%num==0):
                    isprime=False
            if(isprime):
                primes.append(i)
        return primes