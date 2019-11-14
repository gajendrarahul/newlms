from django.urls import path
from . import views

urlpatterns = [
    path('manager',views.manager_view,name='manager_view'),
    path('manager-teacherview/',views.manager_teacherview,name='manager_teacherview')


]