from .matrix import Matrix, ExtendedMatrix
import pdb


def inverse_call(M):
	if M.row_num==M.col_num:
		I = Matrix.identity(M.row_num)
		regularity = M.is_regular()
		if regularity['val']==False and regularity['why']=='rank':
			M.upper_triang_steps()	#chci oblbnout funkci gauss() v ExtendedMatrix, aby upravy skoncily u schodoviteho tvaru
			E = ExtendedMatrix(M,I)
			sol = E.gauss('upper_triang')
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
	rank = M.rank()
	sol[-1]['message'] = {'cz': 'Hodnost matice je '+str(rank)}
	return {'sol': sol, 'rank': rank}

def solvesys_call(joined):
	M, vec = joined.col_split(joined.col_num-1)
	if M.rank()==joined.rank():	#frobeniova veta - zda existuje reseni
		M.gauss_steps()		#aby mela vypoctene piv_cols
		E = ExtendedMatrix(M,vec)
		sol = E.gauss()		#nedefinuji ale nic k message, jelikoz posledni zustane prazdna
		final_mx = sol[-1]['sol'].left.rows
		final_vec = [ sol[-1]['sol'].right.rows[i][0] for i in range(0,M.row_num) ]
		# nyni zjistit, zda ma matice dim(Ker)>0
		if M.rank()<M.col_num:
			var_list = ['x','y','z','u','v','w']
			param_list = ['t','s','r']
			piv_cols = M.piv_cols
			param_cols = list(set(range(0,M.col_num))-set(piv_cols))
			param_dict = { param_cols[i]:param_list[i] for i in range(0,len(param_cols)) }	#prirazeni parametru ke sloupcum
			print_arr = [[],[]]
			for i in range(0,len(piv_cols)):	#v tomto forcyklu se vytvori tabulka pred prevedenim parametru na druhou stranu
				print_arr[0].append([])
				for j in range(0,M.col_num):
					value = final_mx[i][j]
					if value!=0:
						if j==piv_cols[i]:
							print_arr[0][-1].append(var_list[i])
						else:
							sign = '+' if value>0 else '-'
							print_arr[0][-1].append(sign+str(value)+param_dict[j] if abs(value)!=1 else sign+param_dict[j])	#pokud bude koeficient +/-1, nezobrazi se
					else:
						print_arr[0][-1].append('')
				print_arr[0][-1].append('=')
				print_arr[0][-1].append(str(final_vec[i]))
			for i in range(0,len(piv_cols)):	#nyni se parametry prevedou na druhou stranu
				print_arr[1].append([])
				print_arr[1][-1].append(var_list[i])
				print_arr[1][-1].append('=')
				print_arr[1][-1].append(str(final_vec[i]))
				for j in range(0,len(param_cols)):
					value = final_mx[i][param_cols[j]]	#divam se na misto, kde ma byt koeficient j-teho parametru
					if value!=0:
						sign = '+' if value<0 else '-'	#znamenko je obracene, protoze parametry byly prehozeny na opacnou stranu
						print_arr[1][-1].append(sign+str(value)+param_dict[param_cols[j]] if abs(value)!=1 else sign+param_dict[param_cols[j]])
					else:
						print_arr[1][-1].append('')
			return {'sol': sol, 'A': M, 'param_tables': print_arr, 'params': {'num': len(param_cols), 'list': param_list[:len(param_cols)]}}
		else:
			return {'sol': sol, 'A': M}
	else:
		M.upper_triang_steps()
		E = ExtendedMatrix(M,vec)
		sol = E.gauss()
		error = 'frobenius'
		return {'sol': sol, 'A': M, 'error': error}
