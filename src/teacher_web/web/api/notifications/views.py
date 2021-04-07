from rest_framework.views import APIView
from django.conf import settings
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from api.notifications.viewmodels import NotificationIndexViewModel, NotificationDeleteViewModel

class NotificationListViewSet(APIView):
    ''' API endpoint for list of user notifications '''
    def get (self, request):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, 0, 0)

        notifications_view = NotificationIndexViewModel(db=db, settings=settings, auth_user=auth_ctx)

        return JsonResponse({"messages": notifications_view.model}, safe = False)


class NotificationDeleteViewSet(APIView):
    ''' API endpoint for deleting notification '''
    def get (self, request, id):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, 0, 0)

        notifications_view = NotificationDeleteViewModel(db=db, event_log_id=id, auth_user=auth_ctx)

        return JsonResponse({"result": notifications_view.model}, safe = False)
