from django.urls import path
from calc import views


app_name = 'operation'

urlpatterns = [
    path('process/', views.Calculator.as_view(), name='process'),

]
