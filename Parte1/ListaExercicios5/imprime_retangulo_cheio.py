l = int(input('digite a largura:'))
a = int(input('digite a altura:'))
while a > 0:
    largura = l
    while largura > 0:
        print('#', end='')
        largura -= 1
    print('')
    a -= 1
