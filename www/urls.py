from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('<int:contact_id>', views.show_contact, name="contact"),
    path('update/', views.update_contact, name="update_contact"),
    path('delete/', views.delete_contact, name="delete_contact"),
    path('', views.redirect, name="redirect")
]