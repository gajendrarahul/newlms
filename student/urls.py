from django.urls import path
from . import views

urlpatterns = [
    path('student',views.student_view,name='student_view'),
    path('manager-studentview/',views.manager_studentview,name='manager_studentview')


]