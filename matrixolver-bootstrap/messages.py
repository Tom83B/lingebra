import pdb

#swap - (i,j)
#subs - (mult, i, j)
#mult - (rows, mults)

#	popis postupu
#___________________________________________________

def message(operation):
	op_type = operation[0]
	temp_lambda = {	'swap': lambda: swap_message(operation[1]),
		 	'subs': lambda: subs_message(operation[1]),
		 	'mult': lambda: mult_message(operation[1]),
	}[op_type]	#analogie switch/case. bohuzel neni fall-through, ale vyhodnoti se vse uvnitr. proto jsou to lambda funkce
	temp_lambda()

def swap_message(info):
	i, j = info
	return { 'cz': 'Prohozen '+str(i)+'. a '+str(j)+'. řádek.' }

def subs_message(info):
	mult, i, j = info
	return { 'cz': str(i)+'. řádek '+str(mult)+'krát odečten od '+str(j)+'. řádku.' }

def mult_message(info):
	rows, mults = info
	return { 'cz': 'Řádky byly vyděleny tak, aby na levé straně vznikla jednotková matice.' }

#	zpravy, kdyz nastane problem
#___________________________________________________

irregular_message = {	'cz': 'Matice, jejíž inverzi chceš spočítat, není regulární. Neexistuje k ní tedy inverzní matice.' }

def error_message(error):
	return {	'irregular': irregular_message
	}[error]
