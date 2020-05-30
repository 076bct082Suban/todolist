from rest_framework import serializers
from .models import Todo, Todolist

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoListsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Todolist
        fields = "__all__"
        