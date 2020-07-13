from django.urls import resolve, reverse
from django.test import TestCase
from .views import ResourceViewSet #, ResourceListViewSet

# Create your tests here.
class ApiResoourcesPageTest(TestCase):

    """
    def test_url_resolves_to_LessonsListViewSet_get(self):
        url = resolve("/api/schemesofwork/127/lessons/")
        self.assertEqual("api.resources.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonListViewSet.as_view()))
    
    def test_url_resolves_to_LessonsListViewSet_get__reverse(self):
        url = reverse("api.lessons.get", args=[127])
        self.assertEqual("/api/schemesofwork/127/lessons/", url)
    """

    def test_url_resolves_to_ResourceViewSet_get(self):
        url = resolve("/api/schemesofwork/127/lessons/76/resources/118")
        self.assertEqual("api.resource.get", url.url_name)
        self.assertEqual(type(url.func), type(ResourceViewSet.as_view()))

    
    def test_url_resolves_to_ResourceViewSet_get__reverse(self):
        url = reverse("api.resource.get", args=[127, 76, 118])
        self.assertEqual("/api/schemesofwork/127/lessons/76/resources/118", url)

