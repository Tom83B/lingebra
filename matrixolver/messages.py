#swap - (i,j)
#subs - (mult, i, j)
#mult - (rows, mults)

def message(operation):		#operation je step[1], tedy cast bez lambda funkce
	op_type = operation[0]
	print(operation[0])
	return { 'swap': swap_message(operation[1]),
		 'subs': subs_message(operation[1]),
		 'mult': mult_message(operation[1]),
	}[op_type]

def swap_message(info):
	i, j = info
	return { 'cz': 'Prohozen '+str(i)+'. a '+str(j)+'. řádek.' }

def subs_message(info):
	mult, i, j = info
	return { 'cz': str(i)+'. řádek '+str(mult)+'krát odečten od '+str(j)+'. řádku.' }

def mult_message(info):
	rows, mults = info
	return { 'cz': 'Řádky byly vyděleny tak, aby na levé straně vznikla jednotková matice.' }
