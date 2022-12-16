#torre
import data

#falas e escolhas
print("       /-\ \n <<|__/---\__|>> \n _// // |  \\ \_ \n| //// /-\ \\\  | \n/// ///---\\ \ \\ \n |=  =|===|=  =| \n  | = |___| = | \n  +=_________=+        \n   |   ===   |        \n   |   | |   | \n   |   ===   | \n  /|   | |   |\ \n | \   ===   / | \n |\ ':.....:' /| \n | \_________/ |             \n | [** === **] |             \n  \[++ | | ++]/   ")
data.animar('\n Entrando em Torre')
data.sleep(2.0)
data.clear()
data.sleep(1.0)
data.animar('Pudim põe suas patas para bom uso, correndo até Miaudade.\nDentro da cidade, ele se depara com varios Soldados Ratos, os lacaios do Reiqueijão. O que fazer?')
data.animar('\n\n1-Atacar           2-Passar despercebido')
escolha = data.valInt('\n             ')
data.clear()

match escolha:
    case 1:
        data.animar('Você encara de frente os inimigos com sua espada em mãos... ')
        #luta soldado
        data.luta(data.soldadoRato)
        data.animar('O Pudim segue em frente, deixando os inimigos derrotados para trás!')
        input()
        data.clear()
    case 2:
        data.animar('Você tenta passar de fininho pelos ratos, dando passos leves...')
        input()
        if data.sortefuga() == True:
            data.animar('\n...e os deixa pra trás, sem nem saberem que esteve ali!')
        else:
            data.animar('\n...Mas se distrai com uma borboleta! Tentativa falha! ')
            data.luta(data.soldadoRato)
        data.clear()

data.falas('txtes/pudim', 'Pudim', 'Moleza!')
data.animar(' O resto do caminho até a Torre é livre. Pudim abre suas grandes portas (com dificuldade, por não ter dedos) e começa a procurar a entrada para a masmorra.\nHá dois caminhos na sua frente...')
data.animar('\n\n1-Esquerda           2-Direita')
escolha = data.valInt('\n              ')
match escolha:
    case 1:
        data.animar('Pudim segue um longo corredor, se distraindo momentaneamente quando vê um mosquito.\nMais a frente, ele encontra um grande rato, dormindo, porém ao seu lado tem um objeto dourado brilhante. Pudim quer o objeto brilhante.\nO que fazer?')
        data.animar('\n1-Atacar           2-Tentar pegar despercebido')
        escolha = data.valInt('\n             ')
        data.clear()
        match escolha:
            case 1:
                data.animar('Você ataca o inimigo enquanto ele dorme. Golpe Baixo!')
                input ()
                data.clear()
                #luta soldado
                data.luta(data.soldadoRato)
                data.animar('O inimigo dorme de novo (por outro motivo dessa vez). Você se sente um pouco culpado.\n')
                input ()
                data.clear()
                data.animar('Você passa por ele e pega o objeto brilhante, com ele em mãos, você percebe que o objeto é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                input ()
                data.clear()
                data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                data.temChave = True
                input ()
                data.clear()
                data.animar('Você retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                escolha = data.valInt('\n             ')
                data.clear()
                while escolha == 1:
                    data.animar('Você percebe que acaboou de sair desta sala então retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                    escolha = data.valInt('\n             ')
                    data.clear()
                    data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
                    input ()
                    data.clear()

            case 2:
                data.animar('Você dá pulinhos e anda de fininho, até o rato...')
                input ()
                data.clear()
                if data.sortefuga() == True:
                    data.animar('...e fácilmente pega o objeto do seu lado, afinal, ele estava dormindo!')
                    input()
                else:
                    data.animar('...mas tropeça no próprio rabo! Tentativa falha, o rato acordou!')
                    input()
                    data.luta(data.soldadoRato)
                    data.clear()
                data.animar('Com ele em mãos, você percebe que o objeto brilhante é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                input ()
                data.clear()
                data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                data.temChave = True
                data.animar('Você retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                escolha = data.valInt('\n             ')
                data.clear()
                while escolha == 1:
                    data.animar('Você percebe que acabou de sair desta sala então retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                    escolha = data.valInt('\n             ')
                    data.clear()
                    data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
                    input ()
                    data.clear()
data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
input ()
data.clear()
data.falas('txtes/ratão', 'Ratão', 'O que é isso, um gato? Achei que vocês tinham levado seus rabos entre as pernas pra aquele muquifo!')
data.falas('txtes/pudim', 'Pudim', 'Não fale mal do Miauderijo! Agora, me diga logo onde esta o Bola de Pelos!')
data.falas('txtes/ratão', 'Ratão', 'Escuta aqui, eu sou o guarda da masmorra!\n Não vou deixar você soltar o Bola de Pelos que está depois dessa porta atrás de mim!')
data.falas('txtes/pudim', 'Pudim', 'Haha! Você acabou de me contar onde ele está, seu dentuço sujismundo!')
data.falas('txtes/ratão', 'Ratão', 'O que? Droga!!... quer dizer... Foi de proposito!\n Te falei, porque sei que você não vai passar de mim, bichano! Devia ter ficado no muquifo!')
data.falas('txtes/pudim', 'Pudim', 'Rum... Já disse pra não falar mal do Miauderijo!')
#luta com ratao
data.luta(data.ratão)
data.animar('O Ratão cai desacordado, abrindo espaço para a porta atrás dele.')
input()
data.clear()
while data.temChave == False:
    data.animar('Mas a porta está trancada! Hum, onde será que está a chave?')
    input()
    data.clear()
    data.animar('Você retorna, subindo a escada para a sala que estava antes.')
    input()
    data.clear()
    data.animar('Pudim segue um longo corredor, se distraindo momentaneamente quando vê um mosquito.\nEle encontra um grande rato, dormindo, porém ao seu lado tem um objeto dourado brilhante. Pudim quer o objeto brilhante.\nO que fazer?')
    data.animar('\n1-Atacar           2-Tentar pegar despercebido')
    escolha = data.valInt('\n             ')
    data.clear()
    match escolha:
        case 1:
            data.animar('Você ataca o inimigo enquanto ele dorme. Golpe Baixo!')
            input ()
            data.clear()
            #luta soldado
            data.animar('O inimigo dorme de novo (por outro motivo dessa vez). Você se sente um pouco culpado.')
            input()
            data.clear()
            data.animar('Você passa por ele e pega o objeto brilhante, com ele em mãos, você percebe que o objeto é na verdade uma chave. Ele não parece brilhar tanto assim mais')
            input ()
            data.clear()
            data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
            data.temChave = True
            input ()
            data.clear()
        case 2:
                data.animar('Você dá pulinhos e anda de fininho, até o rato...')
                input ()
                data.clear()
                if data.sortefuga() == True:
                    data.animar('...e fácilmente pega o objeto do seu lado, afinal, ele estava dormindo!')
                else:
                    data.animar('...mas tropeça no próprio rabo! Tentativa falha, o rato acordou!')
                    data.luta(data.soldadoRato)
                    data.clear()
                data.animar('Com ele em mãos, você percebe que o objeto brilhante é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                input ()
                data.clear()
                data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                data.temChave = True
data.animar('Você usa a Chave!')
input()
data.clear()
data.animar('Pudim desce o resto das escadas até que, no final, encontra uma única cela.')
input()
data.clear()
data.animar('A Chave parece caber nessa fechadura também...')
input()
data.clear()
data.animar('Abrir?\n1-Abrir           2-Não abrir')
escolha = data.valInt()
data.clear()
match escolha:
    case 1:
        data.falas('txtes/pudim', 'Pudim', 'Vim resgatar você, Bola de Pelos, Miau!')
        data.animar('Um gato velinho, segurando um grande cajado, surje das sombras da cela.')
        input()
        data.clear()
        data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Veja só, se não é Pudim...')
        data.falas('txtes/pudim', 'Pudim', '...')
        data.falas('txtes/gatomago', 'Mago Bola de Pelos', '...')
        data.falas('txtes/pudim', 'Pudim', '...')
        data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Então...\nPor que interrompeu minha soneca, Pudim?')
        data.falas('txtes/pudim', 'Pudim', 'Eu vim te resgatar, velho caduco!... quer dizer, Mago Bola de Pelos!\nOs ratos tomaram conta da nossa cidade, e os gatos de Miaudade foram exilados pro Miauderijo! Precisamos da sua ajuda.')
        data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Hmm... a situação aparenta mais critica do que imaginei...\nPudim, poderia me levar ao Miauderijo?')
        data.falas('txtes/pudim', 'Pudim', 'Rum... vamos lá!')
        data.sleep(2.0)
        data.clear()
        import miauderijo
    case 2:
        data.animar('Pudim repensa a jornada em sua frente. O chamado a ação, os desafios que o encontrariam se continuasse a seguir aquele caminho.\
        \n"Por que eu?" ele pensa, indignado. Ele joga a chave no chão, e retorna pelo mesmo caminho que veio, sem olhar para trás. Pudim\
        \nfoge de Miaudade, não passando no Miauderijo para se despedir de seu avô ou de nenhum dos outros gatos.')
        input()
        data.clear()
        data.animar('A grandiosa hístoria de Pudim, e o ato valente que ele fez que com certeza teria mudado o rumo dos gatos de todo o mundo, nunca\
        \nse realizou para que um dia fosse contada. Nunca mais ouviram falar do Pudim novamente.')
        input()
        data.clear()
        data.animar('Fim.')
        data.sleep(2.0)
        input()
        data.clear()
        import Miaudade
