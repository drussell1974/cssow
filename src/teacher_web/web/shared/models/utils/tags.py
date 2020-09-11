from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def student_uri(scheme_of_work_id = None, lesson_id = None):
    base_uri = settings.STUDENT_WEB__WEB_SERVER_WWW

    if scheme_of_work_id is not None:
        base_uri = base_uri + "/course/%s" % scheme_of_work_id

    if lesson_id is not None:
        base_uri = base_uri + "/lesson/%s" % lesson_id

    return base_uri