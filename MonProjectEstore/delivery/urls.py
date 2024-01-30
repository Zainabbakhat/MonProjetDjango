from django.urls import path
from . import views

urlpatterns = [
    # Ajouter une nouvelle adresse de livraison
    path('delivery/add/', views.add_delivery_info, name='add_delivery_info'),
    
    # Afficher la liste des adresses de livraison pour l'utilisateur connecté
    path('delivery/', views.list_delivery_info, name='list_delivery_info'),
    
    # Modifier une adresse de livraison existante
    path('delivery/edit/<int:id>/', views.edit_delivery_info, name='edit_delivery_info'),
    
    # Supprimer une adresse de livraison
    path('delivery/delete/<int:id>/', views.delete_delivery_info, name='delete_delivery_info'),
]
