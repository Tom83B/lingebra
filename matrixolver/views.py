from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from .matrix import Matrix, ExtendedMatrix


def index(request):
	A = Matrix.zeros(size=(3,3))
	return render(request, 'matrixolver/index.html', {'A': A,})

def get_size(request):
	if request.method == 'POST':
		post = request.POST
		row_num = int(request.POST.get('row_num', 4))
		col_num = int(request.POST.get('col_num', 4))
		A = Matrix.zeros(size=(row_num, col_num))
		return render(request, 'matrixolver/solution.html', {'A': A, 'post': post,})
	return index(request)
		
def solution(request):
	if request.method == 'POST':
		rows = []
		row_num = int(request.POST.get('hidden_rows', 4))
		col_num = int(request.POST.get('hidden_cols', 5))
		for i in range(0, row_num):
			rows.append([])
			for j in range(0, col_num):
				cell_name = 'a'+str(i)+str(j)
				rows[i].append( float(request.POST.get(cell_name, 0.)) )
		A = Matrix(rows)
		I = Matrix.identity(A.row_num)
		E = ExtendedMatrix(A,I)
		sol = E.gauss()
		return render(request, 'matrixolver/index.html', {'sol': sol, 'A': A,})
	return index(request)



# Create your views here.
