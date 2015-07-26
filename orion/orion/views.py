from django.http import HttpResponse
import json
from django.shortcuts import render

def leer(request):
	if request.method=='POST': 
		context={"postrecibido":json.loads(request.POST)}
		return render(request,'templates/pagina.html',context)
	else:
		return HttpResponse("esperando post")


