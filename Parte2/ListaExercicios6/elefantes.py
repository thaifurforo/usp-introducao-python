def elefantes(n):
    if n <= 1:
        return ''
    elif n == 2:
        return elefantes(n-1) +\
               'Um elefante incomoda muita gente\n' +\
               '{} elefantes {}muito mais\n'.format(n, incomodam(n))
    else:
        return elefantes(n - 1) +\
               '{} elefantes incomodam muita gente\n'.format(n-1) +\
               '{} elefantes {}muito mais\n'.format(n, incomodam(n))

def incomodam(n):
    return n * 'incomodam '

