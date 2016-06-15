import random
from shapely.geometry import Polygon, Point

def ponto_unico(poligono):
    """ 
    A função cria_ponto_aleatorio cria um unico ponto aleatorio dentro de um poligono
    
    Dados de entrada: latitute e longitude de cada vertice que constroe o poligono
    
    Dados de saida: um par de coordenadas (um ponto) gerada aleatoriamente dentro de um poligono
    """
    
    # Recebe cada par de coordenadas do bounding box do poligono
    (coord_S_O, coord_S_L, coord_N_O, coord_N_L) = poligono.bounds

    # Gera ponto aleatorio dentro do bounding box do poligono
    while True:
        ponto_aleatorio = Point(random.uniform(coord_S_O, coord_N_O), random.uniform(coord_S_L, coord_N_L))

        # Verifica se o ponto gerado esta CONTIDO no poligono
        if poligono.contains(ponto_aleatorio):
            
            # Se o ponto gerado estiver CONTIDO no poligono
            # Retorna o ponto gerado
            return ponto_aleatorio

def multiplos_pontos(codigos_e_geometrias, codigos_e_populacao):
    """
    A funcao cria_pontos_aleatorios cria pontos aleatorios dentro de um poligono
    
    Dados de entrada: 1) conjunto de dados (dicionario) que contem o codigo do setor censitario
    e os pares de coordenadas (vertices) da geometria do setor censitário; 2) conjunto de dados 
    (dicionario) que contem o codigo do setor censitario e os registros da populacao nos setores 
    censitários
    
    Dados de saida: lista de pares de coordenadas (pontos) aleatorios
    """
    
    # Cria uma lista para guardar pontos
    pontos_aleatorios = []

    # Para setor censitario
    for codigo in codigos_e_populacao:
    
        # Cria uma lista com a quantidade de habitantes no setor
        try:
            populacao = range(int(codigos_e_populacao[codigo]))
        except:
            populacao = range(0)
    
        # Para cada habitante no setor
        for pessoa in populacao:
        
            # Cria um ponto aleatorio dentro do setor
            ponto = ponto_unico(Polygon(codigos_e_geometrias[codigo]))
            x,y = ponto.x, ponto.y
        
            # Guarda o ponto aleatorio gerado
            pontos_aleatorios.append([x,y])
    
    # Retorna a lista  de pontos aleatorios gerados
    return pontos_aleatorios
