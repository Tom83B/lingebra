from django import template

register = template.Library()


@register.filter(name='row_class')
def row_class(operation, row_index):
	if len(operation):
		op_type = operation[0]
		temp_lambda = {	'swap': lambda: swap_class(operation[1], row_index),
				'subs': lambda: subs_class(operation[1], row_index),
				'mult': lambda: mult_class(operation[1], row_index),
		}[op_type]	#analogie switch/case. bohuzel neni fall-through, ale vyhodnoti se vse uvnitr. proto jsou to lambda funkce
		return temp_lambda()
	else: return ''

def swap_class(info, row_index):
	i, j = info
	if row_index==i or row_index==j:
		return 'cSwap'
	else: return ''

def subs_class(info, row_index):
	mult, i, j = info
	if row_index==i:
		return 'cSubsSubstrahend'
	elif row_index==j:
		return 'cSubsMinuend'
	else: return ''

def mult_class(info, row_index):
	rows, mults = info
	if row_index in rows: return 'cMult'
	else: return ''
