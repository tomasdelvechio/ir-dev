#!/usr/bin/python
# -*- coding: utf-8 -*-

docids = [4,9,13,14,15,22,27,30,35,37,39,44]
freqs = [6,2,14,1,1,2,1,24,6,1,2,3]

from treap.treap import treap

t = treap()

for i in xrange(len(docids)):
    t.insert(docids[i], None, freqs[i])

# Recorridos #
##############

# Recorrido en Pre Orden
def PreOrder(node):
    if node == None:
        return
    print node.key
    PreOrder(node.left)
    PreOrder(node.right)

# Recorrido en In Orden
def InOrder(node):
    if node == None:
        return
    InOrder(node.left)
    print node.key
    InOrder(node.right)

# Recorrido Pos Orden
def PosOrder(node):
    if node == None:
        return
    PosOrder(node.left)
    PosOrder(node.right)
    print node.key

# Representacion compacta de la topologia #
###########################################

def GenerarBP(node):
    # Genera el Arbol de parentesis balanceados asociado a la estructura (Seccion 4.3.1)
    # La estructura de recorrido es basicamente InOrder
    
    global topology # Permitimos que se edite la variable global
    
    if node == None:
        return
    topology += '('
    GenerarBP(node.left)
    topology += ')'
    GenerarBP(node.right)

# Otras funciones utiles #
##########################

# Devuelve el Id de documento representado por un nodo
def id(node):
    return node.key

# Devuelve la frecuencia de un nodo, que para el heap es la prioridad
def f(node):
    return node.priority

# Tests #
#########

objective = '(((()())(()())())()((())))'
print objective
topology = ""
GenerarBP(t.root)
topology = '(' + topology + ')' # Agregamos el fake root
print topology


