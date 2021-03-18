class WizardHelper:

    def __init__(self, default_url=None, next_url=None, add_another_url=None):
        self.default_url = default_url
        self.next_url = next_url
        self.add_another_url = add_another_url
        

    def get_redirect_url(self, request):
        
        redirect_to_url = "/" # home
        
        if request is None or request.POST.get("published") is None:
            # default to url after save
            redirect_to_url = self.default_url
        else:
            published = request.POST.get("published")
            published_action = "DEFAULT"
            
            # get the action            
            
            if len(published.split('.')) > 1:
                published_action = published.split('.')[1]
            
            # perform the action

            if published_action.upper() == "DEFAULT":
                # default save option
                redirect_to_url = self.default_url
            elif published_action.upper() == "NEXT":
                # next option
                redirect_to_url = self.next_url
            elif published_action.upper() == "ANOTHER":
                # add another option
                redirect_to_url = self.add_another_url
            else:
                # default to url after save       
                redirect_to_url = self.default_url
        return redirect_to_url
