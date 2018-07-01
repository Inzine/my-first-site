from django.shortcuts import render
#from django.shortcuts import HttpResponse

#def index(request):
	#return HttpResponse("FEEDs ZONE")

def post_list(request):
	return render(request, 'polls/post_list.html', {})