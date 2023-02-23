# -*- coding: utf-8 -*-
#@author: Rafa3la

#Cifra de Cesar

#M - mensagem, k - chave
def encriptarCesa(M:str, K:int):
    M = M.upper()
    c = ""
    for l in M:
        if ord(l) != 32:
            ascL = ord(l)+K
            if ascL > 90:
                ascL = (ascL-64)%26 + 64
            c += chr(ascL)
        
        else:
            c+=l
    return c

def decriptarCesa(C:str, K:int):
    C = C.upper()
    m = ""
    for l in C:
        if ord(l) != 32:
            ascL = ord(l)-K
            if ascL < 65:
                ascL = abs(26-abs(ascL-64))+64
            m += chr(ascL)
        
        else:
            m+=l
    return m