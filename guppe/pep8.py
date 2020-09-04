"""PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP* é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classe;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass



[2] - Utilize nomes em minusculo, separados poor underline para funções e variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5


[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('Tem')


[4] - linhas em branco
-Separar funções e definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma linha em branco;


class Classe:
    pass


[5] - Imports

#import Errado
import sys, os

#import Certo

#import sys
#import os

#não há problemas em utilzar:
#from types import StringType, ListType
#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

Imports devem ser colocados sempre no topo do arquivo, logo depois de quisquer comentários ou docstring
antes de constantes ou variáveis globais


[6] - Espaços em expressões e instruções


[7] - Termine sempre a instrução com uma nova linha
"""












