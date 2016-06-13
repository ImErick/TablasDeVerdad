#!/usr/bin/env python
import pyparsing
from aenum import Enum
import sys


class Type(Enum):
    """implementando Enum"""

    leftparentheses = 0
    rightparentheses = 1
    operator = 2
    empty = 3
    operand = 4

OPERADORES = {  # operando disponibles
    "+": "disyuncion",
    "&": "conjuncion",
    ">": "implicacion",
    "!": "negacion",
}


def negacion(p):
    """negacion se utiliza con simbolo !"""
    return not p


def conjuncion(p, q):
    """conjuncion se utiliza con simbolo &"""
    return (p and q)


def disyuncion(p, q):
    """disyuncion se utiliza con simbolo +"""
    return (p or q)


def implicacion(p, q):
    """condicional se utiliza con simbolo >: ->"""
    if (p == 1 and q == 0):
        return 0
    else:
        return 1


def tipoDeTablaDeVerdad(booleano):
    """define que tipo de proposicion logica es de acuerdo al resultado"""
    if all(item is True for item in booleano):
        print "es tautologia"
    elif all(item is False for item in booleano):
        print "es contradiccion"
    else:
        print "es contingencia"


def operadorATexto(string):
    """validando"""
    if string not in OPERADORES:
        sys.exit("Operador desconocido: " + string)
    return OPERADORES[string]


def tipoDeDato(string):
    """tipo de dato"""
    if string == '(':
        return Type.leftparentheses
    elif string == ')':
        return Type.rightparentheses
    elif string in OPERADORES:
        return Type.operator
    elif string == ' ':
        return Type.empty
    else:
        return Type.operand


def deInfijaAPrefija(expresion):
    """analiza la entrada que hizo el usuario, es un string"""
    stack = []
    while expresion:
        token = expresion.pop()
        category = tipoDeDato(token)

        if category == Type.operand:
            stack.append(token)
        elif category == Type.operator:
            stack.append(
                (operadorATexto(token),
                    stack.pop(), deInfijaAPrefija(expresion)))
        elif category == Type.leftparentheses:
            stack.append(deInfijaAPrefija(expresion))
        elif category == Type.rightparentheses:
            return stack.pop()
        elif category == Type.empty:
            continue
    return stack.pop()


def procesaPrefija(lista):
    """recibe la tupla en infija, de manera recursiva la recorre y procesa"""
    resultado = []
    print lista
    for token in lista:
        if isinstance(token, list) or isinstance(token, tuple):
            procesaPrefija(list(token))
        else:
            if token == "disyuncion":
                for lista[1] in range(2):
                    for lista[2] in range(2):
                        print bool(disyuncion(lista[1], lista[2]))
                        resultado.append(bool(disyuncion(lista[1], lista[2])))
                print tipoDeTablaDeVerdad(resultado)
            elif token == "conjuncion":
                for lista[1] in range(2):
                    for lista[2] in range(2):
                        print bool(conjuncion(lista[1], lista[2]))
                        resultado.append(bool(conjuncion(lista[1], lista[2])))
                print tipoDeTablaDeVerdad(resultado)
            elif token == "implicacion":
                for lista[1] in range(2):
                    for lista[2] in range(2):
                        print bool(implicacion(lista[1], lista[2]))
                        resultado.append(bool(implicacion(lista[1], lista[2])))
                print tipoDeTablaDeVerdad(resultado)


def main():
    """main del programa"""
    # expresion que valida que solo acepte numeros y los operadoress
    contenido = (pyparsing.Word(pyparsing.alphas) | '&' | '!' | '>' | '+')
    # expresion que valida que tenga parentesis y que cierren
    parentesis = pyparsing.nestedExpr('(', ')', content=contenido)

    try:
        entrada = raw_input("ingresa una formula bien formada: ")
        parentesis.parseString(entrada)  # analizando ando
        # devuelve la entrada en forma prefija
        prefija = deInfijaAPrefija(list(entrada[::-1]))
        print prefija
        procesaPrefija(list(prefija))
    except:
        print "hubo un error, probablemente se te paso un parentesis"


main()
