#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop,Button, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from modules.andar import  frente, direita, esquerda
import random

# Robô começa na posição [1,1]
posicao = [1,1,1]
# posicao[0] - x
# posicao[1] - y
# posicao[2] = 1 -> Norte
# posicao[2] = 2 -> Este
# posicao[2] = 3 -> Sul
# posicao[2] = 4 -> Oeste

# BVM começa na posição [6,6]
posicao_BVM = [6,6]

# Manteiga começa numa posição [x,y]
posicao_Manteiga = [3,3]

# Torradeira começa numa posição [i,z]
posicao_Torradeira = [5,2]


# Create your objects here.
ev3 = EV3Brick()


#DEFINIÃO MOTOR

sensor_Cor = ColorSensor(Port.S2)

gyro = GyroSensor(Port.S4)

gyro.reset_angle(0)

motor_Direita = Motor(Port.D)

motor_Esquerda = Motor(Port.A)


# Write your program here.


while(1):
    randomint = random.randint(1, 3)
    if randomint == 1:
        direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 2:
        esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 3:
        frente(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    

 
    while(1):
        wait(200)
        if sensor_Cor.color() == Color.GREEN:
            ev3.speaker.beep()
            break
        pass


