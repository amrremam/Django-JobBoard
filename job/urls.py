from django.urls import path, include
from . import views




urlpatterns = [
    path('list', views.job_list),
    path('<int:id>', views.job_details),
]