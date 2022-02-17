def é_hipotenusa(n):
    éHipotenusa = True
    i = n
    j = 1
    while i >= 1 and n ** 2 != i ** 2 + j ** 2:
        i -= 1
        j = 1
        while i >= 1 and n ** 2 != i ** 2 + j ** 2 and j < n:
            j += 1
            éHipotenusa = False
        éHipotenusa = False
    if i >= 1 and (n ** 2) == (i ** 2) + (j ** 2) and j < n:
        éHipotenusa = True
    return éHipotenusa


def soma_hipotenusas(n):
    somaHipotenusas = 0
    while n >= 1:
        if é_hipotenusa(n):
            somaHipotenusas += n
        n -= 1
    return somaHipotenusas
