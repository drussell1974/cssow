from django.http import HttpRequest
from django.urls import resolve, reverse
from urllib.parse import urlparse

class BreadcrumbGenerator:

    @classmethod
    def get_items(cls, request):
        
        breadcrumbs = {}

        # get url parameters        
        
        path = urlparse(request.path)[2]
        
        kwargs = resolve(path)[2] # get kwargs bits

        # check for institute in url
        institute_id = kwargs.get("institute_id", 0)
        if institute_id > 0:
            #breadcrumbs["/institute"] = {"id":"lnk-bc-institutes","text":"Institutes"}

            # check for department in url
            department_id = kwargs.get("department_id", 0)
            if department_id > 0:
                breadcrumbs[reverse("department.index", args=[institute_id])] = {"id":"lnk-bc-departments","text":"departments"}

                # check for scheme of work in url
                schemeofwork_id = kwargs.get("scheme_of_work_id", 0)
                if schemeofwork_id > 0:
                    breadcrumbs[reverse("schemesofwork.index", args=[institute_id,department_id])] = {"id":"lnk-bc-schemes_of_work","text":"schemes of work"}
                    
                    # check for lesson in url 
                    lesson_id = kwargs.get("lesson_id", 0)
                    if lesson_id > 0:
                        breadcrumbs[reverse("lesson.index", args=[institute_id,department_id, schemeofwork_id])] = {"id":"lnk-bc-lessons","text":"lessons"}
        
        return breadcrumbs
