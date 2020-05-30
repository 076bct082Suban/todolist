from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),

    path('api/', views.apiOverview, name='apiOverview'),
    path('api/todo-list', views.todoList, name='todoList'),
    path('api/todo-detail/<int:pk>', views.todoDetail, name='todoDetail'),
    path('api/todo-create/', views.todoCreate, name="todoCreate"),
    path('api/todo-update/<int:pk>', views.todoUpdate, name="todoUpdate"),
    path('api/todo-delete/<int:pk>', views.todoDelete, name='todoDelte'),
    path('api/get-todolists', views.getTodoLists, name="getTodoLists")
        #     'List': '/todo-list/',
        # 'Detail View': '/todo-detail/<int:pk>/',
        # 'Create': '/todo-create/',
        # 'Update': '/todo-update/<int:pk>/',
        # 'Delete': '/todo-delete/<int:pk>/'
]
