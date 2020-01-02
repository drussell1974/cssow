from django.shortcuts import render

# Create your views here.

def index(request, id):
    context = {}

    return render(request, "learningepisodes/index.html", context)