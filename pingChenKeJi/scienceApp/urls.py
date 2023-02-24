from django.urls import path
from . import views
from scienceApp.views import science

app_name = 'scienceApp'

urlpatterns = [
    # path('science/', views.science, name='science'),  # 科研基地
    path('science/', science, name='science'),  # 科研基地
]