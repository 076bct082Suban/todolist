from rest_framework import serializers
from .models import Todo, Todolist

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoListsSerializers(serializers.ModelSerializer):
    todo_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Todolist
        # fields = "__all__"
        fields = ["id", "list_name", "user", "todo_set"]
        