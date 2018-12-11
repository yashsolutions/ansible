#!/usr/bin/python

cache = {}

def fibonacci(n):
    global cache
    
    if n in cache.keys():
       return cache[n]
    if n <= 1:
       return n
    else:
       result = (fibonacci(n-1) + fibonacci(n-2))
       cache[n] = result
       return result

#1 1 2 3 5 8 13 21 ....
#1 2 3 4 5 6 7  8

print( fibonacci(100) )

#f(x) = f(x-1) + f(x-2)
