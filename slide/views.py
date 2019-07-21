from django.shortcuts import render_to_response, get_object_or_404

def slide_home(request):
    context = {}
    return render_to_response("slide_base.html",context)