# tasks/api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from tasks.models import Task
from django_filters.rest_framework import DjangoFilterBackend

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'created_at', 'due_date', 'priority', 'is_complete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
