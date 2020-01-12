from django.urls import path

from .views import RelatedTopicsListViewSet, KeywordsListViewSet

urlpatterns = [
    #path("", views.index, name="default"),
    path("related-topics/<int:topic_id>", RelatedTopicsListViewSet.as_view() , name="api.default.related-topics"),
    path("keywords", KeywordsListViewSet.as_view(), name="api.default.keywords")
]