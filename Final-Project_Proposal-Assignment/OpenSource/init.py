import sys
sys.path.append('C:\\Users\\Abraao\\Downloads\\dotmaps')

# Bibliotecas do Python
import csv
import operator

# Biblioteca de terceiros
import numpy as np

# Meus modulos
import agrupa_codigoSetor
import caracteristicas_populacao
import escreve_shapefile
import estrutura_pesquisa
import gera_geometria
import questionario

nome_shapefile = "C:\\learnPython\\Projects\\dotMaps\\geographicData\\dataSetorTest.shp"
nome_pesquisa = "C:\\learnPython\\Projects\\dotMaps\\demographicData\\dataSetorTest.csv"

pesquisa_demografica = estrutura_pesquisa.demografica(nome_pesquisa)

q = questionario.censo_demografico(pesquisa_demografica)

codigo_setor = q.id_setor()

#
caracteristicas_populacao = caracteristicas_populacao.etnico_racial(q)
    
#
codigos_e_geometrias = agrupa_codigoSetor.e_geometria(nome_shapefile)
    
#
for caracteristica in caracteristicas_populacao:
        
#
    codigo_populacao = agrupa_codigoSetor.e_populacao(codigo_setor, caracteristica[1])
        
#
    pontos_aleatorios = gera_geometria.multiplos_pontos(codigos_e_geometrias, codigo_populacao)        
#
    escreve_shapefile.pontos(caracteristica[0],pontos_aleatorios)
