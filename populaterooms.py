import os
import django
from decimal import Decimal

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservations.settings')
django.setup()

from reservations.models import Room

def populate_rooms():
    rooms_data = [
        {'room_number': '101', 'room_type': 'Single', 'price': Decimal('50.00'), 'is_available': True, 'image': 'room_images/room1.jpg'},
        {'room_number': '102', 'room_type': 'Double', 'price': Decimal('80.00'), 'is_available': True, 'image': 'room_images/room2.jpg'},
        {'room_number': '103', 'room_type': 'Suite', 'price': Decimal('120.00'), 'is_available': True, 'image': 'room_images/room3.jpg'},
        {'room_number': '104', 'room_type': 'Deluxe', 'price': Decimal('150.00'), 'is_available': True, 'image': 'room_images/room4.jpg'},
        {'room_number': '201', 'room_type': 'Single', 'price': Decimal('55.00'), 'is_available': True, 'image': 'room_images/room5.jpg'},
        {'room_number': '202', 'room_type': 'Double', 'price': Decimal('85.00'), 'is_available': True, 'image': 'room_images/room6.jpg'},
        {'room_number': '203', 'room_type': 'Suite', 'price': Decimal('125.00'), 'is_available': True, 'image': 'room_images/room7.jpg'},
        {'room_number': '204', 'room_type': 'Deluxe', 'price': Decimal('155.00'), 'is_available': True, 'image': 'room_images/room8.jpg'},
    ]

    for room_data in rooms_data:
        room, created = Room.objects.get_or_create(
            room_number=room_data['room_number'],
            defaults={
                'room_type': room_data['room_type'],
                'price': room_data['price'],
                'is_available': room_data['is_available'],
                'image': room_data['image'],
            }
        )
        if created:
            print(f"Created room {room.room_number} - {room.room_type}")
        else:
            print(f"Room {room.room_number} already exists")

if __name__ == '__main__':
    populate_rooms()
