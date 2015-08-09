from .matrix import Matrix, ExtendedMatrix
import pdb


def inverse_call(M):
	message = None
	if M.row_num==M.col_num:
		I = Matrix.identity(M.row_num)
		regularity = M.is_regular()
		if regularity['val']==False and regularity['why']=='rank':
			M.upper_triang_steps()	#chci oblbnout funkci gauss() v ExtendedMatrix, aby upravy skoncily u schodoviteho tvaru
			E = ExtendedMatrix(M,I)
			sol = E.gauss()
			error = 'irregular'
			return {'sol': sol, 'error': error}
		elif regularity['val']==True:
			E = ExtendedMatrix(M,I)
			sol = E.gauss()
			sol[-1][1] = {'cz': 'Na pravé straně je nyní inverzní matice'}
			return {'sol': sol}
