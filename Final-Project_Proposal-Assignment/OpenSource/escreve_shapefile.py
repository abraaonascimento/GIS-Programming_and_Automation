import shapefile

def pontos(nome_do_shapefile, lista_pontos):
    """
    A funcao escreve_shapefile_ponto escreve um arquivo shapefile de pontos
    
    Dados de entrada: 1) nome do arquivo; 2) lista de coordenadas (latitute e longitude) dos pontos
    
    Dados de saida: arquivo shapefile de pontos  
    """
    # Escreve o arquivo shapefile
    novo_shapefile = shapefile.Writer(shapefile.POINT)

    # Adiciona um campo no shapefile
    novo_shapefile.field(nome_do_shapefile)
    
    # Para cada ponto na lista de pontos
    for ponto in lista_pontos: 
        
        # Adiciona um ponto no shapefile com o registro 'pessoa'
        novo_shapefile.point(float(ponto[0]), float(ponto[1]))
        novo_shapefile.record('pessoa')

    # Salva todas as edicoes no shapefile
    novo_shapefile.save('C:\\learnPython\\Projects\\dotMaps\\' + nome_do_shapefile + '.shp')
    
    ### Criando o arquivo projecao geografica ###
    
    # Dados do sistema geodesico de referencia
    epsg = 'GEOGCS["WGS 84",'
    epsg += 'DATUM["WGS_1984",'
    epsg += 'SPHEROID["WGS 84",6378137,298.257223563]]'
    epsg += ',PRIMEM["Greenwich",0],'
    epsg += 'UNIT["degree",0.0174532925199433]]'
   
    # Cria um novo arquivo de projecao geografica 
    prj = open('C:\\learnPython\\Projects\\dotMaps\\' + nome_do_shapefile + '.prj', "w")
    
    # Escreve os dados do sitema geodesico de refenrencia
    prj.write(epsg)
    prj.close()
