# Fibonacci with recursion
from time import time
def fib_recusion(n):
    if n<=1:
        return n
    return fib_recusion(n-1) + fib_recusion(n-2)

#Fibonacci with memoization

def fib_memoization(n, computed={0: 0, 1:1}):
    if n not in computed:
        computed[n] = fib_memoization(n-1, computed) + fib_memoization(n-2,computed)
    return computed[n]


#Array sum with recursion
def arraySum(arr, index=0):
    if len(arr) ==0:
        return 0
    return arr[index] + arraySum(arr, index + 1)

#Factorial in recursion
def factorial_recursion(n):
    if n <0:
        return None
    if n <= 1:
        return 1
    return n*factorial_recursion(n-1)

# Factorial with memoization

def factorial_memoization(n, computed = {0:1, 1:1}):
    if n in computed:
        return computed[n]
    else:
        computed[n] = factorial_memoization(n-1, computed) * n


#print(fib_recusion(5))
#print(fib_recusion(10))
start_time = time()
fib_series = 25
# print(fib_recusion(fib_series))
# print(f"total time to calculate fibonacci({fib_series}) with recursion:{time() - start_time} ")

# start_time = time()
# print(fib_memoization(fib_series))
# print(f"total time to calculate fibonacci({fib_series}) with memoization:{time() - start_time} ")


print(factorial_recursion(fib_series))
print(f"total time to calculate factorial_recursion({fib_series}) with recursion:{time() - start_time} ")
start_time = time()
print(factorial_memoization(fib_series))
print(f"total time to calculate factorial_memoization({fib_series}) with memoization:{time() - start_time} ")