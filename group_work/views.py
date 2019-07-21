from django.shortcuts import render_to_response, get_object_or_404

def group_work_home(request):
    context = {}
    return render_to_response("group_work_base.html",context)