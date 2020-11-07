from django.shortcuts import render
from django.contrib.auth.models import User


def room(request, room_name, username):
    if User.objects.filter(username=room_name).exists():
        temp = sorted((room_name, username))
        return render(request, 'room.html', {
            'room_name': str(temp[0])+str(temp[1]),
            'room_user': room_name,
            'username': username
        })
    else:
        return render(request, 'home.html', {
            'room_name': room_name,
            'messagefail': 'не существует в БД!'
        })
