
import io
from shared.models.utils.demo_helper import DemoHelper
from shared.viewmodels.baseviewmodel import BaseViewModel

class DefaultRestoreDemoDataViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        try:

            DemoHelper.restore(db, auth_user)

            self.model = {"complete":True}  
            
        except Exception as e:
            self.model = {"complete": False, "error": str(e) }