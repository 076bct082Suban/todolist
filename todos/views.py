from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .models import Todolist, Todo

# Create your views here.
def home_view(request):
    todolists = Todolist.objects.all()

    context = {
        "user" : request.user,
        'todolists': todolists
    }
    # template = loader.get_template('todos/index.html')
    return render(request, 'todos/index.html', context )
    # return HttpResponse("hello world")