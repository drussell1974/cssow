from django.http import Http404


def on_not_found(self, model, *identifers):
    str_msg = "The item is currently unavailable or you do not have permission."
    raise Http404(str_msg)
