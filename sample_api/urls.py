from django.urls import path
from .views import PersonListCreateView

urlpatterns = [
    path('', PersonListCreateView.as_view(), name='Listcreate'),
]
