from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
	#path('<int:id>/<nickname>/', views.index, name='index'),
	path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.index, name='index'),
]
