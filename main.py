#!/usr/bin/env python
from itertools import product
import re


def canonica(expr):
    """Descripcion

    recibe la expresion booleana y hace la sustitucion de las variables y de
    los parentesis para poder manejarla mas facil, sustituyendo los OPERADORES
    ingresados por el usuario por operadores validos para hacer la operacion
    """
    OPERADORES = {
        '!': ' not ',   # negacion
        '+': ' or ',    # disyuncion
        '&': ' and ',   # conjuncion
        '-': '<=',      # implicacion
        '=': '==',      # doble implicacion
        '[': '(',
        ']': ')',
        '{': '(',
        '}': ')',
    }
    return re.sub('|'.join(re.escape(sym) for sym in OPERADORES.keys()),
                  lambda sym: OPERADORES[sym.group(0)],
                  expr).strip()


def validaResultado(lista):
    """Descripcion

    Recibe una lista y valida si es tautologia, contradiccion o contingencia
    """
    if all(item == 1 for item in lista):
        print "es tautologia"
    elif all(item == 0 for item in lista):
        print "es contradiccion"
    else:
        print "es contingencia"


def extrae_variables(expr):
    """Descripcion.

    recibe una expresion booleana y devuelve una lista con las varibles
    que se estan usando en la funcion, se valida usando una expresion regular
    donde solo acepta las letras del abecedario en mayusculas o minusculas
    """
    return sorted(set(re.findall(r'\b[A-Za-z]\b', expr)))


def tablaDeVerdad(expr):
    """recibe una expresion regular y crea la tabla"""
    expr = canonica(expr)
    vars = extrae_variables(expr)
    lista = []

    # header de la tabla
    print('\t'.join(vars + [expr]))

    # cuerpo de la tabla
    for vals in product(range(2), repeat=len(vars)):
        locals = dict(zip(vars, vals))
        result = eval(expr, locals)
        lista.append(result)
        print('\t'.join([str(v) for v in vals] +
                        [str(result).replace("True", "1")
                        if str(result) is "True"
                        else str(result).replace("False", "0")]))
    validaResultado(lista)
    return lista


def main():
    """funcion principal"""
    try:
        expresion = raw_input("ingresa una expresion valida: ")
        tablaDeVerdad(expresion)
    except:
        print "hubo un error, probablemente se te paso un parentesis"
main()
