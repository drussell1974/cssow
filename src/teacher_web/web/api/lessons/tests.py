from django.urls import resolve, reverse
from django.test import TestCase
from api.lessons.views import LessonViewSet, LessonListViewSet, LessonPathwayObjectivesViewSet, LessonPathwayKs123ViewSet

# Create your tests here.
class ApiLessonsPageTest(TestCase):

    def test_url_resolves_to_LessonsListViewSet_get(self):
        url = resolve('/api/schemesofwork/127/lessons/')
        self.assertEqual("api.lessons.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonListViewSet.as_view()))

    
    """def test_url_resolves_to_LessonsListViewSet_get__reverse(self):
        url = reverse('api.lesson.get')
        self.assertEqual("/api/schemesofwork/127/lessons/", url)"""


    def test_url_resolves_to_LessonViewSet_get(self):
        url = resolve('/api/schemesofwork/127/lessons/76')
        self.assertEqual("api.lesson.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonViewSet.as_view()))

    
    def test_url_resolves_to_LessonPathwayObjectivesViewSet_get(self):
        """ key_words parameter is optional, but provided """
        url = resolve('/api/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/a,b,c')
        self.assertEqual("api.lesson.pathway-objectives", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayObjectivesViewSet.as_view()))


    def test_url_with_no_keywords_resolves_to_LessonPathwayObjectivesViewSet_get(self):
        """ key_words parameter is optional """
        url = resolve('/api/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/')
        self.assertEqual("api.lesson.pathway-objectives", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayObjectivesViewSet.as_view()))


    def test_url_resolves_to_LessonPathwayKs123ViewSet_get(self):
        url = resolve('/api/schemesofwork/127/lessons/0/pathway-ks123/year/0/topic/0')
        self.assertEqual("api.lesson.pathway", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayKs123ViewSet.as_view()))
