from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('people/', PersonListView.as_view(), name='person-list'),
    path('people/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
