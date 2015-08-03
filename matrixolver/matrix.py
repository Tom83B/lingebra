import copy

class Matrix():
	def __init__(self, rows=None, size=None):
		if rows is not None:
			self.rows = rows
			self.row_num = len(rows)
			self.col_num = len(rows[0])
		else:
			if size is not None:
				self.row_num, self.col_num = size

	@classmethod
	def zeros(cls, size):
		zero_list = [ [ 0 for i in range(0,size[1]) ] for j in range(0,size[0]) ]	#numpy
		return cls(zero_list)

	@classmethod
	def identity(cls, size):
		temp_list = [ [ 0 for i in range(0,size) ] for j in range(0,size) ]	#numpy
		for i in range(0,size):
			temp_list[i][i] = 1
		return cls(temp_list)

	def mprint(self):
		for row in self.rows: print row

	def swap_rows(self, row1, row2):
		self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
		return self

	def substract_row(self, row1, row2, mult):	#numpy
		for i in range(0,self.col_num):
			self.rows[row2][i] = self.rows[row2][i]-mult*self.rows[row1][i]
		return self

	def multiply_row(self, row, mult):	#numpy
		self.rows[row] = [ self.rows[row][i]*mult for i in range(0,self.col_num) ]
		return self

	def upper_triang_steps(self):
		self.steps = []
		self.piv_cols = []
		A = copy.deepcopy(self)
		pivot = 0
		i = 0
		self.check = []
		while pivot<A.col_num-1:
			if A.rows[i][pivot] == 0:
				min_ind = 0
				try:
					pivot_col = [ A.rows[j][pivot] for j in range(0,A.row_num) ]
					min_val = min(list(filter(lambda x: x!=0, pivot_col)), key=abs)
				except ValueError:
					pivot += 1
					continue

				for j in range(i+1,A.row_num):
					if abs(A.rows[j][pivot])==min_val:
						min_ind = j
						A.swap_rows(j,i)
						self.steps.append(lambda M, i=i, j=j: M.swap_rows(i,j))
			
			for j in range(i+1,A.row_num):
				mult = A.rows[j][pivot]/A.rows[i][pivot]
				if mult!=0:
					self.steps.append(lambda M, i=i, j=j, mult=mult: M.substract_row(i,j,mult))
					A.substract_row(i,j,mult)

			self.piv_cols.append(pivot)
			pivot += 1
			i += 1
		if pivot==A.col_num-1 and A.rows[i][pivot]!=0: self.piv_cols.append(pivot)

	def gauss_steps(self):
		A = copy.deepcopy(self)
		self.upper_triang_steps()
		for step in self.steps: step(A)

		for pivot in self.piv_cols[1:][::-1]:
			pivot_col = [ A.rows[i][pivot] for i in range(0,A.row_num) ]	#numpy
			for i in range(0,A.row_num)[::-1]:
				if A.rows[i][pivot]!=0:
					for j in range(0,i):
						mult = A.rows[j][pivot]/A.rows[i][pivot]
						if mult!=0:
							self.steps.append(lambda M, mult=mult, i=i, j=j: M.substract_row(i,j,mult))
							A.substract_row(i,j,mult)
					break

		for pivot in self.piv_cols:
			pivot_col = [ A.rows[i][pivot] for i in range(0,A.row_num) ]	#numpy
			for i in range(0,A.row_num):
				mult = A.rows[i][pivot]
				if mult!=0 and mult!=1:
					print i, pivot
					print mult
					inv_mult = 1./mult
					self.steps.append(lambda M, i=i, inv_mult=inv_mult: M.multiply_row(i,inv_mult))
					A.multiply_row(i,inv_mult)
					break
	

class ExtendedMatrix:
	def __init__(self, left, right):
		self.left = copy.deepcopy(left)
		self.right = copy.deepcopy(right)

	def gauss(self):
		if not hasattr(self.left, 'steps'):
			self.left.gauss_steps()
		return [ ExtendedMatrix(step(self.left), step(self.right)) for step in self.left.steps ]

A = Matrix([[1.,0.,0.],[0.,2.,0.],[0.,0.,3.]])
A.gauss_steps()
#I = Matrix([[1,0],[0,1]])
#ex = ExtendedMatrix(A, I)
#inv = ex.gauss()
