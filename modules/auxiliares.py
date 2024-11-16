from modules.andar import frente, direita, esquerda, virar_180
from pybricks.tools import wait
from pybricks.parameters import Color

def mover_para_manteiga(motore, motord, gyro, sensor_cor, posicao, posicao_Manteiga):
    x_destino = posicao_Manteiga[0]
    y_destino = posicao_Manteiga[1]

    while posicao[0] != x_destino or posicao[1] != y_destino:
        if posicao[1] < y_destino:
            if posicao[2] == 1:
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 2:
                esquerda(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 3:
                virar_180(motore, motord, gyro, posicao)
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 4:
                direita(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] > y_destino:
            if posicao[2] == 1:
                virar_180(motore, motord, gyro, posicao)
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 2:
                direita(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 3:
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 4:
                esquerda(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] < x_destino:
            if posicao[2] == 1:
                direita(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 2:
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 3:
                esquerda(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 4:
                virar_180(motore, motord, gyro, posicao)
                frente(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] > x_destino:
            if posicao[2] == 1:
                esquerda(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 2:
                virar_180(motore, motord, gyro, posicao)
                frente(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 3:
                direita(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[2] == 4:
                frente(motore, motord, gyro, posicao, sensor_cor)

        # Esperar até detectar a cor verde para continuar
        while sensor_cor.color() != Color.GREEN:
            wait(1)

def fugir_do_BVM(motore, motord, gyro, sensor_cor, posicao, posicao_BVM):
    while calcular_distancia(posicao, posicao_BVM) <= 2:
        if posicao[1] < 6:
            while posicao[2] != 1:
                direita(motore, motord, gyro, posicao, sensor_cor)
            frente(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] > 1:
            while posicao[2] != 3:
                direita(motore, motord, gyro, posicao, sensor_cor)
            frente(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] < 6:
            while posicao[2] != 2:
                direita(motore, motord, gyro, posicao, sensor_cor)
            frente(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] > 1:
            while posicao[2] != 4:
                direita(motore, motord, gyro, posicao, sensor_cor)
            frente(motore, motord, gyro, posicao, sensor_cor)

def calcular_distancia(posicao1, posicao2):
    return abs(posicao1[0] - posicao2[0]) + abs(posicao1[1] - posicao2[1])