#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop,Button, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.parameters import SoundFile
from pybricks.media.ev3dev import SoundFile, ImageFile
from modules.andar import  frente, tras, direita, esquerda
from modules.andarBVM import menor_caminho, jogar, waitforinput, dist_to_square, calc_psols, remove_solucoes_nao_otimas
from modules.googlemaps import calcular_rota
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.




# Robot começa no 1,1
# X, Y , ORIENTACAO , FLAG BARREIRA, FLAG CALOR TORRADEIRA
posicao = [1,1,1,0,0]
posicaoBVM = [6,6]
posicao_Torradeira = [6,6]

desviar_barreiras = []
init_dist = 0 #a ser incrementado segundo input
psols = [] #soluções possíveis/quadrados a uma distância igual à dada

barreiras = []



# 0 - x
# 1 - y
#    


# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.set_volume(100)
#DEFINIÃO MOTOR



gyro = GyroSensor(Port.S4)

gyro.reset_angle(0)

motor_Direita = Motor(Port.B)

motor_Esquerda = Motor(Port.D)

sensor_Cor = ColorSensor(Port.S2)



#direita(motor_Esquerda, motor_Direita, gyro)


#frente(motor_Esquerda, motor_Direita)

#direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)

init_dist = waitforinput(ev3, sensor_Cor)
distancia_antiga = init_dist

psols = calc_psols(posicao, init_dist)

if (init_dist <= 5):
    posicao_Manteiga = psols[0]
    caminho_ideal = calcular_rota([posicao[0], posicao[1]], [psols[0][0],psols[0][1]], barreiras)
    print("Caminho ideal: ", caminho_ideal)
    print('sols ',psols)
else:
    print("A distância é muito grande")
    posicao_Manteiga = [3,1]
    caminho_ideal = calcular_rota([posicao[0], posicao[1]], posicao_Manteiga, barreiras)





while(1):
    posicao_Manteiga = caminho_ideal[0]
    print("Caminho ideal primeira iteracao : ", caminho_ideal)
    if posicao_Manteiga[0] == posicao[0] and posicao_Manteiga[1] == posicao[1]:
        caminho_ideal.pop(0)
        posicao_Manteiga = caminho_ideal[0]
    print("O robot neste turno vai para : ", posicao_Manteiga)
    ir_para_manteiga = init_dist
    turno = jogar(caminho_ideal, motor_Esquerda, motor_Direita, gyro, sensor_Cor, posicao, posicao_Manteiga, posicaoBVM,posicao_Torradeira,ev3, init_dist, psols,distancia_antiga, barreiras, ir_para_manteiga)
    if (turno == -1):
        print("GAME OVER")
        for i in range(20):
            ev3.speaker.beep()
            wait(50)
       
        break
    if (turno == 1):
        for i in range(5):
            ev3.speaker.beep()
            wait(1000)
        break
    #se nao encontrou barreira pop numa posicao do caminho

