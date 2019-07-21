from django.shortcuts import render_to_response, get_object_or_404

def assignment_home(request):
    context = {}
    return render_to_response("assignment_base.html",context)