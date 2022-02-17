l = int(input('digite a largura:'))
a = int(input('digite a altura:'))
altura = a
while a > 0:
    if a == 1 or a == altura:
        largura = l
        while largura > 0:
            print('#', end='')
            largura -= 1
        print('')
    else:
        largura = l
        while largura > 0:
            if largura == 1 or largura == l:
                print('#', end='')
            else:
                print(' ', end='')
            largura -= 1
        print('')
    a -= 1
