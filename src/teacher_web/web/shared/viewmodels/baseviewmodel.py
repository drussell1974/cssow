from django.http import Http404

class BaseViewModel:
    model = None

    def on_not_found(self, model, *identifers):
        prefix = repr(model) if model is not None else "item"
        raise Http404("{} {} does not exist, is currrently unavailable or you do not have permission.".format(prefix, identifers))
