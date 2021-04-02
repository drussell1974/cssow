from django.urls import resolve, reverse
from django.test import TestCase
from app.lesson_schedules.views import edit # index, publish, delete, whiteboard, missing_words_challenge, delete_unpublished

# Create your tests here.
class test_app_route_lesson_schedule_page(TestCase):

    '''
    def test__lesson_schedule_index__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/")
        self.assertEqual("lesson_schedule.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__lesson_schedule_index__url_resolves_to_index__reverse(self):
        url = reverse("lesson_schedule.index", args=[12711761271176, 1271176, 127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/", url)
    '''

    def test__lesson_schedule_new__url_resolves_to_new(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/220/schedules/new")
        self.assertEqual("lesson_schedule.new", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__lesson_schedule_new__url_resolves_to_new__reverse(self):
        url = reverse("lesson_schedule.new", args=[12711761271176, 1271176, 127, 220])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/220/schedules/new", url)

    '''
    def test__lesson_schedule_edit__url_resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/12/edit")
        self.assertEqual("lesson_schedule.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__lesson_schedule_edit__url_resolves_to_edit__reverse(self):
        url = reverse("lesson_schedule.edit", args=[12711761271176, 1271176, 127,12])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/12/edit", url)
    '''

    '''
    def test__lesson_schedule_copy__url_resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/copy")
        self.assertEqual("lesson_schedule.copy", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__lesson_schedule_copy__url_resolves_to_edit__reverse(self):
        url = reverse("lesson_schedule.copy", args=[12711761271176, 1271176, 127, 13])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/copy", url)
    '''

    '''
    def test__lesson_schedule_whiteboard__url_resolves_to_whitebaord(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/44/whiteboard")
        self.assertEqual("lesson_schedule.whiteboard_view", url.url_name)
        self.assertEqual(url.func, whiteboard)
        
    
    def test__lesson_schedule_whiteboard__url_resolves_to_whitebaord__reverse(self):
        url = reverse("lesson_schedule.whiteboard_view", args=[12711761271176, 1271176, 11, 44])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/44/whiteboard", url)

    
    def test__lesson_schedule_missing_words_challenge__url_resolves_to_whitebaord(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/7907/learning-objectives/missing-words")
        self.assertEqual("lesson_schedule.missing_words_challenge_view", url.url_name)
        self.assertEqual(url.func, missing_words_challenge)
        
    
    def test__lesson_schedule_missing_words_challenge__url_resolves_to_whitebaord__reverse(self):
        url = reverse("lesson_schedule.missing_words_challenge_view", args=[12711761271176, 1271176, 11, 7907])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/7907/learning-objectives/missing-words", url)
    '''