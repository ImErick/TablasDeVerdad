#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import main


def menu():
    """Funcion que limpia la pantalla y muestra nuevamente el menu"""
    os.system('clear')
    print "Selecciona una opción"
    print "\t1 - agrega premisa"
    print "\t2 - agrega conclusion"
    print "\t9 - salir"


def conjuntaPremisas(lista):
    """hace la tabla de verdad de todas las premisas"""
    resultados = []
    for elemento in lista:
        resultados.append(main.tablaDeVerdad(elemento))
    print resultados  # me quede aqui, salvar la variable lista del modulo


def principal():
    """main del programa"""
    lista = []
    while True:
        menu()
        opcionMenu = raw_input("inserta un numero valor >> ")
        if opcionMenu == "1":
            print ""
            item = raw_input("Agrega una premisa valida: ")
            lista.append(item)
        elif opcionMenu == "2":
            print ""
            item = raw_input("Agrega un la conclusion: ")
            lista.append(item)
        elif opcionMenu == "9":
            break
        else:
            print ""
            raw_input("No has pulsado ninguna opción correcta...")
    print lista
    conjuntaPremisas(lista)


principal()
