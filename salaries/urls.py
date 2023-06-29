from django.urls import path
from .views import SalaryListCreateView

urlpatterns = [
    path('salaries/', SalaryListCreateView.as_view(), name='salary-list-create'),
]