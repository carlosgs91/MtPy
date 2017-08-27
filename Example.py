import MtPy as mt
import sympy as sp

x = sp.Symbol('x')

A = mt.MtPy([2,x],[3,3j])
print 'Generic matrix'
print 'A = mt.MtPy([2,x],[3,3j]) = \n' + str(A)
print 'A.type() = \n' + A.type()

print '\nPerforming a function such as sin() in a matrix finds sin() for each type'
B = mt.sin(A)
print 'B = mt.sin(A) = \n' + str(B)
print 'B.type() = \n' + B.type()

print '\nOperators work in the same manner by finding the method operator in each type'
C = A + mt.transpose(B)
print 'C = A + mt.transpose(B) = \n' + str(C)
print 'C.type() = \n' + C.type()

print '\nNo confussion with copies and references. Everything is a copy unless it is'
print 'is called from the object.'
D = mt.MtPy([1,2],[3,4])
print 'D = \n' + str(D)
print 'mt.transpose(D) = \n' + str(mt.transpose(D))
print 'mt.transpose(D)[0][0] = -1'
mt.transpose(D)[0][0] = -1
print 'Still D\nD = \n' + str(D)
print 'When called from its own, D.transpose()[0][0] = -1'
D.transpose()[0][0] = -1
print 'Now D is transposed and the element modified.\nD =\n' + str(D)
print 'Ideally copies should be implemented in a similar manner as Matlab. Every copy'
print 'should actually be a reference but when you try to modify it it becomes a copy.'

print '\nA wrapper would make functions work in matrices, for example'
print '\ndef myFunExample(x):'
print '    return 2*x + 1'
print '\nNow the wrapper calls the function trough _matFun_'
print 'def funExample(m, copy = True):'
print '    return _matFun_(\'MtFun\', \'myFunExample\', copy, m)'
E = mt.MtPy([1,2],[3,4])
print '\nE = mt.MtPy([1,2],[3,4]) = \n' + str(E)
print 'mt.myFunExample(E) = \n' + str(mt.myFunExample(E))

print '\nOf course all this should be optimized, using Numpy and others packages automatically'
print 'to perform operations when possible to gain speed and default to slow but working'
print 'solutions when needed such as when using symbolic variables.'