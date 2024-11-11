def menor_caminho(destino):
    posicao = [6, 6]
    x_inicial, y_inicial = posicao
    x_destino, y_destino = destino

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

    return [x_inicial, y_inicial]



# Exemplo de uso
destino = [4, 3]
print(menor_caminho(destino)) 