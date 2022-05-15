from random import randint
#Jokenpô
modoDeJogo = 0
while modoDeJogo < 1 or modoDeJogo > 3:
    modoDeJogo = int(input("Escolha o modo de jogo: [1] Jogador x Jogador; [2] Jogador x Computador; [3] Computador x Computador. \n"))
    # Modo de jogo 1 = jogador x jogador
    if modoDeJogo == 1:
        print("Modo de jogo escolhido: Jogador x Jogador \n")
        continuarJogo = "s"
        partida = 0
        vitoriaP1 = 0
        vitoriaP2 = 0
        empate = 0

        pedra = 0
        papel = 0
        tesoura = 0

        totalJogadas = 0
        totalJogadasP1 = 0
        totalJogadasP2 = 0

        nomeP1 = str(input("JOGADOR 1 » Insira seu nome: \n"))
        nomeP2 = str(input("JOGADOR 2 » Insira seu nome: \n"))
        print("Olá,", nomeP1, "e", nomeP2, "! Bem-vindos ao Jokenpô! \n")

        while continuarJogo == "s":
            print(nomeP1, "» Escolha sua jogada: [1] Pedra; [2] Papel; [3] Tesoura")
            jogadaP1 = int(input())
            while jogadaP1 < 1 or jogadaP1 > 3:
                jogadaP1 = int(input("Por favor, escolha uma jogada válida \n"))
            print(nomeP2, "» Escolha sua jogada: [1] Pedra; [2] Papel; [3] Tesoura")
            jogadaP2 = int(input())
            while jogadaP2 < 1 or jogadaP2 > 3:
                jogadaP2 = int(input("Por favor, escolha uma jogada válida"))

            partida += 1
            print("Partida: ", partida)
            totalJogadasP1 += 1
            totalJogadasP2 += 1

            # Jogadas empate
            if jogadaP1 == 1 and jogadaP2 == 1:
                empate += 1
                pedra += 2
                print("Os dois escolheram PEDRA: empate")
            elif jogadaP1 == 2 and jogadaP2 == 2:
                empate += 1
                papel += 2
                print("Os dois escolheram PAPEL: empate")
            elif jogadaP1 == 3 and jogadaP2 == 3:
                empate += 1
                tesoura += 2
                print("Os dois escolheram TESOURA: empate")
            # Jogadas pedra
            elif jogadaP1 == 1 and jogadaP2 == 2:
                vitoriaP2 += 1
                pedra += 1
                papel += 1
                print(nomeP1, "escolheu Pedra x", nomeP2, "escolheu Papel:", nomeP2, "ganhou!")
            elif jogadaP1 == 1 and jogadaP2 == 3:
                vitoriaP1 += 1
                pedra += 1
                tesoura += 1
                print(nomeP1, "escolheu Pedra x", nomeP2, "escolheu Tesoura:", nomeP1, "ganhou!")
                # Jogadas papel
            elif jogadaP1 == 2 and jogadaP2 == 1:
                vitoriaP1 += 1
                papel += 1
                pedra += 1
                print(nomeP1, "escolheu Papel x", nomeP2, "escolheu Pedra:", nomeP1, "ganhou!")
            elif jogadaP1 == 2 and jogadaP2 == 3:
                papel += 1
                tesoura += 1
                vitoriaP2 += 1
                print(nomeP1, "escolheu Papel x", nomeP2, "escolheu Tesoura:", nomeP2, "ganhou!")
            # Jogadas tesoura
            elif jogadaP1 == 3 and jogadaP2 == 1:
                tesoura += 1
                pedra += 1
                vitoriaP2 += 1
                print(nomeP1, "escolheu Tesoura x", nomeP2, "escolheu Pedra:", nomeP2, "ganhou!")
            elif jogadaP1 == 3 and jogadaP2 == 2:
                tesoura += 1
                papel += 1
                vitoriaP1 += 1
                print(nomeP1, "escolheu Tesoura x", nomeP2, "escolheu Papel:", nomeP1, "ganhou!")

            print(nomeP1, "e", nomeP2, ", gostariam de continuar jogando? s - sim; n - não.")
            continuarJogo = str(input())
            while continuarJogo != "n" and continuarJogo != "s":
                print("Por favor, escolha uma opção válida.")
                continuarJogo = str(input())

            if continuarJogo == "n":
                print("Vocês decidiram terminar o jogo")
                print("\nResultados: \n")
                percentualP1 = (vitoriaP1 / partida) * 100
                percentualP2 = (vitoriaP2 / partida) * 100
                percentualEmpate = (empate / partida) * 100
                if percentualP1 > percentualP2:
                    print(nomeP1, " ganhou!")
                elif percentualP2 > percentualP1:
                    print(nomeP2, " ganhou!")
                elif percentualP1 == percentualP2:
                    print("Ninguém ganhou, foi empate!")
                totalJogadas = totalJogadasP1 + totalJogadasP2
                percentualPedra = (pedra / totalJogadas) * 100
                percentualPapel = (papel / totalJogadas) * 100
                percentualTesoura = (tesoura / totalJogadas) * 100
                print("\nNúmero de partidas: ", partida)
                print("Vitórias de", nomeP1, ":", percentualP1, "%")
                print("Vitórias de", nomeP2, ":", percentualP2, "%")
                print("Empates: ", percentualEmpate, "%")
                print("\nO percentual de jogadas mais usadas foram: ")
                print("Pedra: ", percentualPedra, "%")
                print("Papel: ", percentualPapel, "%")
                print("Tesoura: ", percentualTesoura, "%")
    # Modo de jogo 2 = jogador x computador
    if modoDeJogo == 2:
        print("Modo de jogo escolhido: Jogador x Computador")
        continuarJogo = "s"

        partida = 0
        vitoriaUsuario = 0
        vitoriaComputador = 0
        empate = 0

        pedra = 0
        papel = 0
        tesoura = 0

        totalJogadas = 0
        totalJogadasUsuario = 0
        totalJogadasComputador= 0

        while continuarJogo == "s":
            jogadaUsuario = int(input("Escolha sua jogada: [1] Pedra; [2] Papel; [3] Tesoura \n"))

            while jogadaUsuario < 1 or jogadaUsuario > 3:
                jogadaUsuario = int(input("Por favor, escolha uma jogada válida"))

            if jogadaUsuario == 1:
                print("Você escolheu: Pedra", "\n", "Agora é a vez do computador")
                pedra += 1
                totalJogadasUsuario +=1
            elif jogadaUsuario == 2:
                print("Você escolheu: Papel", "\n", "Agora é a vez do computador")
                papel += 1
                totalJogadasUsuario += 1
            elif jogadaUsuario == 3:
                print("Você escolheu: Tesoura", "\n", "Agora é a vez do computador")
                tesoura += 1
                totalJogadasUsuario += 1

            jogadaComputador = randint(1, 3)

            if jogadaComputador == 1:
                print("O computador escolheu: Pedra")
                pedra += 1
                totalJogadasComputador += 1
            elif jogadaComputador == 2:
                print("O computador escolheu: Papel")
                papel += 1
                totalJogadasComputador += 1
            elif jogadaComputador == 3:
                print("O computador escolheu: Tesoura")
                tesoura += 1
                totalJogadasComputador += 1

            if jogadaUsuario == jogadaComputador:
                empate += 1
                print("Empate")
            elif jogadaUsuario != jogadaComputador:
                #Jogadas com Pedra
                if jogadaUsuario == 1 and jogadaComputador == 2:
                    print("Pedra x Papel: o computador ganhou")
                    vitoriaComputador += 1
                elif jogadaUsuario == 1 and jogadaComputador == 3:
                    print("Pedra x Tesoura: você ganhou")
                    vitoriaUsuario += 1
                #Jogadas com Papel
                elif jogadaUsuario == 2 and jogadaComputador == 1:
                    print("Papel x Pedra: você ganhou")
                    vitoriaUsuario += 1
                elif jogadaUsuario == 2 and jogadaComputador == 3:
                    print("Papel x Tesoura: o computador ganhou")
                    vitoriaComputador += 1
                #Jogadas com Tesoura
                elif jogadaUsuario == 3 and jogadaComputador == 1:
                    print("Tesoura x Pedra: o computador ganhou")
                    vitoriaComputador += 1
                elif jogadaUsuario == 3 and jogadaComputador == 2:
                    print("Tesoura x Papel: você ganhou")
                    vitoriaUsuario += 1

            print("Gostaria de continuar jogando? s - sim; n - não")
            continuarJogo = str(input())
            while continuarJogo != "n" and continuarJogo != "s":
                print("Por favor, escolha uma opção válida.")
                continuarJogo = str(input())

            partida += 1

            if continuarJogo == "n":
                print("Você decidiu terminar o jogo")
                print("\nResultados: \n")
                percentualUsuario = (vitoriaUsuario / partida) * 100
                percentualComputador = (vitoriaComputador / partida) * 100
                percentualEmpate = (empate / partida) * 100
                if percentualUsuario > percentualComputador:
                    print("Parabéns, você ganhou!")
                elif percentualUsuario == percentualComputador:
                    print("Ninguém ganhou, foi empate!")
                elif percentualComputador > percentualUsuario:
                    print("Ops, parece que você não ganhou dessa vez :(")
                totalJogadas = totalJogadasUsuario + totalJogadasComputador
                percentualPedra = (pedra / totalJogadas) * 100
                percentualPapel = (papel / totalJogadas) * 100
                percentualTesoura = (tesoura / totalJogadas) * 100
                print("\nNúmero de partidas: ", partida)
                print("Vitórias do Usuário: ", percentualUsuario, "%")
                print("Vitórias do Computador: ", percentualComputador, "%")
                print("Empates: ", percentualEmpate, "%")
                print("\nO percentual de jogadas mais usadas foram: ")
                print("Pedra: ", percentualPedra, "%")
                print("Papel: ", percentualPapel, "%")
                print("Tesoura: ", percentualTesoura, "%")
    #Modo de jogo 3 = computador x computador
    if modoDeJogo == 3:
        print("Modo de jogo escolhido: Computador x Computador")

        continuarJogo = "s"
        vitoriaZelda = 0
        vitoriaPepe = 0
        empate = 0
        pedra = 0
        papel = 0
        tesoura = 0
        totalJogadas = 0
        totalJogadasZelda = 0
        totalJogadasPepe = 0
        print("Você escolheu assistir aos jogos de Jokenpô dos nossos computadores! \n"
              "Prepare-se para testemunhar toda inteligência da Zelda (Computador 1) e a sagacidade do Pepe (Computador 2)\n")
        #Computador 1 = Zelda
        #Computador 2 = Pepe
        escolhaUsuario = int(input("Defina o tipo de partida: [1] Uma por vez (você escolhe quando parar); "
              "[2] Melhor de 3; [3] Melhor de 5 com apostas; "
              "[4] Customizável (escolha quantos jogos que ver). \n"))
        #[1] Uma por vez
        if escolhaUsuario == 1:
            partida = 0

            print("Você escolheu: [1] Uma por vez.")
            while continuarJogo == "s":
                partida += 1
                print("Partida: ", partida)
                jogadaZelda = randint(1, 3)
                totalJogadasZelda += 1
                jogadaPepe = randint(1, 3)
                totalJogadasPepe +=1

                #Jogadas empate
                if jogadaZelda == 1 and jogadaPepe == 1:
                    empate += 1
                    pedra += 2
                    print("Os dois escolheram PEDRA: empate")
                elif jogadaZelda == 2 and jogadaPepe == 2:
                    empate += 1
                    papel += 2
                    print("Os dois escolheram PAPEL: empate")
                elif jogadaZelda == 3 and jogadaPepe == 3:
                    empate += 1
                    tesoura += 2
                    print("Os dois escolheram TESOURA: empate")
                #Jogadas pedra
                elif jogadaZelda == 1 and jogadaPepe == 2:
                    vitoriaPepe += 1
                    pedra += 1
                    papel += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Papel: Pepe ganhou!")
                elif jogadaZelda == 1 and jogadaPepe == 3:
                    vitoriaZelda += 1
                    pedra += 1
                    tesoura += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Tesoura: Zelda ganhou!")
                    #Jogadas papel
                elif jogadaZelda == 2 and jogadaPepe == 1:
                    vitoriaZelda += 1
                    papel += 1
                    pedra += 1
                    print("Zelda escolheu Papel x Pepe escolheu Pedra: Zelda ganhou!")
                elif jogadaZelda == 2 and jogadaPepe == 3:
                    papel += 1
                    tesoura += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Papel x Pepe escolheu Tesoura: Pepe ganhou!")
                #Jogadas tesoura
                elif jogadaZelda == 3 and jogadaPepe == 1:
                    tesoura += 1
                    pedra += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Pedra: Pepe ganhou!")
                elif jogadaZelda == 3 and jogadaPepe == 2:
                    tesoura += 1
                    papel += 1
                    vitoriaZelda += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Papel: Zelda ganhou!")

                print("Gostaria de continuar jogando? s - sim; n - não.")
                continuarJogo = str(input())
                while continuarJogo != "n" and continuarJogo != "s":
                    continuarJogo = str(input("Por favor, escolha uma opção válida.\n"))

                if continuarJogo == "n":
                    print("Você decidiu terminar o jogo")
                    percentualZelda = (vitoriaZelda / partida) * 100
                    percentualPepe = (vitoriaPepe / partida) * 100
                    percentualEmpate = (empate / partida) * 100
                    print("\nResultados: \n")
                    if percentualZelda > percentualPepe:
                        print("A Zelda ganhou!")
                    elif percentualPepe > percentualZelda:
                        print("O Pepe ganhou!")
                    elif percentualPepe == percentualZelda:
                        print("Ninguém ganhou, foi empate!")

                    totalJogadas = totalJogadasZelda + totalJogadasPepe

                    percentualPedra = (pedra / totalJogadas) * 100
                    percentualPapel = (papel / totalJogadas) * 100
                    percentualTesoura = (tesoura / totalJogadas) * 100
                    print("\nNúmero de partidas: ", partida)
                    print("Vitórias da Zelda (Computador 1): ", percentualZelda, "%")
                    print("Vitórias do Pepe (Computador 2): ", percentualPepe, "%")
                    print("Empates: ", percentualEmpate, "%")
                    print("\nO percentual de jogadas mais usadas foram: ")
                    print("Pedra: ", percentualPedra, "%")
                    print("Papel: ", percentualPapel, "%")
                    print("Tesoura: ", percentualTesoura, "%")
        #[2] Melhor de 3
        if escolhaUsuario == 2:
            print("Você escolheu: [2] Melhor de 3")
            melhor3 = 0
            partida = 0

            for melhor3 in range(3):
                partida += 1
                print("Partida:", partida)

                jogadaZelda = randint(1, 3)
                totalJogadasZelda += 1
                jogadaPepe = randint(1, 3)
                totalJogadasPepe += 1

                # Jogadas empate
                if jogadaZelda == 1 and jogadaPepe == 1:
                    empate += 1
                    pedra += 2
                    print("Os dois escolheram PEDRA: empate")
                elif jogadaZelda == 2 and jogadaPepe == 2:
                    empate += 1
                    papel += 2
                    print("Os dois escolheram PAPEL: empate")
                elif jogadaZelda == 3 and jogadaPepe == 3:
                    empate += 1
                    tesoura += 2
                    print("Os dois escolheram TESOURA: empate")
                # Jogadas pedra
                elif jogadaZelda == 1 and jogadaPepe == 2:
                    vitoriaPepe += 1
                    pedra += 1
                    papel += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Papel: Pepe ganhou!")
                elif jogadaZelda == 1 and jogadaPepe == 3:
                    vitoriaZelda += 1
                    pedra += 1
                    tesoura += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Tesoura: Zelda ganhou!")
                    # Jogadas papel
                elif jogadaZelda == 2 and jogadaPepe == 1:
                    vitoriaZelda += 1
                    papel += 1
                    pedra += 1
                    print("Zelda escolheu Papel x Pepe escolheu Pedra: Zelda ganhou!")
                elif jogadaZelda == 2 and jogadaPepe == 3:
                    papel += 1
                    tesoura += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Papel x Pepe escolheu Tesoura: Pepe ganhou!")
                # Jogadas tesoura
                elif jogadaZelda == 3 and jogadaPepe == 1:
                    tesoura += 1
                    pedra += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Pedra: Pepe ganhou!")
                elif jogadaZelda == 3 and jogadaPepe == 2:
                    tesoura += 1
                    papel += 1
                    vitoriaZelda += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Papel: Zelda ganhou!")

                melhor3 += 1
            print("\nResultados melhor de 3: \n")
            percentualZelda = (vitoriaZelda / partida) * 100
            percentualPepe = (vitoriaPepe / partida) * 100
            percentualEmpate = (empate / partida) * 100
            if percentualZelda > percentualPepe:
                print("A Zelda ganhou!")
            elif percentualPepe > percentualZelda:
                print("O Pepe ganhou!")
            elif percentualPepe == percentualZelda:
                print("Ninguém ganhou, foi empate!")

            totalJogadas = totalJogadasZelda + totalJogadasPepe
            percentualPedra = (pedra / totalJogadas) * 100
            percentualPapel = (papel / totalJogadas) * 100
            percentualTesoura = (tesoura / totalJogadas) * 100
            print("\nNúmero de partidas: ", partida)
            print("Vitórias da Zelda (Computador 1): ", percentualZelda, "%")
            print("Vitórias do Pepe (Computador 2): ", percentualPepe, "%")
            print("Empates: ", percentualEmpate, "%")
            print("\nO percentual de jogadas mais usadas foram: ")
            print("Pedra: ", percentualPedra, "%")
            print("Papel: ", percentualPapel, "%")
            print("Tesoura: ", percentualTesoura, "%")
            print("\nGostaria de jogar de novo? [0] Sair do jogo; [1] Resetar jogo.\n")
            gameOver = int(input())
            if gameOver == 0:
                print("Você decidiu sair do jogo.")
                break
            elif gameOver == 1:
                modoDeJogo = 0
            else:
                print("Escolha uma opção válida.")
        #[3] Melhor de 5 com apostas
        if escolhaUsuario == 3:
            print("Você escolheu: Melhor de 5 com apostas \n Como funciona? Neste modo, você escolhe um Computador para apostar na vitória (Zelda ou Pepe),"
                      " se o computador escolhido vencer na melhor de 5, você também vence!")
            melhor5 = 0
            partida = 0
            apostaUsuario = int(input("Escolha em qual computador quer apostar: [1] Zelda; [2] Pepe. \n"))

            while apostaUsuario < 1 or apostaUsuario > 2:
                apostaUsuario = int(input("Escolha uma opção válida. \n"))
            if apostaUsuario == 1:
                print("Você apostou na Zelda (Computador 1)! \n")
            elif apostaUsuario == 2:
                print("Você apostou no Pepe (Computador 2)! \n")

            for melhor5 in range(5):
                partida += 1
                print("Partida:", partida)

                jogadaZelda = randint(1, 3)
                totalJogadasZelda += 1
                jogadaPepe = randint(1, 3)
                totalJogadasPepe += 1

                # Jogadas empate
                if jogadaZelda == 1 and jogadaPepe == 1:
                    empate += 1
                    pedra += 2
                    print("Os dois escolheram PEDRA: empate")
                elif jogadaZelda == 2 and jogadaPepe == 2:
                    empate += 1
                    papel += 2
                    print("Os dois escolheram PAPEL: empate")
                elif jogadaZelda == 3 and jogadaPepe == 3:
                    empate += 1
                    tesoura += 2
                    print("Os dois escolheram TESOURA: empate")
                # Jogadas pedra
                elif jogadaZelda == 1 and jogadaPepe == 2:
                    vitoriaPepe += 1
                    pedra += 1
                    papel += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Papel: Pepe ganhou!")
                elif jogadaZelda == 1 and jogadaPepe == 3:
                    vitoriaZelda += 1
                    pedra += 1
                    tesoura += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Tesoura: Zelda ganhou!")
                    # Jogadas papel
                elif jogadaZelda == 2 and jogadaPepe == 1:
                    vitoriaZelda += 1
                    papel += 1
                    pedra += 1
                    print("Zelda escolheu Papel x Pepe escolheu Pedra: Zelda ganhou!")
                elif jogadaZelda == 2 and jogadaPepe == 3:
                    papel += 1
                    tesoura += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Papel x Pepe escolheu Tesoura: Pepe ganhou!")
                # Jogadas tesoura
                elif jogadaZelda == 3 and jogadaPepe == 1:
                    tesoura += 1
                    pedra += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Pedra: Pepe ganhou!")
                elif jogadaZelda == 3 and jogadaPepe == 2:
                    tesoura += 1
                    papel += 1
                    vitoriaZelda += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Papel: Zelda ganhou!")

                melhor5 += 1

            print("\n Resultados melhor de 5: ")
            percentualZelda = (vitoriaZelda / partida) * 100
            percentualPepe = (vitoriaPepe / partida) * 100
            percentualEmpate = (empate / partida) * 100
            if percentualZelda > percentualPepe:
                print("A Zelda ganhou!")
                if apostaUsuario == 1:
                    print("Parabéns! Você apostou no Computador vencedor!")
                else:
                    print("Ops, parece que você não ganhou dessa vez :(")
            elif percentualPepe > percentualZelda:
                print("O Pepe ganhou!")
                if apostaUsuario == 2:
                    print("Parabéns! Você apostou no Computador vencedor!")
                else:
                    print("Ops, parece que você não ganhou dessa vez :(")
            elif percentualPepe == percentualZelda:
                print("Infelizmente ninguém ganhou... Foi empate!")

            totalJogadas = totalJogadasZelda + totalJogadasPepe
            percentualPedra = (pedra / totalJogadas) * 100
            percentualPapel = (papel / totalJogadas) * 100
            percentualTesoura = (tesoura / totalJogadas) * 100
            print("\n Número de partidas: ", partida)
            print("Vitórias da Zelda (Computador 1): ", percentualZelda, "%")
            print("Vitórias do Pepe (Computador 2): ", percentualPepe, "%")
            print("Empates: ", percentualEmpate, "%")
            print("\nO percentual de jogadas mais usadas foram: ")
            print("Pedra: ", percentualPedra, "%")
            print("Papel: ", percentualPapel, "%")
            print("Tesoura: ", percentualTesoura, "% \n")

            gameOver = int(input("Gostaria de jogar de novo? [0] Sair do jogo; [1] Resetar jogo. \n"))
            if gameOver == 0:
                print("Você decidiu sair do jogo.")
                break
            elif gameOver == 1:
                modoDeJogo = 0
            else:
                print("Escolha uma opção válida.")
        #[4] Customizável
        if escolhaUsuario == 4:
            partida = 0
            quantidadePartidas = int(input("Escolha quantas partidas quer assistir: \n"))
            print("Você escolheu assistir: ", quantidadePartidas)

            for partida in range(quantidadePartidas):
                partida += 1
                print("Partida:", partida)

                jogadaZelda = randint(1, 3)
                totalJogadasZelda += 1
                jogadaPepe = randint(1, 3)
                totalJogadasPepe += 1

                # Jogadas empate
                if jogadaZelda == 1 and jogadaPepe == 1:
                    empate += 1
                    pedra += 2
                    print("Os dois escolheram PEDRA: empate")
                elif jogadaZelda == 2 and jogadaPepe == 2:
                    empate += 1
                    papel += 2
                    print("Os dois escolheram PAPEL: empate")
                elif jogadaZelda == 3 and jogadaPepe == 3:
                    empate += 1
                    tesoura += 2
                    print("Os dois escolheram TESOURA: empate")
                # Jogadas pedra
                elif jogadaZelda == 1 and jogadaPepe == 2:
                    vitoriaPepe += 1
                    pedra += 1
                    papel += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Papel: Pepe ganhou!")
                elif jogadaZelda == 1 and jogadaPepe == 3:
                    vitoriaZelda += 1
                    pedra += 1
                    tesoura += 1
                    print("Zelda escolheu Pedra x Pepe escolheu Tesoura: Zelda ganhou!")
                    # Jogadas papel
                elif jogadaZelda == 2 and jogadaPepe == 1:
                    vitoriaZelda += 1
                    papel += 1
                    pedra += 1
                    print("Zelda escolheu Papel x Pepe escolheu Pedra: Zelda ganhou!")
                elif jogadaZelda == 2 and jogadaPepe == 3:
                    papel += 1
                    tesoura += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Papel x Pepe escolheu Tesoura: Pepe ganhou!")
                # Jogadas tesoura
                elif jogadaZelda == 3 and jogadaPepe == 1:
                    tesoura += 1
                    pedra += 1
                    vitoriaPepe += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Pedra: Pepe ganhou!")
                elif jogadaZelda == 3 and jogadaPepe == 2:
                    tesoura += 1
                    papel += 1
                    vitoriaZelda += 1
                    print("Zelda escolheu Tesoura x Pepe escolheu Papel: Zelda ganhou!")
            percentualZelda = (vitoriaZelda / partida) * 100
            percentualPepe = (vitoriaPepe / partida) * 100
            percentualEmpate = (empate / partida) * 100
            totalJogadas = totalJogadasZelda + totalJogadasPepe
            percentualPedra = (pedra / totalJogadas) * 100
            percentualPapel = (papel / totalJogadas) * 100
            percentualTesoura = (tesoura / totalJogadas) * 100
            print("\nResultados: ")
            if percentualZelda > percentualPepe:
                print("\nA Zelda ganhou!")
            elif percentualPepe > percentualZelda:
                print("\nO Pepe ganhou!")
            elif percentualPepe == percentualZelda:
                print("\nNinguém ganhou, foi empate!")
            print("\nNúmero de partidas: ", partida)
            print("Vitórias da Zelda (Computador 1): ", vitoriaZelda, "-", percentualZelda, "%")
            print("Vitórias do Pepe (Computador 2): ", vitoriaPepe, "-", percentualPepe, "%")
            print("Empates: ", empate, "-", percentualEmpate, "%")
            print("\nO percentual de jogadas mais usadas foram: ")
            print("Pedra: ", percentualPedra, "%")
            print("Papel: ", percentualPapel, "%")
            print("Tesoura: ", percentualTesoura, "%")