from django.urls import resolve
from django.test import TestCase
from app.learningepisode.views import index, new, edit, copy, publish, delete, lessonplan, whiteboard

# Create your tests here.
class LearningEpisodePageTest(TestCase):

    def test__learningepisode_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/')
        self.assertEqual(url.func, index)


    def test__learningepisode_new__url_resolves_to_new(self):
        url = resolve('/schemesofwork/127/lessons/new')
        self.assertEqual(url.func, new)
        

    def test__learningepisode_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/12/edit')
        self.assertEqual(url.func, edit)

        
    def test__learningepisode_copy__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/13/copy')
        self.assertEqual(url.func, copy)
        

    def test__learningepisode_publish__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/13/publish')
        self.assertEqual(url.func, publish)

        
    def test__learningepisode_publish__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/13/delete')
        self.assertEqual(url.func, delete)


    def test__learningepisode_lessonplan__url_resolves_to_lessonplan(self):
        url = resolve('/schemesofwork/127/lessons/13/lessonplan')
        self.assertEqual(url.func, lessonplan)

        
    def test__learningepisode_whiteboard__url_resolves_to_whitebaord(self):
        url = resolve('/schemesofwork/11/lessons/44/whiteboard')
        self.assertEqual(url.func, whiteboard)
        