from django.urls import path
from . import views

urlpatterns = [
    path('manager',views.teacher_view,name='teacher_view'),


]