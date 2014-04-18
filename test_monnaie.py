#! /usr/bin/python
# -*- coding:utf8 -*-

"""
    test_monnaie.py
    Teste les fonctions de de monnaie.py
"""

from monnaie import *
import unittest
from StringIO import StringIO
import sys

class TestCalculerC(unittest.TestCase):

    def test_cas_base(self):
        self.p = [1, 5, 10, 25]
        self.l = 20
        self.c = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 2]
        self.assertSequenceEqual(self.c, calculerC(self.l, self.p))

    def test_cas_impossible(self):
        self.p = [2, 5, 10, 25]
        self.l = 20
        self.c = [0, -1,1, -1, 2, 1, 3, 2, 4, 3, 1, 4, 2, 5, 3, 2, 4, 3, 5, 4, 2]
        self.assertSequenceEqual(self.c, calculerC(self.l, self.p))

    def test_cas_pas_glouton(self):
        self.p = [1, 5, 11, 25]
        self.l = 15
        self.c = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 3]
        self.assertSequenceEqual(self.c, calculerC(self.l, self.p))


class TestAfficherC(unittest.TestCase):

    def test_base(self):
        save_stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        self.l = 10
        self.p = [1, 5, 10, 25]
        afficherC(self.l, self.p)
        output = out.getvalue().strip()
        result= ("0   1   2   3   4   5   6   7   8   9  10\n"
                 "0   1   2   3   4   1   2   3   4   5   2\n"
                 "0   1   2   3   4   1   2   3   4   5   1\n"
                 "0   1   2   3   4   1   2   3   4   5   1")
        self.assertEquals(result,output)
        sys.stdout = save_stdout

    def test_sans_reponse(self):
        save_stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        self.l = 10
        self.p = [2, 5, 10, 25]
        afficherC(self.l, self.p)
        output = out.getvalue().strip()
        result= ("0  -1   1  -1   2  -1   3  -1   4  -1   5\n"
                 "0  -1   1  -1   2   1   3   2   4   3   2\n"
                 "0  -1   1  -1   2   1   3   2   4   3   1\n"
                 "0  -1   1  -1   2   1   3   2   4   3   1")
        self.assertEquals(result,output)
        sys.stdout = save_stdout

class TestTrouverMonnaieOptimale(unittest.TestCase):

    def test_erreur(self):
        self.p = [2, 5, 10, 25]
        self.l = 3
        self.c = [0, -1,1, -1, 2, 1, 3, 2, 4, 3, 1, 4, 2, 5, 3, 2, 4, 3, 5, 4, 2]
        self.assertSequenceEqual([-1,-1,-1,-1], trouverMonnaieOptimale(self.c, self.l, self.p))

    def test_base(self):
        self.p = [1, 5, 10, 25]
        self.l = 19
        self.c = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 2]
        self.assertSequenceEqual([0,1,1,4], trouverMonnaieOptimale(self.c, self.l, self.p))

    def test_glouton_pas_optimal(self):
        self.p = [1, 5, 11, 25]
        self.l = 15
        self.c = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 3]
        self.assertSequenceEqual([0,0,3,0], trouverMonnaieOptimale(self.c, self.l, self.p))


if __name__ == "__main__":
    unittest.main()
