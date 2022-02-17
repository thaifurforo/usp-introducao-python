def conta_letras(frase,contar='vogais'):
    lista_vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    soma = 0
    if contar == 'vogais':
        for letra in frase:
            if letra in lista_vogais:
                soma += 1
    if contar == 'consoantes':
        for letra in frase:
            if letra not in lista_vogais and letra != ' ':
                soma += 1
    return soma


