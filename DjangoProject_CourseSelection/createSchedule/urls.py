from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
    path('courses/', views.available_courses, name='courses'),
    path('schedule/', views.schedule, name='schedule'),
    path('profile/', views.local_users, name='profile'),

]
