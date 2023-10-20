Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nom="Milhau"
>>> prenom="Quentin"
>>> math=14
>>> anglais=16
>>> info=20
>>> promotion=20
>>> type(nom)
<class 'str'>
>>> type(prenom)
<class 'str'>
>>> type(math)
<class 'int'>
>>> type(anglais)
<class 'int'>
>>> type(info)
<class 'int'>
>>> promotion=2023
>>> type(promotion)
<class 'int'>
>>> moy=(math+anglais+info)/3
>>>  f"L'étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {moy}"
 
SyntaxError: unexpected indent
>>> f"L'étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {moy}"
"L'étudiant Milhau Quentin de la promotion 2023 a une moyenne de 16.666666666666668"
>>> 