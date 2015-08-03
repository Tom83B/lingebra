from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^solution/', views.solution, name='solution'),
	url(r'^get_size/', views.get_size, name='get_size'),
	url(r'^', views.index, name='index'),
	#url(r'^/table_size/', views.table_size, name='table_size'),
]
