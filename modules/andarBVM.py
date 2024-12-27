from modules.andar import frente, esquerda, direita, virar_180
from modules.googlemaps import calcular_rota
from pybricks.parameters import Color
from pybricks.tools import wait
def menor_caminho(pos_bvm, posicao):
   
    x_inicial, y_inicial = pos_bvm[0], pos_bvm[1]
    x_destino, y_destino = posicao[0], posicao[1]

    # Movendo no eixo y primeiro
    if y_inicial != y_destino:
        if y_inicial > y_destino:
            y_inicial -= 1
        else:
            y_inicial += 1

    # Se já estiver alinhado no eixo y, mover no eixo x
    elif x_inicial != x_destino:
        if x_inicial > x_destino:
            x_inicial -= 1
        else:
            x_inicial += 1

    print("bvm ", [x_inicial, y_inicial])

    pos_bvm[0] = x_inicial
    pos_bvm[1] = y_inicial


def irparaCoords(x_destino, y_destino, posicao, motore, motord, gyro, sensor_cor):
    #primeiro ver a orientacao do robot
    #caso norte
    print("Estou indo para Posicao ", x_destino, y_destino)
    print("IR PARA COORDS // X: ", x_destino, " Y: ", y_destino)
    print("IR PARA COORDS // Posicao atual: ", posicao)

    if posicao[2] == 1:
        if posicao[0] > x_destino:
            print("Norte: Virando à esquerda")
            esquerda(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] < x_destino:
            print("Norte: Virando à direita")
            direita(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] > y_destino:
            print("Norte: Virando 180 graus")
            virar_180(motore, motord, gyro, posicao)
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[1] < y_destino:
            print("Norte: Indo para frente")
            frente(motore, motord, posicao, sensor_cor)
    #caso sul
    elif posicao[2] == 3:
        if posicao[0] > x_destino:
            print("Sul: Virando à direita")
            direita(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[0] < x_destino:
            print("Sul: Virando à esquerda")
            esquerda(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] > y_destino:
            print("Sul: Indo para frente")
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[1] < y_destino:
            print("Sul: Virando 180 graus")
            virar_180(motore, motord, gyro, posicao)
            frente(motore, motord, posicao, sensor_cor)
    #caso este
    elif posicao[2] == 2:
        if posicao[0] > x_destino:
            print("Este: Virando 180 graus")
            virar_180(motore, motord, gyro, posicao)
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[0] < x_destino:
            print("Este: Indo para frente")
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[1] > y_destino:
            print("Este: Virando à direita")
            direita(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] < y_destino:
            print("Este: Virando à esquerda")
            esquerda(motore, motord, gyro, posicao, sensor_cor)
    #caso oeste
    elif posicao[2] == 4:
        if posicao[0] > x_destino:
            print("Oeste: Indo para frente")
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[0] < x_destino:
            print("Oeste: Virando 180 graus")
            virar_180(motore, motord, gyro, posicao)
            frente(motore, motord, posicao, sensor_cor)
        elif posicao[1] > y_destino:
            print("Oeste: Virando à esquerda")
            esquerda(motore, motord, gyro, posicao, sensor_cor)
        elif posicao[1] < y_destino:
            print("Oeste: Virando à direita")
            direita(motore, motord, gyro, posicao, sensor_cor)
    


def waitforinput(ev3,sensor_cor):

    #distância para cada cor

    d3 = Color.BLUE
    d2 = Color.RED
    md2 = Color.BLACK #para decrementar em caso de bug, sem ter que reiniciar o programa
    total_dist = 0

    while sensor_cor.color() != Color.GREEN:
        color = sensor_cor.color()
        if color == d3:
            total_dist += 1
            ev3.speaker.beep()
            print(total_dist)
            wait(1000)
        elif color == d2:
            total_dist += 2
            ev3.speaker.beep()
            print(total_dist)
            wait(1000)
        elif color == md2:
            total_dist -= 1
            ev3.speaker.beep()
            print(total_dist)
            wait(1000)
        else:
            wait(100)
        ev3.screen.clear()
        ev3.screen.print("Distância: ", total_dist)
    wait(1000)
    ev3.screen.clear()
    ev3.screen.print("Distância: ", total_dist)
    #escrever no ecra do ev3 a distância
    
    return total_dist

def dist_to_square(posicao, square): #devolve dist do robô até o quadrado passado como arg
    return abs(posicao[0]-square[0])+abs(posicao[1]-square[1])

def calc_psols(posicao, dist): #devolve as soluções possíveis iniciais
    psols = []
    for y in range(6):
        for x in range(6):
            if dist_to_square(posicao,[x+1,y+1]) == dist:
                psols.append([x+1,y+1,dist])
    return psols

#devolve as novas sols dependendo se ficou mais perto/longe
def remove_solucoes_nao_otimas(posicao, new_dist, distancia_antiga, sols):
    if(len(sols) != 1):
        # Recalcular todas as distâncias
        for sol in sols:
            sol[2] = dist_to_square(posicao, [sol[0], sol[1]])

            
        # Criar uma nova lista com as soluções filtradas
        sols = [sol for sol in sols if sol[2] == new_dist]
    
    print("Soluções possíveis: ", sols)
    return sols



def jogar(caminho_ideal, motore, motord, gyro, sensor_cor, posicao, posicao_Manteiga, pos_bvm, posicao_Torradeira,ev3, init_dist, psols, distancia_antiga, barreiras,ir_para_manteiga):
    x_destino = posicao_Manteiga[0]
    y_destino = posicao_Manteiga[1]
    copia_x_destino = x_destino
    copia_y_destino = y_destino
    estrategia1_fase1 = 0
    stunned = 0
    new_dist = init_dist
    while (1):
        if stunned != 1:
            # criar funcao ir para coords. x_destino, y_destino
           
            
            irparaCoords(x_destino,y_destino, posicao, motore, motord, gyro, sensor_cor)
        else:
            ev3.speaker.beep()
            wait(2000)

        wait(1000)
        menor_caminho(pos_bvm, posicao)
        print("bvm ", pos_bvm)
        print("posicao ", posicao)
        # Se BVM chegar até à manteiga o robot perde
        if (pos_bvm[0] == posicao_Manteiga[0] and pos_bvm[1] == posicao_Manteiga[1]):
            print("BVM CHEGOU NA MANTEIGA")
            #return -1
        # Se o robot chegar à posição da manteiga o jogo acaba e o homem tosta ganha
        if (posicao[0] == posicao_Manteiga[0] and posicao[1] == posicao_Manteiga[1]):
            print("O HOMENZINHO CHEGOU NA MANTEIGA")
            #return 1
        # se robot entrar na torradeira fica stunned
        if (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 0):
            print("O HOMENZINHO CHEGOU NA TORRADEIRA")
            stunned += 1
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                #return -1
        elif (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 1):
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                #return -1
            stunned = 0
        # se o bolor chegar a tostadeira o jogo acaba
        if (pos_bvm[0] == posicao_Torradeira[0] and pos_bvm[1] == posicao_Torradeira[1]):
            print("BVM CHEGOU À TORRADEIRA")
            #return 1
        #se o bvm chegar ao robot
        if (pos_bvm[0] == posicao[0] and pos_bvm[1] == posicao[1]):
            print("BVM CHEGOU AO HOMENZINHO")
            #return -1
        
        # Esperar atÃ© detectar a cor verde para continuar

        

        if (distancia_antiga > new_dist):
            distancia_antiga = new_dist
            #print("Distancia antiga ", distancia_antiga)


        #agora que estao recalculadas as solucoes possiveis, calcular a nova rota
        # se foi encontrada uma barreira temos que recalcular a rota
        if (posicao[3] == 1):
            # a barreira foi encontrada e temos que adiconar a barreira à lista de barreiras
            # para isso e necessario ter em consideracao a posicao do robot e que ele ia
            # para a posicao da barreira

            posicao[3] = 0
            # temos que ver com base no destino e orientacao do robot qual seria a nova coordenada
            # para onde ele ia
            copia_posicao = [posicao[0], posicao[1]]
            if posicao[2] == 1:
                # se estava para norte temos que analisar a sua posicao atual face ao destino
                if posicao[0] > x_destino:
                    copia_posicao[0] -= 1
                elif posicao[0] < x_destino:
                    copia_posicao[0] += 1
                elif posicao[1] > y_destino:
                    copia_posicao[1] -= 1
                elif posicao[1] < y_destino:
                    copia_posicao[1] += 1
            elif posicao[2] == 2:
                # se estava para este temos que analisar a sua posicao atual face ao destino
                if posicao[0] > x_destino:
                    copia_posicao[0] -= 1
                elif posicao[0] < x_destino:
                    copia_posicao[0] += 1
                elif posicao[1] > y_destino:
                    copia_posicao[1] -= 1
                elif posicao[1] < y_destino:
                    copia_posicao[1] += 1
            elif posicao[2] == 3:
                # se estava para sul temos que analisar a sua posicao atual face ao destino
                if posicao[0] > x_destino:
                    copia_posicao[0] -= 1
                elif posicao[0] < x_destino:
                    copia_posicao[0] += 1
                elif posicao[1] > y_destino:
                    copia_posicao[1] -= 1
                elif posicao[1] < y_destino:
                    copia_posicao[1] += 1
            elif posicao[2] == 4:
                # se estava para oeste temos que analisar a sua posicao atual face ao destino
                if posicao[0] > x_destino:
                    copia_posicao[0] -= 1
                elif posicao[0] < x_destino:
                    copia_posicao[0] += 1
                elif posicao[1] > y_destino:
                    copia_posicao[1] -= 1
                elif posicao[1] < y_destino:
                    copia_posicao[1] += 1
            print("Copia posicao ", copia_posicao)
            #agora que sabemos para onde ele ia e a sua posicao atual podemos inserir na lista de barreiras
            # a barreira que ele encontrou
            barreiras.append([[posicao[0], posicao[1]], [copia_posicao[0], copia_posicao[1]]])  
            print("Barreiras ", barreiras)
            #agora sim vamos recalcula a rota
            if (posicao[0] != 3 and posicao[1] != 1 and ir_para_manteiga > 5):
                x_destino = 3
                y_destino = 1
            if (posicao[0] == 3 and posicao[1] == 1 ):
                estrategia1_fase1 = 1
            if (posicao[0] == 3 and posicao[1] <= 5 and ir_para_manteiga > 5 and estrategia1_fase1 == 1):
                x_destino = 3
                y_destino = 5
            caminho_ideal = calcular_rota([posicao[0], posicao[1]], [x_destino, y_destino], barreiras)
            print("Caminho ideal antes do pop: ", caminho_ideal)
            if len(caminho_ideal) > 1:
                caminho_ideal.pop(0)
            print("Caminho ideal depois do pop: ", caminho_ideal)

            x_destino = caminho_ideal[0][0]
            y_destino = caminho_ideal[0][1]
            copia_x_destino = x_destino
            copia_y_destino = y_destino
            print("Dado que encontrei uma Barreira Tem se um novo caminho - ", caminho_ideal)
        else:
            #o destino pode ter mudado portanto vamos recalcular a rota
            #se o destino mudar recalculo a rota caso contrario pop
            if (posicao[0] != 3 and posicao[1] != 1 and ir_para_manteiga > 5):
                x_destino = 3
                y_destino = 1
            if (posicao[0] == 3 and posicao[1] == 1 ):
                estrategia1_fase1 = 1
            if (posicao[0] == 3 and posicao[1] <= 5 and ir_para_manteiga > 5 and estrategia1_fase1 == 1):
                x_destino = 3
                y_destino = 5
            if (copia_x_destino != x_destino or copia_y_destino != y_destino): 
                caminho_ideal = calcular_rota([posicao[0], posicao[1]], [x_destino, y_destino], barreiras)
                if len(caminho_ideal) > 1:
                    caminho_ideal.pop(0) #remover a posicao atual do robot
                x_destino = caminho_ideal[0][0]
                y_destino = caminho_ideal[0][1]
                copia_x_destino = x_destino
                copia_y_destino = y_destino
            else:
                print("Caminho ideal LINHA 298: ", caminho_ideal)
                if len(caminho_ideal) > 1:
                    caminho_ideal.pop(0)
                x_destino = caminho_ideal[0][0]
                y_destino = caminho_ideal[0][1]
                copia_x_destino = x_destino
                copia_y_destino = y_destino
        

        new_dist = waitforinput(ev3, sensor_cor)
        
       

        newpsols = remove_solucoes_nao_otimas(posicao,new_dist,distancia_antiga,psols)
        psols = newpsols

        if len(psols) == 1:
            print("Posição final Manteiga: ", psols[0])
            #rever isto
            if (ir_para_manteiga <= 5):
                print("Atualizado destino para distancia menos de 5: ", psols[0])
                x_destino = psols[0][0]
                y_destino = psols[0][1]
                # se atualizou o destino vamos recalcular a rota
                caminho_ideal = calcular_rota([posicao[0], posicao[1]], [x_destino, y_destino], barreiras)
                caminho_ideal.pop(0)
                x_destino = caminho_ideal[0][0]
                y_destino = caminho_ideal[0][1]
                print("Caminho ideal PSOLS: ", caminho_ideal)
        elif(ir_para_manteiga <= 5): 
            print("Atualizado destino para distancia menos de 5: ", psols[0])
            x_destino = psols[0][0]
            y_destino = psols[0][1]
            # se atualizou o destino vamos recalcular a rota
            caminho_ideal = calcular_rota([posicao[0], posicao[1]], [x_destino, y_destino], barreiras)
            caminho_ideal.pop(0)
            x_destino = caminho_ideal[0][0]
            y_destino = caminho_ideal[0][1]
            print("Caminho ideal PSOLS: ", caminho_ideal)

        

        
        
        



            
        
        
