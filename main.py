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
from modules.andarBVM import menor_caminho, mover_para_manteiga, waitforinput, dist_to_square, calc_psols, remove_solucoes_nao_otimas
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.




# Robot começa no 1,1
# X, Y , ORIENTACAO , FLAG 
posicao = [1,1,1,0]
posicaoBVM = [5,5]
posicao_Torradeira = [6,6]

desviar_barreiras = []
init_dist = 0 #a ser incrementado segundo input
psols = [] #soluções possíveis/quadrados a uma distância igual à dada




# 0 - x
# 1 - y
#    


# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.set_volume(100)
#DEFINIÃO MOTOR



gyro = GyroSensor(Port.S4)

gyro.reset_angle(0)

motor_Direita = Motor(Port.A)

motor_Esquerda = Motor(Port.D)

sensor_Cor = ColorSensor(Port.S2)



#direita(motor_Esquerda, motor_Direita, gyro)


#frente(motor_Esquerda, motor_Direita)

#direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)

init_dist = waitforinput(ev3, sensor_Cor)
distancia_antiga = init_dist

psols = calc_psols(posicao, init_dist)

posicao_Manteiga = psols[0]

print(psols)

print("Posicao que vai testar a manteiga Manteiga: ", posicao_Manteiga)
#gerar uma posicao aleatoria para que nao coincida nem com a manteiga nem o BVM nem com o homem tosta
#while (posicao_Torradeira == posicao or posicao_Torradeira == posicaoBVM or posicao_Torradeira == posicao_Manteiga):
  #  posicao_Torradeira = [random.randint(1, 6), random.randint(1, 6)]  
print("Posicao Torradeira: ", posicao_Torradeira)

while(1):
    turno = mover_para_manteiga(motor_Esquerda, motor_Direita, gyro, sensor_Cor, posicao, posicao_Manteiga, posicaoBVM,posicao_Torradeira,ev3, init_dist, psols,distancia_antiga)
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
    '''
    

    randomint = random.randint(1, 3)
    if randomint == 1:
        direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 2:
        esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 3:
        frente(motor_Esquerda, motor_Direita, posicao, sensor_Cor)
      
    wait(200)
    ev3.speaker.beep()
    print(posicao)
    print("BVM")

 
    while(1):
        wait(200)
        if sensor_Cor.color() == Color.GREEN:
            ev3.speaker.beep()
            break
        pass
    
          '''






# esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
# ev3.speaker.beep()
# wait(2000)

# direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
# ev3.speaker.beep()
# wait(2000)


#beep

