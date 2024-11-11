#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop,Button, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from modules.andar import  frente, tras, direita, esquerda
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Robot começa no 1,1
posicao = [1,1,1]
# 0 - x
# 1 - y
#    


# Create your objects here.
ev3 = EV3Brick()

#DEFINIÃO MOTOR



gyro = GyroSensor(Port.S4)

gyro.reset_angle(0)

motor_Direita = Motor(Port.A)

motor_Esquerda = Motor(Port.D)

sensor_Cor = ColorSensor(Port.S2)



#direita(motor_Esquerda, motor_Direita, gyro)


#frente(motor_Esquerda, motor_Direita)

#direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)



while(1):
    randomint = random.randint(1, 3)
    if randomint == 1:
        direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 2:
        esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
    elif randomint == 3:
        frente(motor_Esquerda, motor_Direita, posicao, sensor_Cor)
    
    wait(200)
    ev3.speaker.beep()

 
    while(1):
        wait(200)
        if sensor_Cor.color() == Color.GREEN:
            ev3.speaker.beep()
            break
        pass

        


frente(motor_Esquerda, motor_Direita, posicao, sensor_Cor)
ev3.speaker.beep()
wait(2000)

frente(motor_Esquerda, motor_Direita, posicao, sensor_Cor)
ev3.speaker.beep()



direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
ev3.speaker.beep()
wait(2000)

esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
ev3.speaker.beep()
wait(2000)



# esquerda(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
# ev3.speaker.beep()
# wait(2000)

# direita(motor_Esquerda, motor_Direita, gyro, posicao, sensor_Cor)
# ev3.speaker.beep()
# wait(2000)


#beep


