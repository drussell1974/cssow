from django.core.files.storage import FileSystemStorage
from django.conf import settings
import time
import os


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MARKDOWN_STORAGE, name))
        return name

        
def handle_uploaded_markdown(f, model, on_success=None, on_error=None):
    # generate subfolder path
    path = "{scheme_of_work}/{lesson}/{resource}/{filename}".format(
        scheme_of_work=model.scheme_of_work_id, 
        lesson=model.lesson_id, 
        resource=model.id, 
        filename=f)

    try:
        # use django FileSystemStorage to upload to MARKDOWN_ROOT
        fs = OverwriteStorage(location=settings.MARKDOWN_STORAGE)
        #fs.get_available_name(path)

        fs.save(path, f)

        # complete with callback to success_handler
        if on_success is not None:
            on_success(f, "filehandler.py handle_uploaded_markdown: {} saved to {}".format(f, path))

    except Exception as err:
        err_msg = "handle_uploaded_file: An error occurred uploading {} to {}".format(f, path)
        if on_error is not None:
            on_error(err, err_msg)
        else:
            raise
        raise Exception(err_msg, err)
