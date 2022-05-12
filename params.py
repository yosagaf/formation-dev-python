#!/usr/bin/env/python3


def square(x):
    if type(x) == int or type(x) == float:
        return x**2
    else:
        return None


nbre = input("Entrer votre nombre : ")
square(nbre)
