document.addEventListener('DOMContentLoaded', function () {
    const filterButton = document.getElementById('filter-button');
    const roomTypeSelect = document.getElementById('room_type');
    const availabilitySelect = document.getElementById('availability');
    const maxPriceInput = document.getElementById('max_price');
    const roomItems = document.querySelectorAll('.room-item');

    filterButton.addEventListener('click', function () {
        const roomType = roomTypeSelect.value;
        const availability = availabilitySelect.value;
        const maxPrice = parseFloat(maxPriceInput.value);

        roomItems.forEach(function (room) {
            const roomPrice = parseFloat(room.getAttribute('data-price'));
            const roomTypeData = room.getAttribute('data-room-type');
            const roomAvailability = room.getAttribute('data-availability');

            let showRoom = true;

            if (roomType && roomType !== roomTypeData) {
                showRoom = false;
            }

            if (availability && availability !== roomAvailability) {
                showRoom = false;
            }

            if (!isNaN(maxPrice) && roomPrice > maxPrice) {
                showRoom = false;
            }

            if (showRoom) {
                room.style.display = 'block';
            } else {
                room.style.display = 'none';
            }
        });
    });
});
