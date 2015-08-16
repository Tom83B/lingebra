from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^inverse/solution/', views.inv_solution, name='inv_solution'),
	#url(r'^inverse/inv_get_size/', views.inv_get_size, name='inv_get_size'),
	url(r'^inverse/', views.inv_index, name='inv_index'),
	url(r'^rank/solution', views.rank_solution, name='rank_solution'),
	url(r'^rank/', views.rank, name='rank'),
	url(r'^system/solution', views.system_solution, name='system_solution'),
	url(r'^system/', views.system, name='system'),
	url(r'^', views.index, name='index'),
	#url(r'^/table_size/', views.table_size, name='table_size'),
]
