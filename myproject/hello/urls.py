from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='home'),       # shows contact form at /
    path('contact/', views.contact_view, name='contact'),  # also at /contact/
]
