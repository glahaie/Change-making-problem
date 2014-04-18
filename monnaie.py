#! /usr/bin/python
# -*- coding:utf8 -*-

"""
    monnaie.py
    Par Guillaume Lahaie
    LAHG04077707
    Dernière mise à jour: 17 avril 2014

    Implémentation de l'algorithme de monnaie. Pour le moment je suppose
    qu'il est possible de rendre la monnaie pour tous les montants possibles
    il faudrait trouver traiter le cas où il n'est pas possible de rendre
    la monnaie
"""

import sys

def afficherC(L, P):
    """
        Affiche toutes les lignes de l'algorithme de programmation dynamique permettant
        de trouver le nombre de pièces optimales à rendre pour L. Si aucune solution
        n'est possible, la valeur -1 est affichée.
    """
    C = [sys.maxint]*(L+1)
    for j in range(0, len(P)):
        C[0] = 0
        for i in range(1, L+1):
            if P[j] <= i:
                C[i] = min(C[i], 1+ C[i-P[j]])

        #On imprime la ligne
        print reduce(lambda x, y: x + " "+y,
                     map(lambda x: "{"+str(x)+":3}",
                         range(0, len(C)))).format(*
                                 map(lambda x: -1 if x == sys.maxint else x, C)).strip()

def calculerC(M, P):
    """On retourne la dernière ligne de C pour la plus grande valeur de
       contenue dans M. Si la valeur de C est -1, il n'est pas possible de rendre
       la monnaie exacte.
    """
    maxChange = max(M)
    C = [sys.maxint]*(maxChange+1)
    for j in range(0, len(P)):
        C[0] = 0
        for i in range(1, maxChange+1):
            if P[j] <= i:
                C[i] = min(C[i], 1+ C[i-P[j]])

    return map(lambda x: -1 if x == sys.maxint else x, C)


def lireFichier(nom_fichier):
    """Lit le fichier à traiter: la première contient le nombre de valeurs de
       pièces de monnaie, ensuite les valeurs des pièces de monnaie, le
       nombre de valeurs à calculer, finalement les valeurs de monnaie à rendre
    """
    with open(nom_fichier, "r") as f:
        no_pieces = int(f.readline().strip())
        P = map(lambda x: int(x),
                filter(lambda x: x != "",
                       map(lambda x: x.strip(),
                           f.readline().strip().split(" "))))

        assert (len(P) == no_pieces),\
                "Erreur de dimensions dans le fichier " + nom_fichier

        no_monnaie = int(f.readline().strip())
        Monnaies = map(lambda x: int(x),
                filter(lambda x: x != "",
                       map(lambda x: x.strip(),
                           f.readline().strip().split(" "))))

        assert (len(Monnaies) == no_monnaie),\
                "Erreur de dimensions dans le fichier " + nom_fichier

    return P, Monnaies

def trouverMonnaieOptimale(C, monnaie, P):
    """Retourne un tableau contenant, en ordre décroissant, le nombre de
       pièces de chaque dénomination de la solution optimale pour monnaie.
       S'il est impossible de rendre la monnaie exacte, on retourne un
       tableau contenant des nombres négatifs.

       On assume ici que monnaie <= L.
    """

    S = [0]*len(P)
    if C[monnaie] < 0:
        return map(lambda x: -1, S)
    i = 0
    n = len(P)
    while monnaie > 0:
        if (monnaie >= P[n-1-i]) and (C[monnaie] - 1==  C[monnaie - P[n-1-i]] ):
            monnaie = monnaie - P[n-1-i]
            S[i] += 1
        else:
            i += 1
    return S



def main():

    fichier_defaut = "monnaie.txt"
    if len(sys.argv) > 1:
        fichier_defaut = sys.argv[1]

    P, Monnaies = lireFichier(fichier_defaut)

    #On imprime pour L = 20
    print reduce(lambda x, y: str(x) + " " + str(y), P)
    afficherC(20, P)

    C = calculerC(Monnaies, P)

    print "\nMontant: nombre de pièces en ordre décroissant de valeur"
    for i in Monnaies:
        S = trouverMonnaieOptimale(C, i, P)
        if S[0] < 0:
            print str(i) + " : Aucune solution possible"
        else:
            print str(i) + " : " + reduce(lambda x, y: str(x) + " " + str(y), S)

if __name__ == "__main__":
        main()
