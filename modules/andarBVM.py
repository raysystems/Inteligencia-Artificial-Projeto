from modules.andar import frente, esquerda, direita, virar_180
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

def waitforinput(ev3,sensor_cor):

    #distância para cada cor
    d4 = Color.BROWN
    d3 = Color.BLUE
    d2 = Color.RED
    d1 = Color.YELLOW
    md2 = Color.BLACK #para decrementar em caso de bug, sem ter que reiniciar o programa
    total_dist = 0

    while sensor_cor.color() != Color.GREEN:
        match sensor_cor.color(): #python >= 3.10
            case d4:
                total_dist += 4
                ev3.speaker.beep()
                print(total_dist)
                wait(1000)
            case d3:
                total_dist += 3
                ev3.speaker.beep()
                print(total_dist)
                wait(1000)
            case d2:
                total_dist += 2
                ev3.speaker.beep()
                print(total_dist)
                wait(1000)
            case d1:
                total_dist += 1
                ev3.speaker.beep()
                print(total_dist)
                wait(1000)
            case md2:
                total_dist -= 2
                ev3.speaker.beep()
                print(total_dist)
                wait(1000)
            case default:
                wait(100)
    wait(1000)
    return total_dist

def dist_to_square(posicao, square): #devolve dist do robô até o quadrado passado como arg
    return abs(posicao[0]-square[0])+abs(posicao[1]-square[1])

def calc_psols(posicao, dist): #devolve as soluções possíveis iniciais
    psols = []
    for y in range(6):
        for x in range(6):
            if dist_to_square(posicao,[x+1,y+1]) == dist:
                psols.append([x+1,y+1])
    return psols

#devolve as novas sols dependendo se ficou mais perto/longe
def calc_new_sols(previous_pos, current_pos, previous_dist, current_dist, current_sols):
    if previous_dist > current_dist: #está mais perto
        for sol in current_sols: #remove os que ficaram mais longe
            if dist_to_square(current_pos, sol) > dist_to_square(previous_pos,sol):
                current_sols.remove(sol)
    else: #está mais longe
        for sol in current_sols: #remove os que ficaram mais perto
            if dist_to_square(current_pos, sol) < dist_to_square(previous_pos,sol):
                current_sols.remove(sol)
    return current_sols



def mover_para_manteiga(motore, motord, gyro, sensor_cor, posicao, posicao_Manteiga, pos_bvm, posicao_Torradeira,ev3, init_dist, psols):
    x_destino = posicao_Manteiga[0]
    y_destino = posicao_Manteiga[1]
    stunned = 0
    pos_queue = [posicao] #queue para a posição atual e anterior do robô
    dist_queue = [init_dist]
    while posicao[0] != x_destino or posicao[1] != y_destino :
        new_dist = 0
        if stunned != 1:

            if posicao[1] < y_destino:
                if posicao[2] == 1:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 2:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 3:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 4:
                    direita(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[1] > y_destino:
                if posicao[2] == 1:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 2:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 3:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 4:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
            elif posicao[0] < x_destino:
                if posicao[2] == 1:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 2:
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 3:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 4:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
            elif posicao[0] > x_destino:
                if posicao[2] == 1:
                    esquerda(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 2:
                    virar_180(motore, motord, gyro, posicao)
                    frente(motore, motord, posicao, sensor_cor)
                elif posicao[2] == 3:
                    direita(motore, motord, gyro, posicao, sensor_cor)
                elif posicao[2] == 4:
                    frente(motore, motord, posicao, sensor_cor)
        else:
            ev3.speaker.beep()
            wait(2000)

        wait(2000)
        menor_caminho(pos_bvm, posicao)
        print("bvm ", pos_bvm)
        print("posicao ", posicao)
        # Se BVM chegar até à manteiga o robot perde
        if (pos_bvm[0] == posicao_Manteiga[0] and pos_bvm[1] == posicao_Manteiga[1]):
            print("BVM CHEGOU NA MANTEIGA")
            return -1
        # Se o robot chegar à posição da manteiga o jogo acaba e o homem tosta ganha
        if (posicao[0] == posicao_Manteiga[0] and posicao[1] == posicao_Manteiga[1]):
            print("O HOMENZINHO CHEGOU NA MANTEIGA")
            return 1
        # se robot entrar na torradeira fica stunned
        if (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 0):
            print("O HOMENZINHO CHEGOU NA TORRADEIRA")
            stunned += 1
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                return -1
        elif (posicao[0] == posicao_Torradeira[0] and posicao[1] == posicao_Torradeira[1] and stunned == 1):
            if (pos_bvm == posicao_Torradeira):
                print("HOMEM TOSTA ESTAVA NA TORRADEIRA E BVM CHEGOU À TORRADEIRA")
                return -1
            stunned = 0
        # se o bolor chegar a tostadeira o jogo acaba
        if (pos_bvm[0] == posicao_Torradeira[0] and pos_bvm[1] == posicao_Torradeira[1]):
            print("BVM CHEGOU À TORRADEIRA")
            return 1
        #se o bvm chegar ao robot
        if (pos_bvm[0] == posicao[0] and pos_bvm[1] == posicao[1]):
            print("BVM CHEGOU AO HOMENZINHO")
            return -1
        
        # Esperar atÃ© detectar a cor verde para continuar
        new_dist = waitforinput(ev3, sensor_cor)

        #mantém as 2 distâncias e posições mais recentes em queues
        dist_queue.append(new_dist)
        if len(dist_queue) > 2:
            dist_queue.pop(0)
        pos_queue.append(posicao)
        if len(pos_queue) > 2:
            pos_queue.pop(0)

        #atualiza as soluções possíveis
        psols = calc_new_sols(pos_queue[0],pos_queue[1],dist_queue[0],dist_queue[1],psols)
        
        x_destino = psols[0][0]
        y_destino = psols[0][1]

        #!importante, falta dar fix na condição de detetar se o homem chegou à manteiga, o bvm chegou à manteiga, e o q está hardcoded da fase anterior
        
        
        
