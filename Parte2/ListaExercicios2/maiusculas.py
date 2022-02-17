# 65 a 90

def maiusculas(frase):
    letras_maiusculas = ''
    for letra in frase:
        if ord(letra) in range(65, 91):
            letras_maiusculas += letra
    return letras_maiusculas

