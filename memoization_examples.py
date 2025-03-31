# Fibonacci with recursion
from time import time
def fib_recusion(n):
    if n<=1:
        return n
    return fib_recusion(n-1) + fib_recusion(n-2)

def fib_memoization(n, computed={0: 0, 1:1}):
    if n not in computed:
        computed[n] = fib_memoization(n-1, computed) + fib_memoization(n-2,computed)
    return computed[n]

#print(fib_recusion(5))
#print(fib_recusion(10))
start_time = time()
fib_series = 100
print(fib_recusion(fib_series))
print(f"total time to calculate fibonacci({fib_series}) with recursion:{time.now() - start_time} ")

start_time = time()
print(fib_memoization(fib_series))
print(f"total time to calculate fibonacci({fib_series}) with memoization:{time.now() - start_time} ")