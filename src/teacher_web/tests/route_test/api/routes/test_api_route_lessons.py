from django.urls import resolve, reverse
from django.test import TestCase
from api.lessons.views import LessonViewSet, LessonListViewSet, LessonPathwayObjectivesViewSet, LessonPathwayKs123ViewSet

# Create your tests here.
class test_api_route_lessons(TestCase):

    def test_url_resolves_to_LessonsListViewSet_get(self):
        url = resolve("/api/institute/127671276711/department/67/schemesofwork/127/lessons/")
        self.assertEqual("api.lessons.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonListViewSet.as_view()))

    
    def test_url_resolves_to_LessonsListViewSet_get__reverse(self):
        url = reverse("api.lessons.get", args=[127671276711, 67, 127])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127/lessons/", url)


    def test_url_resolves_to_LessonViewSet_get(self):
        url = resolve("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76")
        self.assertEqual("api.lesson.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonViewSet.as_view()))

    
    def test_url_resolves_to_LessonViewSet_get__reverse(self):
        url = reverse("api.lesson.get", args=[127671276711, 67, 127, 76])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76", url)

    
    def test_url_resolves_to_LessonPathwayObjectivesViewSet_get(self):
        """ key_words parameter is optional, but provided """
        url = resolve("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/a,b,c")
        self.assertEqual("api.lesson.pathway-objectives", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayObjectivesViewSet.as_view()))


    def test_url_resolves_to_LessonPathwayObjectivesViewSet_get__reverse(self):
        url = reverse("api.lesson.pathway-objectives", args=[127671276711, 67, 127, 76, 4, "a,b,c"])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/a,b,c", url)


    def test_url_with_no_keywords_resolves_to_LessonPathwayObjectivesViewSet_get(self):
        """ key_words parameter is optional """
        url = resolve("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/")
        self.assertEqual("api.lesson.pathway-objectives", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayObjectivesViewSet.as_view()))

    
    def test_url_with_no_keywords_resolves_to_LessonPathwayObjectivesViewSet_get__reverse(self):
        url = reverse('api.lesson.pathway-objectives', args=[127671276711, 67, 127, 76, 4])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-objectives/key-stage/4/keywords/", url)


    def test_url_resolves_to_LessonPathwayKs123ViewSet_get(self):
        url = resolve("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-ks123/key-stage/2/topic/4")
        self.assertEqual("api.lesson.pathway-ks123", url.url_name)
        self.assertEqual(type(url.func), type(LessonPathwayKs123ViewSet.as_view()))

    
    def test_url_resolves_to_LessonPathwayKs123ViewSet_get__reverse(self):
        url = reverse('api.lesson.pathway-ks123', args=[127671276711, 67, 127, 76, 3, 4])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127/lessons/76/pathway-ks123/key-stage/3/topic/4", url)

