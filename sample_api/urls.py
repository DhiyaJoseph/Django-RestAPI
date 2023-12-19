from django.urls import path
from .views import PersonListCreateView, personDetailAPIview

urlpatterns = [
    path('', PersonListCreateView.as_view(), name='Listcreate'),
    path('person/<pk>/', personDetailAPIview.as_view(), name='person-detail'),
]
