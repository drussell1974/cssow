from django.core.files.storage import FileSystemStorage
from django.conf import settings

def handle_uploaded_markdown(f, model, on_success=None, on_error=None):
    # generate subfolder path
    path = "{scheme_of_work}/{lesson}/{resource}/{filename}".format(
        scheme_of_work=model.scheme_of_work_id, 
        lesson=model.lesson_id, 
        resource=model.id, 
        filename=f)
        
    try:
        # use django FileSystemStorage to upload to MARKDOWN_ROOT
        fs = FileSystemStorage(location=settings.MARKDOWN_STORAGE)
        fs.save(path, f)

        # complete with callback to success_handler
        if on_success is not None:
            on_success(f, "filehandler.py handle_uploaded_markdown: {} saved to {}".format(f, path))

    except Exception as err:
        if on_error is not None:
            on_error(err, "handle_uploaded_file: An error occurred uploading {} to {}".format(f, path))
        else:
            raise