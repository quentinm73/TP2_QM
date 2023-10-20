Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> jour=input()
20
>>> heure=input()
10
>>> minute=input()
0
>>> nb_min= (jour-1)*(60*24) + (heure*60) + minute
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    nb_min= (jour-1)*(60*24) + (heure*60) + minute
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> jour=int(input())
20
>>> heure=int(input())
10
>>> minute=int(input())
0
>>> nb_min= (jour-1)*(60*24) + (heure*60) + minute
>>> print(nb_min)
27960
>>> 