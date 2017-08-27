import MtPy as mp

def _matFun_(baseModule, name, copy, *args):
	rows = 0
	cols = 0
	for arg in args:
		if isinstance(arg, mp.MtPy):
			selfM = arg
			rows = arg.rows()
			cols = arg.cols()
			break

	if copy:
		m = zeros(rows, cols)
	else:
		m = selfM
	for rowId in range(0, rows):
		for colId in range(0, cols):
			newArgs = ()
			for arg in args:
				try:
					newArgs += (arg[rowId][colId],)
				except TypeError as e:
					newArgs += (arg,)
			
			if len(args) == 1:
				newArgs = newArgs[0]

			v = None
			if baseModule == 'operator':
				f0 = _getFun_(baseModule, name, newArgs[0])
				f1 = _getFun_(baseModule, '__r'+name.split('__')[1]+'__', newArgs[1])
				v = f0(newArgs[1])
				if v == NotImplemented:
					v = f1(newArgs[0])
			else:
				if isinstance(baseModule, list) == False:
					baseModule = [baseModule]
				for bm in baseModule:
					try:
						f = _getFun_(bm, name, newArgs)
						v = f(newArgs)
						break
					except TypeError as e:
						pass
			if v == None:
				raise TypeError(name + 'not implemented for the type given')

			m[rowId][colId] = v
	return m

def _getFun_(baseModule, name, arg):
	if baseModule == 'operator':
		return getattr(arg,name)

	try:
		subModuleName = (arg).__module__ #str(type(arg)).split('\'')[1]
		moduleName = (arg).__module__.split('.')[0]
		moduleList = [subModuleName]
		if moduleName != subModuleName:
			moduleList.append(moduleName)

		for module in moduleList:
			try:
				tempModule = __import__(module)
				return getattr(tempModule, name)
			except AttributeError as e:
				pass
			except ImportError as e:
				pass
	except AttributeError as e:
		namespace = __import__(baseModule)
		return getattr(namespace,name)

def zeros(rows, cols):
	m = []
	for i in range(0, rows):
		r = []
		for i in range(0,cols):
			r.append(0)
		m.append(r)
	return mp.MtPy(m)

def transpose(m, copy = True):
	m2 = zeros(m.cols(),m.rows())
	for rowId in range(0, m.rows()):
		for colId in range(0, m.cols()):
			m2[colId][rowId] = m[rowId][colId]
	if copy == False:
		m.copy(m2)
	return m2

def clone(m):
	m2 = zeros(m.rows(),m.cols())
	for rowId in range(0, m.rows()):
		for colId in range(0, m.cols()):
			m2[rowId][colId] = m[rowId][colId]
	return m2

def sin(m, copy = True):
	return _matFun_(['math', 'cmath'],'sin', copy, m)
def cos(m, copy = True):
	return _matFun_(['math', 'cmath'],'cos', copy, m)
def tan(m, copy = True):
	return _matFun_(['math', 'cmath'],'tan', copy, m)
def asin(m, copy = True):
	return _matFun_(['math', 'cmath'],'asin', copy, m)
def acos(m, copy = True):
	return _matFun_(['math', 'cmath'],'acos', copy, m)
def atan(m, copy = True):
	return _matFun_(['math', 'cmath'],'atan', copy, m)

def myFunExample(x):
	return 2*x + 1

def funExample(m, copy = True):
	return _matFun_('MtFun', 'myFunExample', copy, m)