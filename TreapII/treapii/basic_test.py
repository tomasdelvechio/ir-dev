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
def _id(node):
    return node.key

# Devuelve la frecuencia de un nodo, que para el heap es la prioridad
def f(node):
    return node.priority

# Arbol de codificacion diferencial #
#####################################

# Dado un treap debemos poder calcular su Treap diferencial (Differenttially Encoded Treap).

def GenerarDET(node, node_parent):
    """ Presupone t cargado y det vacio inicialmente """
    #~ global t
    #~ global det
    
    if node == None:
        return
    GenerarDET(node.left, node)
    # si es el nodo raiz
    if node_parent == None:
        diff_ids.append(_id(node))
        diff_freqs.append(f(node))
    else:
        if(_id(node) > _id(node_parent)):
            diff_ids.append(_id(node) - _id(node_parent))
        else:
            diff_ids.append(_id(node_parent) - _id(node))
        diff_freqs.append(f(node_parent) - f(node))
    GenerarDET(node.right, node)

# DACs y VBEncoding #
#####################

#~ def VBcode(num, b=3):
    #~ bin_num = bin(num)
    #~ bin_num = bin_num[2:]

def VBEncodeNumber(n):
    _bytes = []
    while True:
        _bytes.insert(0,n % 128)
        if n < 128:
            break
        n = n / 128
    _bytes[len(_bytes)-1] += 128
    return _bytes

def VBEncode(numbers):
    bytestream = []
    for n in numbers:
        _bytes = VBEncodeNumber(n)
        bytestream = bytestream + _bytes
    return bytestream

def VBDecode(bytestream):
    numbers = []
    n = 0
    for i in xrange(len(bytestream)):
        if bytestream[i] < 128:
            n = 128 * n + bytestream[i]
        else:
            n = 128 * n + (bytestream[i] - 128)
            numbers.append(n)
            n = 0
    return numbers

# Tests #
#########

### Para generar el BP del Treap

#~ objective = '(((()())(()())())()((())))'
#~ print objective
#~ topology = ""
#~ GenerarBP(t.root)
#~ topology = '(' + topology + ')' # Agregamos el fake root
#~ print topology

### Para generar el DET

#~ diff_ids = []
#~ diff_freqs = []
#~ GenerarDET(t.root, None)
#~ print diff_ids
#~ print diff_freqs

### VBEncode tests

posting = [123,231,344,543,643,788,888,889,900,1202]
print posting
encoded = VBEncode(posting)
print encoded
decoded = VBDecode(encoded)
print decoded
