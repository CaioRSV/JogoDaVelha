import random
import time
import os
clear=lambda: os.system('cls')
while True:
    cabouGame=0
    print('Começando novo jogo...')
    def check(simbol):
        simbol=simbol.upper()
        checkmate=0
        if quadro[0]+quadro[3]+quadro[6]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[1]+quadro[4]+quadro[7]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[2]+quadro[5]+quadro[8]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[0]+quadro[1]+quadro[2]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[3]+quadro[4]+quadro[5]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[6]+quadro[4]+quadro[2]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[6]+quadro[4]+quadro[2]==simbol+simbol+simbol:
            checkmate+=2
        if quadro[0]+quadro[4]+quadro[8]==simbol+simbol+simbol:
            checkmate+=2
        if checkmate>0:
            return 1
        if '-' not in quadro and checkmate==0:
            return 2
    player=[]
    bot=[]
    cabochose=0
    while cabochose<1:
        chose=input('X ou O?')
        if chose.upper()=='X':
            player.append('X')
            bot.append('O')
            cabochose+=1
        if chose.upper()=='O':
            player.append('O')
            bot.append('X')
            cabochose+=1
        else:
            print('Digite apenas X ou O.')
            print('-')
    quadro=['-','-','-',
            '-','-','-',
            '-','-','-']
    def printquadro():
        print(quadro[0:3])
        print(quadro[3:6])
        print(quadro[6:9])
    def jogarp(simbolplayer):
        printquadro()
        while True:
            jogada=input('Onde quer jogar? (ABC=Colunas/123=Linhas): ')
            trad1=['A1','B1','C1','A2','B2','C2','A3','B3','C3']
            trad2=[0,1,2,3,4,5,6,7,8]
            jogadaINDEX=trad2[trad1.index(jogada.upper())]
            if quadro[jogadaINDEX]=='-':
                quadro[jogadaINDEX]=str(simbolplayer)
                break
            if quadro[jogadaINDEX]!='-':
                print('Jogada inválida, escolha outra posição.')
        printquadro()
        input('-')
        clear()    
    def jogarb(simbolbot):
        contadorDisponiveis= [i for i, x in enumerate(quadro) if x == '-'] #Lista todas disponíveis
        contadorBot= [i for i, x in enumerate(quadro) if x == str(simbolbot)] #Lista todos do BOT
        conjunto=contadorDisponiveis+contadorBot
        doBot=''
        Disponiveis=''
        for i in contadorDisponiveis: #Adiciona nos dois str
            Disponiveis+=str(i)
        for i in contadorBot:
            doBot+=str(i)
        if contadorBot==[]:
            randomics=random.randint(0,len(contadorDisponiveis)-1)
            randomicado=contadorDisponiveis[randomics]
            quadro[randomicado]=simbolbot ################################################FAZER JOGAAAAAAAAAAAAAAADAAAAAAAAA
        if contadorBot!=[]:
            win_pos=['036','147','258','012','345','678','642','048'] #Possiveis wins
            win_REAL={} #Wins Jogáveis
            a=doBot
            dic1={} #Dicionario pra armazenar coisas
            for i in a: #NESSE BLOCO SE CONTA SIMILARIDADES ENTRE JA JOGADAS E WINS
                for x in win_pos:
                    if x.count(i)>0 and str(x) not in dic1:
                        dic1[str(x)]=1
                    if x.count(i)>0 and str(x) in dic1:
                        dic1[str(x)]+=1
            for i in dic1:
                contador=0
                for x in i:
                    if int(x) in conjunto:
                        contador+=1
                if contador>=3:
                    win_REAL[i]=dic1[i]
            if win_REAL=={}:
                randomics2=random.randint(0,len(contadorDisponiveis)-1)
                randomicado2=contadorDisponiveis[randomics2]
                quadro[randomicado2]=simbolbot
            if win_REAL!={}:
                ehojogas=max(win_REAL, key=win_REAL.get)
                vojoga=''
                jajoguei=0
                for i in ehojogas:
                    if quadro[int(i)]=='-' and jajoguei==0:
                        quadro[int(i)]=simbolbot
                        jajoguei+=1
        print('Jogada do adversário:')
        printquadro()
        input('-')
        clear()
    def endgamecheck():
        if check(player[0])==1:
            input('Você foi o ganhador!')
            return 'deez'
        if check(bot[0])==1:
            input('Você perdeu!')
            return 'deez'
        if check(player[0])==2 or check(bot[0])==2:
            input('Empate!')
            return 'deez'
    def jogaPrimeiro():
        cabouGame=0
        while cabouGame<1:
            jogarp(player[0])
            check(player[0])
            check(bot[0])
            endgamecheck()#
            if endgamecheck()=='deez':
                cabouGame+=5
            if cabouGame<1:
                jogarb(bot[0])
                check(bot[0])
                check(player[0])
                endgamecheck()#
                if endgamecheck()=='deez':
                    cabouGame+=5
    def jogaSegundo():
        cabouGame=0
        while cabouGame<1:
            jogarb(bot[0])
            check(bot[0])
            check(player[0])
            endgamecheck()#
            if endgamecheck()=='deez':
                cabouGame+=5
            if cabouGame<1:
                jogarp(player[0])
                check(player[0])
                check(bot[0])
                endgamecheck()#
                if endgamecheck()=='deez':
                    cabouGame+=5
    vezrandom=random.randint(1,2)
    if vezrandom==1:
        input('Você vai jogar primeiro.')
        player.append(1)
        bot.append(2)
        jogaPrimeiro()
    if vezrandom==2:
        input('O BOT irá jogar primeiro')
        player.append(2)
        bot.append(1)
        jogaSegundo()
    print('-')
    input('Pressione qualquer botão para continuar jogando')
    quadro=['-','-','-',
            '-','-','-',
            '-','-','-']
#1-036
#2-147
#3-258
#4-012
#5-345
#6-678
#7-642
#8-048

#[0][1][2]      [A1][B1][C1]
#[3][4][5]      [A2][B2][C2]
#[6][7][8]      [A3][B3][C3]
