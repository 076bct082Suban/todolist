from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todolist, Todo
from .serializers import TodoSerializers, TodoListsSerializers


# Create your views here.
def home_view(request):
    user = request.user
    todolists = user.todolist_set.all()

    context = {
        "user" : request.user,
        'todolists': todolists
    }
    # template = loader.get_template('todos/index.html')
    return render(request, 'todos/index.html', context )
    # return HttpResponse("hello world")

# For api
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<int:pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<int:pk>/',
        'Delete': '/todo-delete/<int:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializers(todos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializers(todo, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    print(request)
    serializer = TodoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    else:
        print("NOpe")
        return Response({'message': "You fked up."})


@api_view(['POST'])
def todoUpdate(request, pk):
    task = Todo.objects.get(id=pk)     
    serializer = TodoSerializers(isinstance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response("Task deleted")  
    

@api_view(['GET'])
def getTodoLists(request):
    user = request.user
    todolists = user.todolist_set.all()

    serializer = TodoListsSerializers(todolists, many=True)

    return Response(serializer.data)


# @api_view('GET')
# def getTodoList(request):
#     user = request.user
    
