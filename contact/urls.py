from django.urls import path
from .views import ContactDetailView, ContactListView
urlpatterns = [
    path('', ContactListView.as_view(), name = 'list'),
    path('list/<int:id>/', ContactDetailView.as_view(), name = 'listview'),
]
