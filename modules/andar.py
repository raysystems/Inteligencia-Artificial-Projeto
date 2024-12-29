from pybricks.parameters import Stop
from pybricks.tools import DataLog, wait, StopWatch
from pybricks.parameters import Color

barreira = False


def verificarExisteBarreiraQ(sensor_cor):
    return sensor_cor.color() == Color.RED

def verificarExisteCalorTorradeira(sensor_cor, posicao):
    if sensor_cor.color() == Color.BLUE:
        posicao[4] = 1
    

def trocarOrientacao(direcao, posicao):
    if direcao == "E":
        posicao[2] = 4 if posicao[2] - 1 < 1 else posicao[2] - 1
    elif direcao == "D":
        posicao[2] = 1 if posicao[2] + 1 > 4 else posicao[2] + 1

def direita(motore, motord, gyro, posicao, sensor_cor):
    gyro.reset_angle(0)
    if posicao[2] == 1 and posicao[0] <= 5:
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                # Encontrou uma barreira temos que guardar as suas proximas acoes para desviar
                posicao[3] = 1 # ativar flag que encontrou barreira
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] += 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 2 and posicao[1] > 1:
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        gyro.reset_angle(0)
        
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[1] -= 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 3 and posicao[0] > 1:
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        gyro.reset_angle(0)
        
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
                motore.brake()
                motord.brake()
                motore.run(-250)
                motord.run(-250)
                trocarOrientacao("D", posicao)
                wait(1200)
                motore.brake()
                motord.brake()
                return
                
        wait(2200)
        motore.brake()
        motord.brake()
        posicao[0] -= 1
        trocarOrientacao("D", posicao)
    elif posicao[2] == 4 and posicao[1] <= 5:
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        gyro.reset_angle(0)
        
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
    gyro.reset_angle(0)
    if posicao[2] == 1 and posicao[0] > 1:

        while gyro.angle() >= -87:
            motore.run(150)
            motord.run(-150)
        gyro.reset_angle(0)

        motore.brake()
        motord.brake()
        wait(1000)
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
            motore.run(100)
            motord.run(-100)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        wait(1000)
        motore.run(180)
        motord.run(180)
     
       

        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
            motore.run(100)
            motord.run(-100)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
            motore.run(100)
            motord.run(-100)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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
        motore.run(180)
        motord.run(180)
        while sensor_cor.color() != Color.BLACK:
            verificarExisteCalorTorradeira(sensor_cor, posicao)
            if verificarExisteBarreiraQ(sensor_cor):
                posicao[3] = 1 # ativar flag que encontrou barreira
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

def virar_180(motore, motord, gyro, posicao):
    gyro.reset_angle(0)
    if posicao[2] == 1:

        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        wait(2000)
        trocarOrientacao("D", posicao)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        gyro.reset_angle(0)
        motore.brake()
        motord.brake()
        
        trocarOrientacao("D", posicao)
    elif posicao[2] == 2:
        gyro.reset_angle(0)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        wait(2000)
        gyro.reset_angle(0)
        trocarOrientacao("D", posicao)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
    elif posicao[2] == 3:
        gyro.reset_angle(0)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        wait(2000)
        trocarOrientacao("D", posicao)
        gyro.reset_angle(0)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
    elif posicao[2] == 4:
        gyro.reset_angle(0)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        wait(2000)
        gyro.reset_angle(0)
        trocarOrientacao("D", posicao)
        while gyro.angle() <= 90:
            motore.run(-100)
            motord.run(100)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)