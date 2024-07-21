from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
  if request.method == 'GET':
    return render(request, 'index.html')
  else:
    return HttpResponseNotFound('Not Found')
  