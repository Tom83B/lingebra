from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from fractions import Fraction
from .matrix import Matrix, ExtendedMatrix
from .matrix_calls import inverse_call, rank_call
from . import messages

import pdb

def index(request):
	return render(request, 'matrixolver/index.html')

def inv_index(request):
	A = Matrix.zeros(size=(3,3))
	return render(request, 'matrixolver/inverse.html', {'A': A,})

#def inv_get_size(request):
#	if request.method == 'POST':
#		post = request.POST
#		row_num = int(request.POST.get('row_num', 4))
#		col_num = int(request.POST.get('col_num', 4))
#		A = Matrix.zeros(size=(row_num, col_num))
#		return render(request, 'matrixolver/inverse.html', {'A': A, 'post': post,})
#	return inv_index(request)
		
def inv_solution(request):
	if request.method == 'POST':
		rows = []
		row_num = int(request.POST.get('hidden_rows', 4))
		col_num = int(request.POST.get('hidden_cols', 5))
		for i in range(0, row_num):
			rows.append([])
			for j in range(0, col_num):
				cell_name = 'a'+str(i)+str(j)
				rows[i].append( Fraction(request.POST.get(cell_name, 0.)) )
		A = Matrix(rows)
		result = inverse_call(A)
		if 'error' in result:
			print(result['error'])
			error_message = messages.error_message(result['error'])
			return render(request, 'matrixolver/inverse.html', {'sol': result['sol'], 'A': A, 'rows': rows, 'error': error_message['cz'],})
		else:
			return render(request, 'matrixolver/inverse.html', {'sol': result['sol'], 'A': A, 'rows': rows,})
	return inv_index(request)

def rank(request):
	A = Matrix.zeros(size=(4,4))
	return render(request, 'matrixolver/rank.html', {'A': A,})

def rank_solution(request):
	if request.method == 'POST':
		rows = []
		row_num = int(request.POST.get('hidden_rows', 4))
		col_num = int(request.POST.get('hidden_cols', 5))
		for i in range(0, row_num):
			rows.append([])
			for j in range(0, col_num):
				cell_name = 'a'+str(i)+str(j)
				rows[i].append( Fraction(request.POST.get(cell_name, 0.)) )
		A = Matrix(rows)
		result = rank_call(A)
		if 'error' in result:
			print(result['error'])
			error_message = messages.error_message(result['error'])
			return render(request, 'matrixolver/rank.html', {'sol': result['sol'], 'A': A, 'rows': rows, 'error': error_message['cz'],})
		else:
			return render(request, 'matrixolver/rank.html', {'sol': result['sol'], 'A': A, 'rows': rows,})
	return rank(request)

def system(request):
	A = Matrix.zeros(size=(3,3))
	return render(request, 'matrixolver/syslineq.html', {'A': A,})

# Create your views here.
