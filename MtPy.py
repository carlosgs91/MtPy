from MtFun import *
import MtFun as mf

class MtPy(object):
	
	def __init__(self, *vararg):
		self.m = []
		if len(vararg) == 0:
			return
		elif len(vararg) == 1 and isinstance(vararg[0], list):
			self.m = vararg[0]
			if isinstance(self.m[0], list) == False:
				self.m = [self.m]
		else:
			for element in vararg:
				if isinstance(vararg[0], list) == False:
					element = [element]
				self.m.append(element)

	def __getitem__(self, key):
		return self.m[key]

	def __str__(self):
		s = ''
		mStr = mf.zeros(self.rows(), self.cols())
		colSizes = mf.zeros(1, self.cols())
		#print colSizes
		for rowId in range(0,self.rows()):
			for colId in range(0, self.cols()):
				mStr[rowId][colId] = str(self[rowId][colId])
				if len(mStr[rowId][colId]) > colSizes[0][colId]:
					colSizes[0][colId] = len(mStr[rowId][colId])

		for rowId in range(0,self.rows()):
			for colId in range(0, self.cols()):
				element = mStr[rowId][colId]
				extraSpace = colSizes[0][colId] - len(element)
				if colId == 0:
					s += '['
				s += ' '*extraSpace + element
				if colId != self.cols() - 1:
					s += ',' + '  '
				else:
					s += ']'
			if rowId != self.rows() - 1:
				s += '\n'
		return s

	def __repr__(self):
		return self.__str__()

	def rows(self):
		return len(self.m)

	def cols(self):
		return len(self.m[0])

	def size(self):
		return [self.rows(), self.cols()]

	def __neg__(self):
		return -1*self

	def __pos__(self):
		return self

	def __add__(self, m):
		return mf._matFun_('operator','__add__', True, self, m)

	def __radd__(self, m):
		return self.__add__(m)

	def __sub__(self, m):
		return mf._matFun_('operator','__sub__', True, self, m)

	def __rsub__(self, m):
		return -1*self.__sub__(m)

	def __mul__(self, m):
		if isinstance(m, MtPy):
			A = self
			b = m
			transposeResult = False
			if (A.cols() == b.rows() and A.rows() == 1):
				A = mf.transpose(m)
				b = mf.transpose(self)
				print A
				print b
				transposeResult = True
			if A.size() == b.size() or (A.cols() == b.rows() and b.cols() == 1):
				rows = A.rows()
				rows2 = b.rows()
				cols2 = b.cols()
				m2 = mf.zeros(rows, cols2)
				for rowId in range(0, rows):
					for colId in range(0, cols2):
						for rowId2 in range(0, rows2):
							m2[rowId][colId] += A[rowId][rowId2] * b[rowId2][colId]
				if transposeResult:
					m2 = mf.transpose(m2)
				return m2
			else:
				print 'what'
		else:
			return mf._matFun_('operator','__mul__', True, self, m)

	def __rmul__(self, m):
		#mat vs mat shouldnt reverse...
		return self.__mul__(m)

	def transpose(self, copy = False):
		return mf.transpose(self, copy = copy)

	def sin(m, copy = False):
		return mf.sin(m, copy = copy)
	def cos(m, copy = False):
		return mf.cos(m, copy = copy)
	def tan(m, copy = False):
		return mf.tan(m, copy = copy)
	def asin(m, copy = False):
		return mf.asin(m, copy = copy)
	def acos(m, copy = False):
		return mf.acos(m, copy = copy)
	def atan(m, copy = False):
		return mf.atan(m, copy = copy)