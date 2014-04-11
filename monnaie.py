#! /usr/bin/python
# -*- coding:utf8 -*-

"""
    monnaie.py
    Par Guillaume Lahaie
    LAHG04077707
    Dernière mise à jour: 10 avril 2014

    Implémentation de l'algorithme de monnaie
"""

import sys


def afficherC(L, P):
    C = [-1]*(L+1)
    for j in range(0, len(P)):
        C[0] = 0
        for i in range(1, L+1):
            min = sys.maxint
            for k in range(0, j+1):
                if P[k] <= i:
                    temp = 1 + C[i-P[k]]
                    if temp < min:
                        min = temp
            C[i] = min
        #On imprime la ligne
        print reduce(lambda x, y: x + " " + y, map(lambda x: str(x) + " ", C))

        
