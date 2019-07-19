from django.shortcuts import render_to_response, get_object_or_404


def home_page(request):
    context = {}
    # context['']
    return render_to_response("home.html",context)