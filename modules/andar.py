from pybricks.tools import wait 
from pybricks.parameters import Color 
from pybricks.hubs import EV3Brick

beep = EV3Brick()

barreira = False

def verificarBarreira(motore, motord, sensor_Cor):
    global barreira
    if (sensor_Cor.color() == Color.RED):
        motore.brake()
        motord.brake()
        motore.run(-150)
        motord.run(-150)
        wait(1200)
        motore.brake()
        motord.brake()
        # variavel para nao incrementar a posicao pois o robo nao andou devido a uma barreira
        barreira = True


# Função para verificar se ja andou uma casa apos encontrar a linha preta anda por um x tempo ate ficar dentro do quadrado
def verificarPassagem(motore, motord, sensor_Cor, posicao, direcao):
    global barreira
    while sensor_Cor.color() != Color.BLACK:
        if not(barreira):
            motore.run(180)
            motord.run(180)
            verificarBarreira(motore, motord, sensor_Cor)
        else:
            break


def trocarOrientacao(direcao, posicao):
    if direcao == "E":
        # Se a orientação atual é 1 (Norte), muda para 4 (Oeste), caso contrário, decrementa 1
        if posicao[2] - 1 < 1:
            posicao[2] = 4 
        else:
            posicao[2] -= 1
    elif direcao == "D":
        # Se a orientação atual é 4 (Oeste), muda para 1 (Norte), caso contrário, incrementa 1
        if posicao[2] + 1 > 4:
            posicao[2] = 1 
        else:
            posicao[2] += 1

def direita(motore, motord, gyro, posicao, sensor_Cor):
    global barreira
    if posicao[2] == 1 and posicao[0] <= 5:
        while int(gyro.angle()) < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "D")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] += 1
        barreira = False
        
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 2 and posicao[1] > 1:
        while int(gyro.angle()) < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "D")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] -= 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 3 and posicao[0] > 1:
        while int(gyro.angle()) < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "D")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] -= 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 4 and posicao[1] <= 5:
        while int(gyro.angle()) < 90:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        trocarOrientacao("D", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "D")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] += 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
def esquerda(motore, motord, gyro, posicao, sensor_Cor):
    global barreira
    if posicao[2] == 1 and posicao[0] > 1:
        while int(gyro.angle()) > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        trocarOrientacao("E", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "E")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] -= 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 2 and posicao[1] <= 5:
        while int(gyro.angle()) > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        trocarOrientacao("E", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "E")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] += 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 3 and posicao[0] <= 5:
        while int(gyro.angle()) > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        trocarOrientacao("E", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "E")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] += 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 4 and posicao[1] > 1:
        while int(gyro.angle()) > -90:
            motore.run(-150)
            motord.run(150)
        motore.brake()
        motord.brake()
        trocarOrientacao("E", posicao)
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "E")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] -= 1
        barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()

def frente(motore, motord, gyro, posicao, sensor_Cor):
    global barreira
    if posicao[2] == 1 and posicao[1] <= 5:
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "F")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] += 1
            barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 2 and posicao[0] <= 5:
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "F")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] += 1
            barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 3 and posicao[1] > 1:
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "F")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[1] -= 1
            barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()
    elif posicao[2] == 4 and posicao[0] > 1:
        motore.run(180)
        motord.run(180)
        verificarPassagem(motore, motord, sensor_Cor, posicao, "F")
        wait(3000)
        if not(barreira):
            motore.brake()
            motord.brake()
            posicao[0] -= 1
            barreira = False
        gyro.reset_angle(0)
        print(posicao)
        beep.speaker.beep()


def virar_180(motore, motord, gyro, posicao):
    if posicao[2] == 1:
        while gyro.angle() < 180:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        posicao[2] = 3
        gyro.reset_angle(0)
    elif posicao[2] == 2:
        while gyro.angle() < 180:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        posicao[2] = 4
        gyro.reset_angle(0)
    elif posicao[2] == 3:
        while gyro.angle() < 180:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        posicao[2] = 1
        gyro.reset_angle(0)
    elif posicao[2] == 4:
        while gyro.angle() < 180:
            motore.run(150)
            motord.run(-150)
        motore.brake()
        motord.brake()
        posicao[2] = 2
        gyro.reset_angle(0)