from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_example, name='form_example'),
]
