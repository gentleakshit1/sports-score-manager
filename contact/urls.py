from django.urls import path
from .views import contact_view, contact_confirmation

urlpatterns = [
    path('', contact_view, name='contact'),
    path('confirmation/', contact_confirmation, name='contact_confirmation'),
]