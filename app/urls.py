from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aim/', views.aim, name='aim'),
    path('scope/', views.scope, name='scope'),
    path('team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('papers/<int:journal_id>', views.papers, name='papers'),
    # authentication urls
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]