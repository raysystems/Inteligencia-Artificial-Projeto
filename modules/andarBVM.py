from modules.andar import frente, esquerda, direita, virar_180
from pybricks.parameters import Color
from pybricks.tools import wait
def menor_caminho(pos_bvm, posicao):
   
    x_inicial, y_inicial = pos_bvm[0], pos_bvm[1]
    x_destino, y_destino = posicao[0], posicao[1]

    # Movendo no eixo y primeiro
    if y_inicial != y_destino:
        if y_inicial > y_destino:
            y_inicial -= 1
        else:
            y_inicial += 1

    # Se já estiver alinhado no eixo y, mover no eixo x
    elif x_inicial != x_destino:
        if x_inicial > x_destino:
            x_inicial -= 1
        else:
            x_inicial += 1

    print("bvm ", [x_inicial, y_inicial])

    pos_bvm[0] = x_inicial
    pos_bvm[1] = y_inicial



def mover_para_manteiga(motore, motord, gyro, sensor_cor, posicao, posicao_Manteiga, pos_bvm, posicao_Torradeira,ev3):
    x_destino = posicao_Manteiga[0]
    y_destino = posicao_Manteiga[1]
    stunned = 0
    while posicao[0] != x_destino or posicao[1] != y_destino :
        if stunned != 1:

            if posicao[1] < y_destino:
                if posicao[2] == 1:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 2:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 3:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 4:
                    direita(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[1] > y_destino:
                if posicao[2] == 1:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 2:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 3:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 4:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[0] < x_destino:
                if posicao[2] == 1:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 2:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 3:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 4:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
            elif posicao[0] > x_destino:
                if posicao[2] == 1:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 2:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 3:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 4:
                    frente(motore, motord, posicao, sensor_cor)
        else:
            ev3.speaker.beep()
            wait(2000)

        wait(2000)
        menor_caminho(pos_bvm, posicao)
        print("bvm ", pos_bvm)
        print("posicao ", posicao)
        # Se BVM chegar até à manteiga o robot perde
        if (pos_bvm[0] == posicao_Manteiga[0] and pos_bvm[1] == posicao_Manteiga[1]):
            print("BVM CHEGOU NA MANTEIGA")
            return -1
        # Se o robot chegar à posição da manteiga o jogo acaba e o homem tosta ganha
        if (posicao[0] == posicao_Manteiga[0] and posicao[1] == posicao_Manteiga[1]):
            print("O HOMENZINHO CHEGOU NA MANTEIGA")
            return 1
        # se robot entrar na torradeira fica stunned
        if (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 0):
            print("O HOMENZINHO CHEGOU NA TORRADEIRA")
            stunned += 1
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                return -1
        elif (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 1):
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                return -1
            stunned = 0
        # se o bolor chegar a tostadeira o jogo acaba
        if (pos_bvm[0] == posicao_Torradeira[0] and pos_bvm[1] == posicao_Torradeira[1]):
            print("BVM CHEGOU À TORRADEIRA")
            return 1
        #se o bvm chegar ao robot
        if (pos_bvm[0] == posicao[0] and pos_bvm[1] == posicao[1]):
            print("BVM CHEGOU AO HOMENZINHO")
            return -1
        
        # Esperar atÃ© detectar a cor verde para continuar
        
        while sensor_cor.color() != Color.GREEN:
            wait(1)
        wait(1000)
        
        