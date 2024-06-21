from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ruta para la página principal
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # Rutas de usuarios
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/admin/dashboard/',views.admin_dashboard, name='admin_dashboard'),

    # Rutas de Reservaciones
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/make/<int:room_id>/',views.make_reservation, name='make_reservation'),


    # Nuevas rutas para editar y eliminar habitaciones
    path('rooms/', views.admin_room_list, name='room_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/create/', views.create_room, name='create_room'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
]

# Documentación de cambios:
# 1. Agregada la ruta 'rooms/edit/<int:room_id>/' para la vista de edición de habitaciones.
# 2. Agregada la ruta 'rooms/delete/<int:room_id>/' para la vista de eliminación de habitaciones.
