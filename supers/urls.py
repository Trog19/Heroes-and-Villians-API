from django.urls import path

import super_types
from . import views


urlpatterns =[
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    path('<int:pk>/', views.supers_type)
]
