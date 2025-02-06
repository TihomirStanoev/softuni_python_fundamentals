rooms = int(input())

free_chairs = 0
is_free_chairs = True
for room in range(1, rooms+1):
    room_chairs = input().split()
    chairs, visitors  = room_chairs
    room_chairs = len(chairs) - int(visitors)
    remaining_chairs_in_room = room_chairs

    if remaining_chairs_in_room > 0:
        free_chairs += remaining_chairs_in_room
    elif remaining_chairs_in_room < 0:
        is_free_chairs = False
        print(f'{abs(remaining_chairs_in_room)} more chairs needed in room {room}')


if is_free_chairs:
    print(f'Game On, {free_chairs} free chairs left')