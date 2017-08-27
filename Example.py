import MtPy as mt
import sympy as sp

x = sp.Symbol('x')

A = mt.MtPy([x,2],[3,4])
B = mt.MtPy([2,4],[6,-3.0])
xx = mt.MtPy([1],[3])
C = mt.MtPy([2,4,1],[6,-3.0, 3])
y = mt.MtPy([1],[3],[5])
yt = mt.MtPy([1,3])

print mt.sin(A)
print xx - A
print A*x
print B*B
print C*y
print yt*C

A = mt.MtPy([x,2],[3,4])
print A
print mt.sin(A)
print A
print A.sin()
print A

A = mt.MtPy([x, x**2],[sp.sin(x), 3/2.0])
print A
print mt.sin(A)

'''
print A
print A.size()
B = mt.MtPy(1)
print B.size()

print type(B)
print mt.zeros(2,2)'''