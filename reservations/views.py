from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Room, Reservation
from .forms import RoomForm

def home(request):
    return render(request, 'index.html')

@login_required
def index(request):
    user = request.user  # Obtenemos el usuario actualmente autenticado
    reservations = Reservation.objects.filter(user=user)  # Obtener historial de reservas del usuario (ejemplo)

    context = {
        'title': 'Profile',
        'user': user,
        'reservations': reservations,
    }
    return render(request, 'accounts/profile.html', context)

@staff_member_required  # Requiere que el usuario sea un administrador
def admin_dashboard(request):
    # Obtener información relevante para el dashboard
    total_rooms = Room.objects.count()
    total_reservations = Reservation.objects.count()

    context = {
        'title': 'Admin Dashboard',
        'total_rooms': total_rooms,
        'total_reservations': total_reservations,
    }
    return render(request, 'accounts/admin_dashboard.html', context)

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'reservations/room_list.html', {'rooms': rooms})

def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def make_reservation(request, room_id):
    if request.method == 'POST':
        room = Room.get_object_or_404(id=room_id)
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        reservation = Reservation(user=request.user, room=room, check_in=check_in, check_out=check_out)
        reservation.save()
        return redirect('reservation_list')
    else:
        room = get_object_or_404(Room, id=room_id)
        return render(request, 'reservations/make_reservation.html', {'room': room})

@login_required
@staff_member_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'reservations/create_room.html', {'form': form})

@login_required
@staff_member_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'reservations/edit_room.html', {'form': form, 'room': room})

@login_required
@staff_member_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'reservations/delete_room.html', {'room': room})

def profile(request):
    return render(request, 'accounts/profile.html')

def admin_room_list(request):
    rooms = Room.objects.all()
    return render(request, 'reservations/room_list.html', {'rooms': rooms})
