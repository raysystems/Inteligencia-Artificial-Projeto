#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from modules.andar import  frente, tras, direita, esquerda


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


