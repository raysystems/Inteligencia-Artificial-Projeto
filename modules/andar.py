from pybricks.parameters import Stop
from pybricks.tools import DataLog, wait, StopWatch
from pybricks.parameters import Color

def verificarExisteBarreiraQ(sensor_cor):
    return sensor_cor.color() == Color.RED


def trocarOrientacao(direcao, posicao):
    if direcao == "E":
        posicao[2] = 4 if posicao[2] - 1 < 1 else posicao[2] - 1
    elif direcao == "D":
        posicao[2] = 1 if posicao[2] + 1 > 4 else posicao[2] + 1

def direita(motore, motord, gyro, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[0] <= 5:
        while gyro.angle() <= 90:
            motore.run(-250)
            motord.run(250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                break
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 2 and posicao[1] > 1:
        while gyro.angle() <= 90:
            motore.run(-250)
            motord.run(250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                break
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 3 and posicao[0] > 1:
        while gyro.angle() <= 90:
            motore.run(-250)
            motord.run(250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                break
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 4 and posicao[1] <= 5:
        while gyro.angle() <= 90:
            motore.run(-250)
            motord.run(250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                break
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
        trocarOrientacao("D", posicao)

def esquerda(motore, motord, gyro, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[0] > 1:
        while gyro.angle() >= -90:
            motore.run(250)
            motord.run(-250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("E", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        trocarOrientacao("E", posicao)
    elif posicao[2] == 2 and posicao[1] <= 5:
        while gyro.angle() >= -90:
            motore.run(250)
            motord.run(-250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("E", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
        trocarOrientacao("E", posicao)
    elif posicao[2] == 3 and posicao[0] <= 5:
        while gyro.angle() >= -90:
            motore.run(250)
            motord.run(-250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("E", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        trocarOrientacao("E", posicao)
    elif posicao[2] == 4 and posicao[1] > 1:
        while gyro.angle() >= -90:
            motore.run(250)
            motord.run(-250)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("E", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        trocarOrientacao("E", posicao)

def frente(motore, motord, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[1] <= 5:
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] += 1
    elif posicao[2] == 2 and posicao[0] <= 5:
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
    elif posicao[2] == 3 and posicao[1] > 1:
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
    elif posicao[2] == 4 and posicao[0] > 1:
        motore.run(250)
        motord.run(250)
        while sensor_cor.color() != Color.BLACK:
            if verificarExisteBarreiraQ(sensor_cor):
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                wait(1200)
                motore.brake()
                motord.brake()
                return
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1

def tras(motore, motord, posicao, sensor_cor):
    if posicao[2] == 1 and posicao[1] > 1:
        motore.run(-250)
        motord.run(-250)
        while sensor_cor.color() != Color.BLACK:
            pass
        wait(500)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
    elif posicao[2] == 2 and posicao[0] > 1:
        motore.run(-250)
        motord.run(-250)
        while sensor_cor.color() != Color.BLACK:
            pass
        wait(500)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
    elif posicao[2] == 3 and posicao[1] <= 5:
        motore.run(-250)
        motord.run(-250)
        while sensor_cor.color() != Color.BLACK:
            pass
        wait(500)
        motore.brake()
        motord.brake()
        posicao[1] += 1
    elif posicao[2] == 4 and posicao[0] <= 5:
        motore.run(-250)
        motord.run(-250)
        while sensor_cor.color() != Color.BLACK:
            pass
        wait(500)
        motore.brake()
        motord.brake()
        posicao[0] += 1