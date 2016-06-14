import numpy as np

class censo_demografico(object):

    def __init__(self, pesquisa_censo):
        self.pesquisa_censo = np.array(pesquisa_censo)
        self.id = self.pesquisa_censo[0]
        self.id_setor = self.pesquisa_censo[:,0]
        
        self.responsavel = "Instituto Brasileiro de Geografia e Estatistica"
        self.nome = "Censo Demografico"
        self.data = "2010"
        
        self.populacao_branca   = self.pesquisa_censo[:,3]
        self.populacao_preta    = self.pesquisa_censo[:,4]
        self.populacao_amarela  = self.pesquisa_censo[:,5]
        self.populacao_parda    = self.pesquisa_censo[:,6]
        self.populacao_indigena = self.pesquisa_censo[:,7]

    def responsavel(self):
        return self.responsavel

    def nome(self):
        return self.nome

    def data(self):
        return self.data
    
    def indice(self):
        return self.id

    def id_setor(self):
        return self.id_setor

    def populacao_branca(self):
        return self.populacao_branca  # V002 -Pessoas Residentes e cor ou raça - branca

    def populacao_preta(self):
        return self.populacao_preta  # V003 Pessoas Residentes e cor ou raça - preta

    def populacao_amarela(self):
        return self.populacao_amarela  # V004 Pessoas Residentes e cor ou raça - amarela

    def populacao_parda(self):
        return self.populacao_parda  # V005 Pessoas Residentes e cor ou raça - parda

    def populacao_indigena(self):
        return self.populacao_indigena  # V006 Pessoas Residentes e cor ou raça - indigena

    def total_registro(self):
        return len(self.pesquisa_censo)
