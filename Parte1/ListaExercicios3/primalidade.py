num = int(input('Digite um número inteiro: '))
if num <= 0:
    print('Erro')
else:

    primo = True
    i = 1
    while primo and i < num-1:
        if num % (num - i) == 0:
            primo = False
        i += 1

    if primo:
        print('primo')
    else:
        print('não primo')
