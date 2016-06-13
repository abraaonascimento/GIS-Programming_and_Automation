import numpy as np

class censo_demografico(object):

    def __init__(self, pesquisa_censo):
        self.pesquisa_censo = pesquisa_censo

    def responsavel(self):
        self.responsavel = "Instituto Brasileiro de Geografia e Estatistica"
        return self.responsavel

    def nome(self):
        self.nome = "Censo Demografico"
        return self.nome

    def data(self):
        self.data = "2010"
        return self.data
    
    def indice(self):
        self.id = self.pesquisa_censo[0]
        return self.id

    def id_setor(self):
        self.id_setor = np.array(self.pesquisa_censo)
        self.id_setor = self.id_setor[:,0]
        return self.id_setor

    def populacao_branca(self):
        self.populacao_branca = np.array(self.pesquisa_censo)
        self.populacao_branca = self.populacao_branca[:,3] # V002 -Pessoas Residentes e cor ou raça - branca
        return self.populacao_branca

    def populacao_preta(self):
        self.populacao_preta = np.array(self.pesquisa_censo)
        self.populacao_preta = self.populacao_preta[:,4] # V003 Pessoas Residentes e cor ou raça - preta                                         
        return self.populacao_preta

    def populacao_amarela(self):
        self.populacao_amarela = np.array(self.pesquisa_censo)
        self.populacao_amarela = self.populacao_amarela[:,5] # V004 Pessoas Residentes e cor ou raça - amarela
        return self.populacao_amarela

    def populacao_parda(self):
        self.populacao_parda = np.array(self.pesquisa_censo)
        self.populacao_parda = self.populacao_parda[:,6] # V005 Pessoas Residentes e cor ou raça - parda
        return self.populacao_parda

    def populacao_indigena(self):
        self.populacao_indigena = np.array(self.pesquisa_censo)
        self.populacao_indigena = self.populacao_indigena[:,7] # V006 Pessoas Residentes e cor ou raça - indigena                                                                 
        return self.populacao_indigena

    def total_registro(self):
        self.total_registro = len(self.pesquisa_censo)
        return self.total_registro
