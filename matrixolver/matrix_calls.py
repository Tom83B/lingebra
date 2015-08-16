from .matrix import Matrix, ExtendedMatrix
import pdb


def inverse_call(M):
	if M.row_num==M.col_num:
		I = Matrix.identity(M.row_num)
		regularity = M.is_regular()
		if regularity['val']==False and regularity['why']=='rank':
			M.upper_triang_steps()	#chci oblbnout funkci gauss() v ExtendedMatrix, aby upravy skoncily u schodoviteho tvaru
			E = ExtendedMatrix(M,I)
			sol = E.gauss()
			sol[-1]['message'] = {'cz': 'Matice není regulární. Neexistuje k ní tedy inverzní'}
			error = 'irregular'
			return {'sol': sol, 'error': error}	#sol je jeden velky slovnik, aby v nem slo v templatu prehledne iterovat
		elif regularity['val']==True:
			E = ExtendedMatrix(M,I)
			sol = E.gauss()
			sol[-1]['message'] = {'cz': 'Na pravé straně je nyní inverzní matice'}
			error = 'irregular'
			return {'sol': sol}

def rank_call(M):
	sol = M.stairs()
	rank = 0
	for row in M.rows[::-1]:
		if not all(val==0 for val in row): rank += 1
	sol[-1]['message'] = {'cz': 'Hodnost matice je '+str(rank)}
	return {'sol': sol, 'rank': rank}

def solvesys_call(joined):
	A, vec = joined.col_split(joined.col_num-1)
	E = ExtendedMatrix(A,vec)
	sol = E.gauss()		#nedefinuji ale nic k message, jelikoz posledni zustane prazdna
	return {'sol': sol, 'A': A}

#	asi by bylo cool zavest nejakou tridu Call a tohle by mohly byt jeji objekty nebo tak neco
