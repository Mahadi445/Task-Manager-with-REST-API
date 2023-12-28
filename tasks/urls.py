from django.urls import path
from tasks import views as v

urlpatterns = [
    path('',v.home_page, name='home_page')
]
