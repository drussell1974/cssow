from django.urls import resolve, reverse
from django.test import TestCase
from api.default.views import KeywordsListViewSet, RelatedTopicsListViewSet

# Create your tests here.
class test_api_route_default_keywords(TestCase):

    def test_url_resolves_to_KeywordsListViewSet_view(self):
        url = resolve('/api/institute/127671276711/department/67/keywords/13')
        self.assertEqual("api.default.keywords", url.url_name)
        self.assertEqual(type(url.func), type(KeywordsListViewSet.as_view()))


    def test_url_resolves_to_KeywordsListViewSet_view__reverse(self):
        url = reverse("api.default.keywords", args=[127671276711, 67, 13])
        self.assertEqual("/api/institute/127671276711/department/67/keywords/13", url)
