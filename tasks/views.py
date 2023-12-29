from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list') 
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    template_name = 'auth/login.html'
    def get(self, request):
        logout(request)
        return redirect('login')

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        creation_date = self.request.GET.get('creation_date', None)
        if creation_date:
            queryset = queryset.filter(created_at__date=creation_date)
        due_date = self.request.GET.get('due_date', None)
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)
        priority = self.request.GET.get('priority', None)
        if priority:
            queryset = queryset.filter(priority=priority)
        is_complete = self.request.GET.get('completed', None)
        if is_complete:
            is_complete = is_complete.lower() == 'true'
            queryset = queryset.filter(is_complete=is_complete)
        
        queryset = queryset.filter(user=self.request.user)    
        return queryset

    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')