from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Takes a request and sends back the response
# request handler

def hello(request):
    return render(request, 'hello.html', { 'appName': "Playground"})
    # return HttpResponse("Hello")
