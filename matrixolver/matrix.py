import copy
from fractions import Fraction
import pdb

from .messages import message

class Matrix(): #vyresit problem s float
	def __init__(self, rows=None, size=None):
		self.regular = None
		self.steps = None
		if rows is not None:
			self.rows = rows
			self.row_num = len(rows)
			self.col_num = len(rows[0])
		else:
			if size is not None:
				self.row_num, self.col_num = size

	@classmethod
	def zeros(cls, size):
		zero_list = [ [ Fraction() for i in range(0,size[1]) ] for j in range(0,size[0]) ]	#numpy
		return cls(zero_list)

	@classmethod
	def identity(cls, size):
		temp_list = [ [ Fraction() for i in range(0,size) ] for j in range(0,size) ]	#numpy
		for i in range(0,size):
			temp_list[i][i] = Fraction(1,1)
		return cls(temp_list)

	def mprint(self):
		for row in self.rows: print(row)

	def swap_rows(self, row1, row2):
		self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
		return self

	def substract_row(self, row1, row2, mult):	#numpy
		for i in range(0,self.col_num):
			self.rows[row2][i] = self.rows[row2][i]-mult*self.rows[row1][i]
		return self

	def multiply_rows(self, rows, mults):	#numpy
		for (row, mult) in zip(rows, mults):
			self.rows[row] = [ self.rows[row][i]*mult for i in range(0,self.col_num) ]
		return self

	def is_regular(self):
		if self.regular is not None:
			return self.regular
		else:
			if self.row_num != self.col_num:
				return {'val': False, 'why': 'not_square'}
			elif self.steps is not None:
				product = 1
				X = copy.deepcopy(self)
				for step in self.steps: step[0](X)
				diagonal = [ X.rows[i][i] for i in range(0,X.row_num) ]
				for element in diagonal: product *= element
				if product == 0: return {'val': False, 'why': 'rank'}
				else: return {'val': True, 'why': 'you are good to go!'}
			else:
				X = copy.deepcopy(self)	#nechci, aby mela matice steps not None a gauss byl pritom jen polovicni
				X.upper_triang_steps()
				return X.is_regular()	#ted by uz steps nemelo byt None

	def col_split(self, col):	#col je sloupec, za kterym se to lame
		rowsA = [ row[:col] for row in self.rows ]
		rowsB = [ row[col:] for row in self.rows ]
		return Matrix(rowsA), Matrix(rowsB)

	def upper_triang_steps(self):
		self.steps = []
		self.piv_cols = []
		A = copy.deepcopy(self)
		pivot = 0
		i = 0
		while i<A.row_num and pivot<A.col_num:
			if A.rows[i][pivot] == 0:
				min_ind = 0
				try:
					pivot_col = [ A.rows[j][pivot] for j in range(0,A.row_num) ]
					min_val = min(list(filter(lambda x: x!=0, pivot_col[i:])), key=abs)
				except ValueError:
					pivot += 1
					continue

				for j in range(i+1,A.row_num):
					if abs(A.rows[j][pivot])==min_val:
						min_ind = j
						A.swap_rows(j,i)
						lambda_func = lambda M, i=i, j=j: M.swap_rows(i,j)
						self.steps.append((lambda_func, ['swap', (i,j)]));
			
			for j in range(i+1,A.row_num):
				try:
					mult = Fraction(A.rows[j][pivot],A.rows[i][pivot])
					if mult!=0:
						lambda_func = lambda M, i=i, j=j, mult=mult: M.substract_row(i,j,mult)
						self.steps.append((lambda_func, ['subs', (mult, i, j)]))
						A.substract_row(i,j,mult)
				except IndexError:
					break

			self.piv_cols.append(pivot)
			pivot += 1
			i += 1

	def gauss_steps(self):
		A = copy.deepcopy(self)
		self.upper_triang_steps()
		for step in self.steps: step[0](A)

		for pivot in self.piv_cols[1:][::-1]:
			pivot_col = [ A.rows[i][pivot] for i in range(0,A.row_num) ]	#numpy
			for i in range(0,A.row_num)[::-1]:
				if A.rows[i][pivot]!=0:
					for j in range(0,i):
						mult = Fraction(A.rows[j][pivot],A.rows[i][pivot])
						if mult!=0:
							lambda_func = lambda M, mult=mult, i=i, j=j: M.substract_row(i,j,mult)
							self.steps.append((lambda_func, ['subs', (mult,i,j)]))	#radek i se odecita od j
							A.substract_row(i,j,mult)
					break

		rows = []
		mults = []
		for pivot in self.piv_cols:
			pivot_col = [ A.rows[i][pivot] for i in range(0,A.row_num) ]	#numpy
			for i in range(0,A.row_num):
				mult = A.rows[i][pivot]
				if mult!=0 and mult!=1:
					inv_mult = Fraction(1,mult)
					rows.append(i)
					mults.append(inv_mult)
					break	
		A.multiply_rows(rows, mults)
		func = lambda M, rows=rows, mults=mults: M.multiply_rows(rows,mults)
		self.steps.append((func, ['mult', (rows, mults)]))

	def stairs(self):
		M = self
		M.upper_triang_steps()
		steps_info = [ step[1] for step in M.steps ]
		messages = [ message(info) for info in steps_info ]+[{}]
		solution = [copy.deepcopy(M)] + [ step[0](M) for step in M.steps ]
		keys = ['sol', 'info', 'message']
		return_list = [ list(a) for a in zip(solution, steps_info+[[]], messages) ]	#prvek [[]] dodan, aby vse melo stejnou delku
		return [dict(zip(keys, a)) for a in return_list]


class ExtendedMatrix:
	def __init__(self, left, right):
		self.left = copy.deepcopy(left)
		self.right = copy.deepcopy(right)

	def gauss(self):
		if self.left.steps is None:
			self.left.gauss_steps()
		steps_info = [ step[1] for step in self.left.steps ]
		messages = [ message(info) for info in steps_info ]+[{'cz': ''}]
		solution = [copy.deepcopy(self)] + [ ExtendedMatrix(step[0](self.left), step[0](self.right)) for step in self.left.steps ]
		keys = ['sol', 'info', 'message']
		return_list = [ list(a) for a in zip(solution, steps_info+[[]], messages) ]	#prvek [[]] dodan, aby vse melo stejnou delku
		return [dict(zip(keys, a)) for a in return_list]


def join(A,B):
	if A.row_num == B.row_num:
		col_num = A.col_num + B.col_num
		rows = [ rowA+rowB for (rowA,rowB) in zip(A.rows,B.rows) ]
		return Matrix(rows)
	else: raise TypeError('matice musi mit stejny pocet rad')


A = Matrix([[1,0,0],[0,2,0],[0,0,3]])
A.gauss_steps()
#I = Matrix([[1,0],[0,1]])
#ex = ExtendedMatrix(A, I)
		#inv = ex.gauss()
