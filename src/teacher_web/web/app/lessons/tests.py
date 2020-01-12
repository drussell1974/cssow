from django.urls import resolve
from django.test import TestCase
from app.lessons.views import index, new, edit, copy, publish, delete, lessonplan, whiteboard, save

# Create your tests here.
class lessonPageTest(TestCase):

    def test__lesson_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/')
        self.assertEqual("lesson.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__lesson_new__url_resolves_to_new(self):
        url = resolve('/schemesofwork/127/lessons/new')
        self.assertEqual("lesson.new", url.url_name)
        self.assertEqual(url.func, new)
        

    def test__lesson_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/12/edit')
        self.assertEqual("lesson.edit", url.url_name)
        self.assertEqual(url.func, edit)

        
    def test__lesson_copy__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/13/copy')
        self.assertEqual("lesson.copy", url.url_name)
        self.assertEqual(url.func, copy)
        

    def test__lesson_publish__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/13/publish')
        self.assertEqual(url.func, publish)

        
    def test__lesson_publish__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/13/delete')
        self.assertEqual("lesson.delete_item", url.url_name)
        self.assertEqual(url.func, delete)


    def test__lesson_lessonplan__url_resolves_to_lessonplan(self):
        url = resolve('/schemesofwork/127/lessons/13/lessonplan')
        self.assertEqual("lesson.lessonplan", url.url_name)
        self.assertEqual(url.func, lessonplan)

        
    def test__lesson_whiteboard__url_resolves_to_whitebaord(self):
        url = resolve('/schemesofwork/11/lessons/44/whiteboard')
        self.assertEqual("lesson.whiteboard_view", url.url_name)
        self.assertEqual(url.func, whiteboard)
        
    
    def test__lesson_save_item__url_resolves_to_save_item(self):
        url = resolve('/schemesofwork/11/lessons/78/save')
        self.assertEqual("lesson.save", url.url_name)
        self.assertEqual(url.func, save)


