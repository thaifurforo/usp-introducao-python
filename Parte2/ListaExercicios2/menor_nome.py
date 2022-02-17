def len_string(string):
    return len(string.strip())
def menor_nome(lista_nomes):
    menor_nome_str = min(lista_nomes, key = len_string)
    #nome = menor_nome[0].upper() + menor_nome[1:]
    #nome = nome.strip()
    #for letra in nome:
    #    if nome.index(letra) == 0:
    #        continue
    #    letra_anterior = nome[nome.index(letra)-1]
    #    if letra_anterior == ' ':
    #        index = nome.index(letra)
    #        nome = nome[:index] + letra.upper() + nome[index+1:]
    #return nome
    menor_nome_str = menor_nome_str.strip().title()
    return menor_nome_str



