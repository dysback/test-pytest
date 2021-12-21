

def fact(n: int) -> int:
    if n < 0:
        raise ValueError("Fact argument can't be nagative")

    if n > 0:
        return fact(n - 1) * n
    return 1

def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("Fibo argument can't be nagative")
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

