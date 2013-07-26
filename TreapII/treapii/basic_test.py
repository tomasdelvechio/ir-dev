#!/usr/bin/python
# -*- coding: utf-8 -*-

docids = [4,9,13,14,15,22,27,30,35,37,39,44]
freqs = [6,2,14,1,1,2,1,24,6,1,2,3]

from treap.treap import treap

t = treap()

for i in xrange(len(docids)):
    t.insert(docids[i], None, freqs[i])

# Recorrido en Pre Orden
def PreOrder(node):
    if node == None:
        return
    print node.key
    PreOrder(node.left)
    PreOrder(node.right)

def GenerarBP(node):
    # Genera el Arbol de parentesis balanceados asociado a la estructura (Seccion 4.3.1)
    # La estructura de recorrido es basicamente InOrder
    if node == None:
        return
    print '(',
    GenerarBP(node.left)
    print ')',
    GenerarBP(node.right)

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

objective = '( ( ( ( ) ( ) ) ( ( ) ( ) ) ( ) ) ( ) ( ( ( ) ) ) )'
print objective
print '(', # Es la raiz falsa
GenerarBP(t.root)
print ')' # Es la raiz falsa


