from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json



@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'portrait': mark_safe(request.user.extension.portrait)
    })

def index(request):
    if request.user.is_authenticated:
        return redirect(f'./{request.user.username}')
    return redirect('../login')
    # return render(request, 'chat/index.html', {})