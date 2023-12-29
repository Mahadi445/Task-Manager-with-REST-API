from django.urls import path
from .views import RegisterView, LoginView, LogoutView
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
