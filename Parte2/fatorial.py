def fatorial(n):
    if n < 0:
        fatorial = 0
    else:
        fatorial = 1
        i = 2
        while i <= n:
            fatorial *= i
            i += 1
    return fatorial
