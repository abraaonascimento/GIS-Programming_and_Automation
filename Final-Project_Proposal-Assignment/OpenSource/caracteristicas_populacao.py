def etnico_racial(questionario):
    
    caracteristicas = []
    
    populacao_amarela = questionario.populacao_amarela()
    caracteristicas.append(['populacao_amarela', populacao_amarela])
    
    populacao_branca = questionario.populacao_branca()
    caracteristicas.append(['populacao_branca',populacao_branca])
    
    populacao_indigena = questionario.populacao_indigena()
    caracteristicas.append(['populacao_indigena', populacao_indigena])
    
    populacao_parda = questionario.populacao_parda()
    caracteristicas.append(['populacao_parda', populacao_parda])
    
    populacao_preta = questionario.populacao_preta()
    caracteristicas.append(['populacao_preta', populacao_preta])
    
    return caracteristicas 
