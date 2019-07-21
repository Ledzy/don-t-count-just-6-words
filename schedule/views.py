from django.shortcuts import render_to_response, get_object_or_404

def schedule_home(request):
    context = {}
    return render_to_response("schedule_base.html",context)