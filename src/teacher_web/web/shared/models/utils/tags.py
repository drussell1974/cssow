from datetime import datetime
from django.conf import settings
from django import template
from django.template.defaultfilters import stringfilter
from shared.models.core.helper_string import date_to_string

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


@register.filter(name="display_shortdate")
@stringfilter
def display_shortdate(value):
    """ given ISOFORMAT (see settings.ISOFORMAT) """
    # convert to date and back to display_date using date_to_string
    
    return date_to_string(datetime.strptime(value, settings.ISOFORMAT), show_long=False)


@register.filter(name="format_time")
@stringfilter
def format_time(value):
    """ given ISOFORMAT_TIME_MS (see settings.ISOFORMAT_TIME_MS) convert to short time, given settings.ISOFORMAT_TIME """
    # convert to time ms and back to short time
    
    return datetime.strptime(value, settings.ISOFORMAT_TIME_MS).strftime(settings.ISOFORMAT_TIME)
