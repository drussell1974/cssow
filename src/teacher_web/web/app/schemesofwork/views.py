from django.shortcuts import render
from django.db import connection as db
from cssow.models import cls_schemeofwork
from shared.view_model import ViewModel

# Create your views here.

def index(request):
    schemes_of_work = cls_schemeofwork.get_all(db, key_stage_id=0, auth_user=request.user.id)
    
    data = {
        "schemes_of_work":schemes_of_work
    }

    view_model = ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", data=data)

    return render(request, "schemesofwork/index.html", view_model.content)