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
			sol[-1]['message'] = {'cz': 'Matice není regulární. Neexistuje k ní tedy inverzní'}
			error = 'irregular'
			return {'sol': sol, 'error': error}	#sol je jeden velky slovnik, aby v nem slo v templatu prehledne iterovat
		elif regularity['val']==True:
			E = ExtendedMatrix(M,I)
			sol = E.gauss()
			sol[-1]['message'] = {'cz': 'Na pravé straně je nyní inverzní matice'}
			error = 'irregular'
			return {'sol': sol, 'messages': message}