Change-making problem
===========

An implementation of the Dynamic programming algorithm for the
[Change-making problem](http://en.wikipedia.org/wiki/Change-making_problem).

With the result of the dynamic programming algorithm, a greedy algorithm is
implemented to find the best solution.

The application takes one optional argument: a file name containing the coins
and the change to calculate. The file must be in the form:

```
Number of coins
Values of coins
Number of values of change
Values of change
```

An example is:

```
4
1 5 10 25
3
30 85 123
```

If no argument is given, the application uses the file `monnaie.txt`. The latex
file contains an analysis of the complexity of the algorithms.

---

Problème du rendu de la monnaie.
===========

Algorithme glouton - problème de la monnaie, approche dynamique et gloutonne.
Le programme a été testé avec python 2.7.6 et pypy 2.2.1 sur linux, et sur les
serveurs malt et rayon1.

Pour tester le programme avec le fichier monnaie.txt: python monnaie.py. Pour
les tests unitaires: python test\_monnaie.py. Les tests requièrent python
2.7+ car j'utilise assertSequenceEqual.

 Il est possible d'entrer le nom d'un fichier en argument, alors ce fichier
sera considéré à la place de monnaie.txt.
