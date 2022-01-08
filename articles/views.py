from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse

# add some functions
def articles(request):
    return HttpResponse('This is home page which contains articles')

def categories(request, name):
    return HttpResponse('This is categories page for ' + str(name))
