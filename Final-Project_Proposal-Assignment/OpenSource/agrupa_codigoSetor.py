import shapefile

def e_geometria(nome_shapefile):
    """ 
    A funcao agrupa_codigo_e_setor junta cada codigo de setor censitario dentro de um arquivo 
    shapefile com os pares de coordenadas que constroem a geometria do setor censitario
    
    Dados de entrada: arquivo shapefile de setores censitarios
    
    Dados de saida: conjunto de dados (dicionario) que contem o codigo do setor censitario
    e os pares de coordenadas (vertices) da geometria do setor censitário. 
    """
    
    # Le o arquivo shapefile
    arquivo_shp = shapefile.Reader(nome_shapefile)
    
    # Recebe todas as geometrias do shapefile 
    geometrias = arquivo_shp.shapes()
    
    # Recebe todos os atributos do shapefile
    atributos = arquivo_shp.records()
    
    # Cria um conjunto para guardar o codigo e a geometria de um setor censitario
    codigo_e_geometria = {}
    
    # Cria um conjunto para guardar todos os codigos e todas as geometrias dos setores censitarios
    todos_codigos_e_geometrias = {}

    # Para cada geometria do shapefile
    for indice, geometria in enumerate(geometrias): 
        
        # Recebe o codigo e os pares de coordenadas da geometria do setor
        codigo_e_geometria[str(atributos[indice][1])] = geometria.points
        
        # Guarda o codigo e os pares de coordenadas da geometria do setor
        todos_codigos_e_geometrias.update(codigo_e_geometria)
    
    # Retorna todos os codigos e todos os pares de coordenadas das geometrias dos setores censitarios 
    return todos_codigos_e_geometrias
    
def e_populacao(codigoSetor, populacao):
    """
    A funcao agrupa_codigo_e_populacao junta cada codigo de setor censitario com o registro de papulacao
    (numero de pessoas) no setor censitario. 
    
    Dados de entrada: 1) lista de codigos de setores censitarios; 2) lista de registros de populacao nos 
    setores censitarios
    
    Dados de saida: conjunto de dados (dicionario) que contem o codigo do setor censitario e os registros 
    da populacao nos setores censitários
    """
    
    # Cria um conjunto para guardar o codigo e o registro de populacao no setor censitarios
    registro_populacao = {}
    
    # Cria um conjunto para guardar todos os codigos e todos os registros de populacao nos setores censitarios
    registros_populacao = {}
    
    # Pula a primeira linha (o cabeçalho) da lista de setores censitarios
    codigos = codigoSetor[1:] 
    
    # Pula a primeira linha (o cabeçalho) da lista de registros de populacao nos setores censitarios
    populacao = populacao[1:]
    
    # Para cada codigo na lista de setores censitarios
    for indice, codigo in enumerate(codigos):
        
        # Recebe o codigo e o registro de populacao no setor
        registro_populacao[codigo] = populacao[indice]
        
        # Guarda o codigo e o registro de populacao no setor
        registros_populacao.update(registro_populacao)
       
    # Retorna todos os codigos e todos os registros de populaacao nos setores censitarios 
    return registros_populacao
