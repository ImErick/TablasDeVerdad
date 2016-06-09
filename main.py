#!/usr/bin/env python
import pyparsing


def negacion(p):
    """negacion se utiliza con simbolo !"""
    return not p


def conjuncion(p, q):
    """conjuncion se utiliza con simbolo &"""
    return (p and q)


def disyuncion(p, q):
    """disyuncion se utiliza con simbolo +"""
    return (p or q)


def condicional(p, q):
    """condicional se utiliza con simbolo >"""
    if (p == 1 and q == 0):
        return 0
    else:
        return 1


def hazTablaDeVerdad():
    """aqui voy a tratar de hacer la tabla de verdad"""
    pass


def analizaEntrada(lista):
    """analiza la entrada que hizo el usuario, recibe una lista"""
    string = ''.join(str(e) for e in lista)  # me quede aqui, no se que hacer con la lista recursiva
    print string.replace("+", "and")


def main():
    """main del programa"""
    contenido = (pyparsing.Word(pyparsing.alphanums) | '&' | '!' | '>' | '+')
    parentesis = pyparsing.nestedExpr('(', ')', content=contenido)
    entrada = raw_input("ingresa una formula bien formada: ")
    resultado = parentesis.parseString(entrada)
    analizaEntrada(resultado.asList())


main()
