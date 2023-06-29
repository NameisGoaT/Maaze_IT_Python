from django.urls import path
from .views import ManagerListCreateView

urlpatterns = [
    path('managers/', ManagerListCreateView.as_view(), name='manager-list-create'),
]