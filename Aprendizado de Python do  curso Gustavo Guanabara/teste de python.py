Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print7+4)
SyntaxError: unmatched ')'
print(7+4)
11
print('Olá mundo !')
Olá mundo !
print('Olá ',5)
Olá  5
nome = 'David'
idade = 21
peso = 74.8
print(nome, idade, peso)
David 21 74.8
nome = input('qual é o seu nome?)
             
SyntaxError: unterminated string literal (detected at line 1)
nome = input('qual é o seu nome?')
             
qual é o seu nome?
david
             
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    david
NameError: name 'david' is not defined
idade = input('quantos anos vc tem?')
             
quantos anos vc tem?21
quantos anos vc tem?21
             
SyntaxError: invalid syntax. Perhaps you forgot a comma?
peso = input('qual é o seu peso?')
             
qual é o seu peso? 44.5
print(nome,idade,peso)
             
 21  44.5
