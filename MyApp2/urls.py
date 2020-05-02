from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form_list, name='form_list'),
    path('form/<int:pk>/', views.form_detail, name='form_detail'),
    path('add/form/', views.add_form, name='add_form'),
    path('form/<int:pk>/edit/', views.form_edit, name='form_edit'),
]