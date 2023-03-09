def recursion_fibo(n):
    return 1 if n<=2 else recursion_fibo(n-2) + recursion_fibo(n-1)