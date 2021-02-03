from django.urls import resolve, reverse
from django.test import TestCase
from app.lessons.views import index, edit, publish, delete, whiteboard, delete_unpublished

# Create your tests here.
class test_app_route_lesson_page(TestCase):

    def test__lesson_index__url_resolves_to_index(self):
        url = resolve("/schemesofwork/127/lessons/")
        self.assertEqual("lesson.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__lesson_index__url_resolves_to_index__reverse(self):
        url = reverse("lesson.index", args=[127])
        self.assertEqual("/schemesofwork/127/lessons/", url)


    def test__lesson_view__url_resolves_to_index(self):
        url = resolve("/schemesofwork/127/lessons/220")
        self.assertEqual("lesson.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__lesson_view__url_resolves_to_index__reverse(self):
        url = reverse("lesson.view", args=[11,220])
        self.assertEqual("/schemesofwork/11/lessons/220", url)


    def test__lesson_new__url_resolves_to_new(self):
        url = resolve("/schemesofwork/127/lessons/new")
        self.assertEqual("lesson.new", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__lesson_new__url_resolves_to_new__reverse(self):
        url = reverse("lesson.new", args=[127])
        self.assertEqual("/schemesofwork/127/lessons/new", url)


    def test__lesson_edit__url_resolves_to_edit(self):
        url = resolve("/schemesofwork/127/lessons/12/edit")
        self.assertEqual("lesson.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__lesson_edit__url_resolves_to_edit__reverse(self):
        url = reverse("lesson.edit", args=[127,12])
        self.assertEqual("/schemesofwork/127/lessons/12/edit", url)


    def test__lesson_copy__url_resolves_to_edit(self):
        url = resolve("/schemesofwork/127/lessons/13/copy")
        self.assertEqual("lesson.copy", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__lesson_copy__url_resolves_to_edit__reverse(self):
        url = reverse("lesson.copy", args=[127, 13])
        self.assertEqual("/schemesofwork/127/lessons/13/copy", url)
    

    def test__lesson_publish__url_resolves_to_index(self):
        url = resolve("/schemesofwork/127/lessons/13/publish")
        self.assertEqual("lesson.publish_item", url.url_name)
        self.assertEqual(url.func, publish)


    def test__lesson_publish__url_resolves_to_index__reverse(self):
        url = reverse("lesson.publish_item", args=[127,13])
        self.assertEqual("/schemesofwork/127/lessons/13/publish", url)


    def test__lesson_whiteboard__url_resolves_to_whitebaord(self):
        url = resolve("/schemesofwork/11/lessons/44/whiteboard")
        self.assertEqual("lesson.whiteboard_view", url.url_name)
        self.assertEqual(url.func, whiteboard)
        
    
    def test__lesson_whiteboard__url_resolves_to_whitebaord__reverse(self):
        url = reverse("lesson.whiteboard_view", args=[11, 44])
        self.assertEqual("/schemesofwork/11/lessons/44/whiteboard", url)

    
    def test__lesson_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve("/schemesofwork/11/lessons/delete_unpublished")
        self.assertEqual("lesson.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)
        
    
    def test__lesson_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("lesson.delete_unpublished", args=[11])
        self.assertEqual("/schemesofwork/11/lessons/delete_unpublished", url)