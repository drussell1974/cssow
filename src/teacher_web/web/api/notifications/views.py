from rest_framework.views import APIView
from django.conf import settings
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from api.notifications.viewmodels import NotificationIndexViewModel

class NotificationListViewSet(APIView):
    ''' API endpoint for list of user messages '''
    def get (self, request):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, 0, 0)

        notifications_view = NotificationIndexViewModel(db=db, settings=settings, auth_user=auth_ctx)

        return JsonResponse({"messages": notifications_view.model}, safe = False)
