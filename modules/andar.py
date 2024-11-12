from pybricks.parameters import Stop 
from pybricks.tools import DataLog, wait, StopWatch 
from pybricks.parameters import Color 

def verificarExisteBarreiraQ(sensor_cor):
    return sensor_cor.color() == Color.RED

def verificarBarreira(motore, motord, sensor_cor, posicao, direcao, trocar):
    while sensor_cor.color() != Color.BLACK:
        if verificarExisteBarreiraQ(sensor_cor):
            motore.brake()
            motord.brake()
            motore.run(-150)
            motord.run(-150)
            if trocar:
                trocarOrientacao(direcao, posicao)
            wait(1200)
            motore.brake()
            motord.brake()
            return


def trocarOrientacao(direcao, posicao):
    if direcao == "E":
        # Se a orientação atual é 1 (Norte), muda para 4 (Oeste), caso contrário, decrementa 1
        if posicao[2] - 1 < 1:
            posicao[2] = 4 
        else:
            posicao[2] -= 1
    elif direcao == "D":
        # Se a orientação atual é 4 (Oeste), muda para 1 (Norte), caso contrário, incrementa 1
        print("teste")
        if posicao[2] + 1 > 4:
            posicao[2] = 1 
        else:
            posicao[2] += 1

def direita(motore, motord, gyro, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[0] <= 5:
        while gyro.angle() < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "D", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        trocarOrientacao("D", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 2 and posicao[1] > 1:
        while gyro.angle() < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "D", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        trocarOrientacao("D", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 3 and posicao[0] > 1:
        while gyro.angle() < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "D", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        trocarOrientacao("D", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 4 and posicao[1] <= 5:
        while gyro.angle() < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "D", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
        trocarOrientacao("D", posicao)
        gyro.reset_angle(0)
        print(posicao)

def esquerda(motore, motord, gyro, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[0] > 1:
        while gyro.angle() > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "E", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        trocarOrientacao("E", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 2 and posicao[1] <= 5:
        while gyro.angle() > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "E", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
        trocarOrientacao("E", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 3 and posicao[0] <= 5:
        while gyro.angle() > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "E", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        trocarOrientacao("E", posicao)
        gyro.reset_angle(0)
        print(posicao)
    elif posicao[2] == 4 and posicao[1] > 1:
        while gyro.angle() > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "E", True)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        trocarOrientacao("E", posicao)
        gyro.reset_angle(0)
        print(posicao)

def frente(motore, motord, gyro, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[1] <= 5:
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "F", False)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
        gyro.reset_angle(0)
    elif posicao[2] == 2 and posicao[0] <= 5:
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "F", False)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        gyro.reset_angle(0)
    elif posicao[2] == 3 and posicao[1] > 1:
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "F", False)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        gyro.reset_angle(0)
    elif posicao[2] == 4 and posicao[0] > 1:
        motore.run(180)
        motord.run(180)
        verificarBarreira(motore, motord, sensor_cor, posicao, "F", False)
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        gyro.reset_angle(0)