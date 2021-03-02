from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def student_uri(institute_id, department_id, scheme_of_work_id = None, lesson_id = None):
    base_uri = settings.STUDENT_WEB__WEB_SERVER_WWW

    base_uri = base_uri + "/institute/%s" % institute_id
    base_uri = base_uri + "/department/%s/course/" % department_id
    
    if scheme_of_work_id is not None:
        base_uri = base_uri + "%s/lesson/" % scheme_of_work_id

    if lesson_id is not None:
        base_uri = base_uri + "%s" % lesson_id

    return base_uri