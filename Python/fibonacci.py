def Fibonacci(n,cache):
    # n : value
    if (n <= 2):
        return n
    
    if (cache.get(n) != None): # IF FIBONACCI IS NOT ON CACHE
        return cache[n]
    else:
        cache[n] = Fibonacci(n - 1,cache) + Fibonacci(n - 2,cache)
        return cache[n]

n = 10
i = 0
cache = {}
while (i < n):
    print(Fibonacci(n,cache))
    i += 1
