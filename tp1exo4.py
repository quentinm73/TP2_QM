Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nb_minu=input()
2790
>>> date = (nb_minu/60)/24
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    date = (nb_minu/60)/24
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> nb_minu=int(input())
27360
>>> date = (nb_minu/60)/24
>>> print(date)
19.0
>>> print('nombre de jour :',date)
nombre de jour : 19.0
>>> 