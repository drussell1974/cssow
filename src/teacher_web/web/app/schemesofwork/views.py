from django.shortcuts import render
from cssow.models import cls_schemeofwork

# Create your views here.

def index(request):
    schemes_of_work = cls_schemeofwork.get_all(None, key_stage_id=0, auth_user=request.user.id)
    context = {
        "page_title": "Dave Russell - Teach Computer Science",
        "content": {
            "main_heading":"Schemes of Work",
            "sub_heading":"Our shared schemes of work by key stage",
            "schemes_of_work": schemes_of_work
        }
    }

    return render(request, "schemesofwork/index.html", context)