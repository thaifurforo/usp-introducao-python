from operator import attrgetter

class Carro:
    def __init__(self, modelo, posição_km):
        self.modelo = modelo
        self.posição_km = posição_km
        self.velocidade = 80
    def posição_final(self, tempo):
        self.posição_km += (self.velocidade * tempo)
        return self.posição_km

def main():
    posição_inicial_carro_pica = int(input('Digite a posição inicial (km) do carro pica: '))
    posição_inicial_celta_2012 = int(input('Digite a posição inicial (km) do celta 2012: '))
    tempo = int(input('Digite quanto tempo durou essa corrida (em horas): '))
    carro_pica = Carro('carro pica', posição_inicial_carro_pica)
    celta_2012 = Carro('celta 2012', posição_inicial_celta_2012)
    celta_2012.posição_final(tempo)
    carro_pica.posição_final(tempo)
    print('\n***********************\n')
    print('Lino, um {0} x {1}\nOs dois a {2} tu acha q vai ficar um do lado do outro?\n'
          '-------------------\n'
          'Gustavo, Sim filha da puta\n{2}km é {2}km arromado\n'
          '-------------------\n'
          'Lino, creio que nao'.format(carro_pica.modelo, celta_2012.modelo, carro_pica.velocidade))
    print('\n***********************\n')
    if carro_pica.posição_km == celta_2012.posição_km:
        print('Lino estava certo e os dois carros estão lado a lado no km {} da rodovia.'.format(carro_pica.posição_km))
    else:
        primeiro_lugar = max([carro_pica, celta_2012], key=attrgetter('posição_km'))
        if primeiro_lugar.modelo == 'carro pica':
            primeiro_lugar_posição_inicial = posição_inicial_carro_pica
        else:
            primeiro_lugar_posição_inicial = posição_inicial_celta_2012
        segundo_lugar = min([carro_pica, celta_2012], key=attrgetter('posição_km'))
        print('Gustavo estava certo, os dois carros não estão lado a lado.\n'
              'O {0} se deu bem por ter começado na frente, no km {1} da rodovia!\n'
              'Após {2} horas de corrida, o {0} chegou no km {3}, enquanto o {4} ainda estava no km {5}!\n'
              'Moral da história: nunca se esqueça de verificar o ponto inicial.'.format(primeiro_lugar.modelo, primeiro_lugar_posição_inicial, tempo, primeiro_lugar.posição_km, segundo_lugar.modelo, segundo_lugar.posição_km))


main()