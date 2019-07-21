from django.shortcuts import render_to_response, get_object_or_404

def prepare_home(request):
    context = {}
    return render_to_response("prepare_base.html",context)