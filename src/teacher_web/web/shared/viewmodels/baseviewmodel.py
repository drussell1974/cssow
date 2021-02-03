from django.http import Http404

class BaseViewModel:
    model = None
    error_message = ""
    alert_message = ""
    saved = False

    def on_post_complete(self, saved = False):
        self.saved = saved    


    def on_not_found(self, model, *identifers):
        prefix = repr(model) if model is not None else "item"
        raise Http404("{} {} does not exist, is currently unavailable or you do not have permission.".format(prefix, identifers))
