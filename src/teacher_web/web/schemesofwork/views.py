from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "page_title": "Dave Russell - Teach Computer Science",
        "content": {
            "main_heading":"Schemes of Work",
            "sub_heading":"Our shared schemes of work by key stage"
        }
    }

    return render(request, "schemesofwork/index.html", context)