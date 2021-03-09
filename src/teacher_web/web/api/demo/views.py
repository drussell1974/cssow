from rest_framework.views import APIView
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from .viewmodels import DefaultRestoreDemoDataViewModel

#@permission_required("admin.can_restore_demo_data")
class RestoreDemoDataApiView(APIView):
    ''' API endpoint for restoring demo data for demo '''
    
    def get(self, request):
        ''' checks database to restore demo data as necessary '''
        
        ''' NOTE: must be running on localhost '''
        
        # TODO: check request if from localhost

        #auth_ctx = AuthCtx(db, request, institute_id=0, department_id=0)
        auth_ctx = 2

        restore_data_view = DefaultRestoreDemoDataViewModel(db, auth_user=auth_ctx)
        
        return JsonResponse(restore_data_view.model, safe = False)