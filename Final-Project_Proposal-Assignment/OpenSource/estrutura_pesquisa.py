import csv
import numpy as np

def demografica(nome_pesquisa):

    pesquisa_censo = open(nome_pesquisa)

    pesquisa_censo_csv = csv.reader(pesquisa_censo, delimiter=";")

    pesquisa_censo_l = list(pesquisa_censo_csv)
    pesquisa_censo_l = np.array(pesquisa_censo_l)
    
    return pesquisa_censo_l
