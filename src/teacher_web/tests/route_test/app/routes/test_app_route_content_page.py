from django.urls import resolve, reverse
from django.test import TestCase
from app.content.views import index, edit

class test_app_route_content_page(TestCase):

    def test__lesson_index__url_resolves_to_index(self):
        url = resolve("/schemesofwork/127/curriculum-content/")
        self.assertEqual("content.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__lesson_index__url_resolves_to_index__reverse(self):
        url = reverse("content.index", args=[127])
        self.assertEqual("/schemesofwork/127/curriculum-content/", url)


    def test__lesson_new__url_resolves_to_new(self):
        url = resolve("/schemesofwork/127/curriculum-content/new")
        self.assertEqual("content.new", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__lesson_new__url_resolves_to_new__reverse(self):
        url = reverse("content.new", args=[127])
        self.assertEqual("/schemesofwork/127/curriculum-content/new", url)


    def test__lesson_edit__url_resolves_to_edit(self):
        url = resolve("/schemesofwork/127/curriculum-content/12/edit")
        self.assertEqual("content.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__lesson_edit__url_resolves_to_edit__reverse(self):
        url = reverse("content.edit", args=[127,89])
        self.assertEqual("/schemesofwork/127/curriculum-content/89/edit", url)