class WizardHelper:

    def __init__(self, default_url=None, next_url=None, add_another_url=None):
        self.default_url = default_url
        self.next_url = next_url
        self.add_another_url = add_another_url
        

    def get_redirect_url(self, request):
        
        redirect_to_url = "/" # home
        if request is None or request.POST.get("wizard_mode") is None:
            # default to url after save
            redirect_to_url = self.default_url

        elif request.POST.get("wizard_mode", 0) == "0":
            # default save option
            redirect_to_url = self.default_url

        elif request.POST.get("wizard_mode", 0) == "1":
            # next option
            redirect_to_url = self.next_url

        elif request.POST.get("wizard_mode", 0) == "2":
            # add another option
            redirect_to_url = self.add_another_url

        #elif request.POST.get("next") != "None" and request.POST.get("next") != "":
        #    # use in page next value
        #    redirect_to_url = request.POST.get("next")
        
        else:
            # default to url after save       
            redirect_to_url = self.default_url

        return redirect_to_url
