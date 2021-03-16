class ViewHelper:

    @staticmethod
    def postSaveRedirect(request, next_step, add_another, default):

        redirect_to_url = "/" # home

        if request.POST.get("wizard_mode", 0) == "1":
            # next option
            redirect_to_url = next_step

        elif request.POST.get("wizard_mode", 0) == "2":
            # add another option
            redirect_to_url = add_another

        elif request.POST["next"] != "None"  and request.POST["next"] != "":
            # use in page next value
            redirect_to_url = request.POST["next"]    

        else:
            # default to url after save       
            redirect_to_url = default

        return redirect_to_url
