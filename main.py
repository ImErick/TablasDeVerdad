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


def condicional(p, q):
    """condicional se utiliza con simbolo >: ->"""
    if (p == 1 and q == 0):
        return 0
    else:
        return 1


def hazTablaDeVerdad():
    """aqui voy a tratar de hacer la tabla de verdad"""
    pass


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
            stack.append((operadorATexto(token), stack.pop(), deInfijaAPrefija(expresion)))
        elif category == Type.leftparentheses:
            stack.append(deInfijaAPrefija(expresion))
        elif category == Type.rightparentheses:
            return stack.pop()
        elif category == Type.empty:
            continue
    return stack.pop()


def main():
    """main del programa"""
    # expresion que valida que solo acepte numeros y los operadoress
    contenido = (pyparsing.Word(pyparsing.alphas) | '&' | '!' | '>' | '+')
    # expresion que valida que tenga parentesis y que cierren
    parentesis = pyparsing.nestedExpr('(', ')', content=contenido)

    entrada = raw_input("ingresa una formula bien formada: ")
    parentesis.parseString(entrada)  # analizando ando
    # devuelve la entrada en forma prefija
    prefija = deInfijaAPrefija(list(entrada[::-1]))
    print prefija


main()
