from django.shortcuts import redirect, HttpResponse

def index(request):
    return redirect('/api/v2/')
	