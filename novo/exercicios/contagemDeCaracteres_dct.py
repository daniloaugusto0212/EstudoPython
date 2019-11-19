def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('Danilo')
    {'a': 1, 'd': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1}
    >>> contar_caracteres('banana')
    {'a':3, 'b':1, 'n':2}

    :param s:
    :return:
    """


    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
        

    return  resultado

if __name__ == '__main__':
    contar_caracteres('Danilo')
    print()
    contar_caracteres('banana')
