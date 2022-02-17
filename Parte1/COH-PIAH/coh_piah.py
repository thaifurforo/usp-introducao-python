import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0
    indice = 0
    for i in as_a:
        similaridade += abs(i - as_b[indice])
        indice += 1

    similaridade = similaridade / 6
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    for i in sentencas:
        frases += separa_frases(i)
    for i in frases:
        palavras += separa_palavras(i)

    tamanho_total_palavras = 0
    for i in palavras:
        tamanho_total_palavras += len(i)

    tamanho_total_sentencas = 0
    for i in sentencas:
        tamanho_total_sentencas += len(i)

    tamanho_total_frases = 0
    for i in frases:
        tamanho_total_frases += len(i)

    n_palavras = len(palavras)
    n_sentencas = len(sentencas)
    n_frases = len(frases)
    palavras_diferentes = n_palavras_diferentes(palavras)
    palavras_unicas = n_palavras_unicas(palavras)

    wal = tamanho_total_palavras / n_palavras
    ttr = palavras_diferentes / n_palavras
    hlr = palavras_unicas / n_palavras
    sal = tamanho_total_sentencas / n_sentencas
    sac = n_frases / n_sentencas
    pal = tamanho_total_frases / n_frases

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_textos = []

    for i in textos:
        assinatura = calcula_assinatura(i)
        ass_textos.append(assinatura)

    grau_similaridade = []
    for i in ass_textos:
        grau_similaridade.append(compara_assinatura(ass_cp, i))

    maior_grau_similaridade = min(grau_similaridade)
    texto_infectado = grau_similaridade.index(maior_grau_similaridade) + 1

    print('O autor do texto', texto_infectado, 'está infectado com COH-PIAH')
    return texto_infectado


ass_cp = le_assinatura()
textos = le_textos()
avalia_textos(textos, ass_cp)
