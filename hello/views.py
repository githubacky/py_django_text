from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def index(request):
	if 'msg' in request.GET:
		msg = request.GET['msg']
		result = 'you typed: "' + msg + '".'
	else:
		result = 'please send msg parameter!'
	
	return HttpResponse(result)
'''
def index(request, id, nickname):
	result = 'you id: ' + str(id) + ', name: "' + nickname + '".'
	
	return HttpResponse(result)
