def html_validation_message(validation_messages):
    if len(validation_messages) == 0:
        return None
    else:
        html = ""
        for property, message in validation_messages.items():
            #property = property.replace('_', ' ').title()
            html = html + "<b>{property}</b> {message}<br>".format(property=property, message=message)
        return html
