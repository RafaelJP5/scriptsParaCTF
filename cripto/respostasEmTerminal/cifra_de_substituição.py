# -*- coding: utf-8 -*-
#@author: Rafa3la

def encriptarSubs(M, K, alf = "abcdefghijklmnopqrstuvwxyz"):
    K = list(K.upper())
    M = M.upper()
    alf = alf.upper()
    C = ""

    for l in M:
        i = alf.find(l)
        C += K[i]

    print(M+"\n"+C)
    return C

def decriptarSubs(C, K, alf = "abcdefghijklmnopqrstuvwxyz"):
    K = list(K.upper())
    alf = alf.upper()
    C = C.upper()
    M = ""

    for l in C:
        i = alf.find(l)
        if i > len(K)-1:
            M += "_"
        else:
            M += K[i]

    print(C+"\n"+M)
    return M

