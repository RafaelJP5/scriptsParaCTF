# -*- coding: utf-8 -*-
#@author: Rafa3la

def contaChrMono(M:str, alf:str = "abcdefghijklmnopqrstuvwxyz"):
    M = M.upper()
    alf = alf.upper()
    analise = {}
    for l in M:
        if ord(l) != 32:
            if not(l in analise):
                analise[l] = 0
            
            analise[l] +=1
        
    return analise

def contaChrPoli(M:str,K:int, alf:str = "abcdefghijklmnopqrstuvwxyz"):
    M = M.upper()
    alf = alf.upper()
    analise = [{} for i in range(K)]
    contador = 0
    for l in M:
        if ord(l) != 32:
            if not(l in analise[contador]):
                analise[contador][l] = 0
            
            analise[contador][l] += 1
            contador = contador + 1 if contador < K-1 else 0
    
    return analise