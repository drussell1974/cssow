from django.shortcuts import render
from django.http import HttpResponse

import models.cls_schemeofwork

# Create your views here.
def index(request):

    # get the schemes of work
    latest_schemes_of_work = cls_schemeofwork.get_latest_schemes_of_work(db, top = 5, auth_user = auth.user_id)

    content = {
        "main_heading":"Teach Computer Science",
        "sub_heading":"Computing Schemes of Work across all key stages"
              }
    context = {
        "page_title": "Dave Russell - Teach Computer Science",
        "content": content,
        "latest_schemes_of_work": latest_schemes_of_work
    }

    return render(request, "default/index.html", context)