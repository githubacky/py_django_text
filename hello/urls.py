from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
	path('<int:id>/<nickname>/', views.index, name='index'),
]
