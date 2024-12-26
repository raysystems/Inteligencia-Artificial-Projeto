from collections import deque

class NoArvore:
    def __init__(self, posicao):
        self.posicao = posicao  # Posição do nó [x, y]
        self.filhos = []        # Lista de filhos (nós adjacentes)

    def adicionar_filho(self, no_filho):
        self.filhos.append(no_filho)


def calcular_vizinhos(posicao):
    """Calcula as posições vizinhas possíveis no grid."""
    x, y = posicao
    vizinhos = []
    if x - 1 >= 1:
        vizinhos.append([x - 1, y])  # Cima
    if x + 1 <= 6:
        vizinhos.append([x + 1, y])  # Baixo
    if y - 1 >= 1:
        vizinhos.append([x, y - 1])  # Esquerda
    if y + 1 <= 6:
        vizinhos.append([x, y + 1])  # Direita
    return vizinhos


def construir_arvore(posicao, profundidade_maxima, barreiras):
    """
    Constrói uma árvore de posições possíveis até uma profundidade máxima usando BFS.
    """
    raiz = NoArvore(posicao)
    fila = deque([(raiz, 0)])  # Fila para BFS, contendo nós e suas profundidades
    visitados = set()
    visitados.add(tuple(posicao))

    while fila:
        no_atual, profundidade = fila.popleft()
        if profundidade >= profundidade_maxima:
            continue

        for vizinho in calcular_vizinhos(no_atual.posicao):
            if tuple(vizinho) in visitados:
                continue  # Ignora filhos que já foram visitados
            if [no_atual.posicao, vizinho] in barreiras or [vizinho, no_atual.posicao] in barreiras:
                continue  # Ignora caminhos com barreiras

            no_filho = NoArvore(vizinho)
            no_atual.adicionar_filho(no_filho)
            fila.append((no_filho, profundidade + 1))
            visitados.add(tuple(vizinho))

    return raiz


def bfs_encontrar_destino(raiz, destino, barreiras):
    """
    Realiza uma busca em largura (BFS) para encontrar o destino.
    """
    fila = deque([(raiz, [])])  # Fila para BFS, contendo nós e o caminho percorrido
    visitados = set()
    visitados.add(tuple(raiz.posicao))

    while fila:
        no_atual, caminho = fila.popleft()
        caminho.append(no_atual.posicao)

        if no_atual.posicao == destino:
            return caminho

        for filho in no_atual.filhos:
            if tuple(filho.posicao) not in visitados:
                fila.append((filho, caminho.copy()))
                visitados.add(tuple(filho.posicao))

    return None


def calcular_rota(posicao_atual, destino, barreiras):
    """
    Calcula a rota do robô até o destino, considerando as barreiras encontradas.
    """
    profundidade_maxima = 3
    caminho_seguido = []
    print("Destino: ", destino) 
    print("Posicao atual: ", posicao_atual)

    while True:
        print("Tentando com profundidade máxima .")
        raiz = construir_arvore(posicao_atual, profundidade_maxima, barreiras)
        caminho = bfs_encontrar_destino(raiz, destino, barreiras)
        if not caminho:
            #print("Não há caminho disponível para o destino. Aumentando a profundidade máxima e tentando novamente.")
            profundidade_maxima += 1
            continue

        #print(f"Caminho encontrado: {caminho}")
        caminho_seguido = caminho
        break

    return caminho_seguido


