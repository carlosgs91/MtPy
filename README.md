# MtPy
Just a quick (slow and hacky) code of what I would like to have when working with data in Python.

# Example
```
Generic matrix
A = mt.MtPy([2,x],[3,3j]) =
[2,   x]
[3,  3j]
A.type() =
[<type 'int'>,  <class 'sympy.core.symbol.Symbol'>]
[<type 'int'>,                    <type 'complex'>]

Performing a function such as sin() in a matrix finds sin() for each type
B = mt.sin(A) =
[0.909297426826,          sin(x)]
[ 0.14112000806,  10.0178749274j]
B.type() =
[<type 'float'>,               sin]
[<type 'float'>,  <type 'complex'>]

Operators work in the same manner by finding the method operator in each type
C = A + mt.transpose(B) =
[2.90929742683,  x + 0.141120008059867]
[   sin(x) + 3,         13.0178749274j]
C.type() =
[              <type 'float'>,  <class 'sympy.core.add.Add'>]
[<class 'sympy.core.add.Add'>,              <type 'complex'>]

No confussion with copies and references. Everything is a copy unless it is
is called from the object.
D =
[1,  2]
[3,  4]
mt.transpose(D) =
[1,  3]
[2,  4]
mt.transpose(D)[0][0] = -1
Still D
D =
[1,  2]
[3,  4]
When called from its own, D.transpose()[0][0] = -1
Now D is transposed and the element modified.
D =
[-1,  3]
[ 2,  4]
Ideally copies should be implemented in a similar manner as Matlab. Every copy
should actually be a reference but when you try to modify it it becomes a copy.

A wrapper would make functions work in matrices, for example

def myFunExample(x):
    return 2*x + 1

Now the wrapper calls the function trough _matFun_
def funExample(m, copy = True):
    return _matFun_('MtFun', 'myFunExample', copy, m)

E = mt.MtPy([1,2],[3,4]) =
[1,  2]
[3,  4]
mt.myFunExample(E) =
[3,  5]
[7,  9]

Of course all this should be optimized, using Numpy and others packages automatically
to perform operations when possible to gain speed and default to slow but working
solutions when needed such as when using symbolic variables.
```
