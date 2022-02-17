def computador_escolhe_jogada(n, m):
    if n <= m:
        jogadaComputador = n
    else:
        jogadaComputador = m
        while jogadaComputador > 1 and (n - jogadaComputador) % (m+1) != 0 and jogadaComputador <= n and jogadaComputador <= m:
            jogadaComputador -= 1
    if jogadaComputador == 1:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou', jogadaComputador, 'peças.')
    return jogadaComputador


def usuario_escolhe_jogada(n, m):
    jogadaUsuario = int(input('Quantas peças você vai tirar?'))
    while jogadaUsuario < 1 or jogadaUsuario > n or jogadaUsuario > m:
        print('Oops! Jogada inválida! Tente de novo.')
        print('')
        jogadaUsuario = int(input('Quantas peças você vai tirar?'))
    n -= jogadaUsuario
    if jogadaUsuario == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou', jogadaUsuario, 'peças.')
    return jogadaUsuario


def partida():
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    while m > n or m <= 0 or n < 1:
        print('Oops! Parâmetros inválidos! Tente de novo.')
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))

    print('')
    if n % (m+1) != 0:
        print('Computador começa!')
        while n > 0:
            n -= computador_escolhe_jogada(n, m)
            print('Agora restam', n, 'peças no tabuleiro.')
            if n == 0:
                resultado = 'computadorVencedor'
            if n > 0:
                n -= usuario_escolhe_jogada(n, m)
                print('Agora restam', n, 'peças no tabuleiro.')
                if n == 0:
                    resultado = 'usuarioVencedor'
    else:
        print('Você começa!')
        while n > 0:
            n -= usuario_escolhe_jogada(n, m)
            print('Agora restam', n, 'peças no tabuleiro.')
            if n == 0:
                resultado = 'usuarioVencedor'
            if n > 0:
                n -= computador_escolhe_jogada(n, m)
                print('Agora restam', n, 'peças no tabuleiro.')
                if n == 0:
                    resultado = 'computadorVencedor'
    if resultado == 'usuarioVencedor':
        print('Fim do jogo! Você ganhou!')
        return 'usuarioVencedor'
    else:
        print('Fim de jogo! O computador ganhou!')
        return 'computadorVencedor'


def campeonato():
    vitoriasComputador = 0
    vitoriasUsuario = 0
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar uma partida campeonato')
    escolhaCampeonato = int(input())
    while escolhaCampeonato != 1 and escolhaCampeonato != 2:
        int(input('Oops! Escolha inválida! Tente de novo'))

    if escolhaCampeonato == 1:
        print('Você escolheu uma partida isolada!')
        print('')
        partida()
    else:
        print('Você escolheu um campeonato!')
        print('')
        print('**** Rodada 1 ****')
        if partida() == 'computadorVencedor':
            vitoriasComputador += 1
        else:
            vitoriasUsuario += 1
        print('')
        print('**** Rodada 2 ****')
        if partida() == 'computadorVencedor':
            vitoriasComputador += 1
        else:
            vitoriasUsuario += 1
        print('')
        print('**** Rodada 3 ****')
        if partida() == 'computadorVencedor':
            vitoriasComputador += 1
        else:
            vitoriasUsuario += 1
        print('*** Final do Campeonato ***')
        print('Placar: Você', vitoriasUsuario, 'x',
              vitoriasComputador, 'Computador')


campeonato()
