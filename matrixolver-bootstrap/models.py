from django.db import models

#from .matrix import Matrix as m_class
#
#
#class MatrixField(models.Field)
#	def __init__(self, *args, **kwargs):
#		kwargs['max_length'] = 104
#		super(MatrixField, self).__init__(*args,**kwargs)
#
#class Matrix(models.Model):
#	row_num = models.IntegerField()
#	col_num = models.IntegerField()
#
#	def associate(self):
#		cells = self.cell_set
#		flat_rows = [ cell.val for cell in cells ]
#		self.rows = []
#		for i in range (0,self.row_num):
#			for j in range(0,self.col_num):
#				self.rows[i][j] = flat_rows[i*self.col_num-1+j]
#		self.mat = m_class(self.rows)
#
#	def __str__(self):
#		return 'matrix'
#	#vsechny veci importovany z matrixu
#
#class Cell(models.Model):
#	matrix = models.ForeignKey(Matrix)
#	row = models.IntegerField()
#	col = models.IntegerField()
#	val = models.FloatField()
#
## Create your models here.
