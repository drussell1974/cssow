from django.urls import resolve, reverse
from django.test import TestCase
from app.content.views import index, edit, delete_unpublished

class test_app_route_content_page(TestCase):

    def test__content_index__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/")
        self.assertEqual("content.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__content_index__url_resolves_to_index__reverse(self):
        url = reverse("content.index", args=[12711761271176, 1271176, 127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/", url)


    def test__content_new__url_resolves_to_new(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/new")
        self.assertEqual("content.new", url.url_name)
        self.assertEqual(url.func, edit)
        

    def test__content_new__url_resolves_to_new__reverse(self):
        url = reverse("content.new", args=[12711761271176, 1271176, 127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/new", url)


    def test__content_edit__url_resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/12/edit")
        self.assertEqual("content.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__content_edit__url_resolves_to_edit__reverse(self):
        url = reverse("content.edit", args=[12711761271176, 1271176, 127,89])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/89/edit", url)


    def test__content_delete_unpublished__url_resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/delete_unpublished")
        self.assertEqual("content.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)


    def test__content_delete_unpublished__url_resolves_to_edit__reverse(self):
        url = reverse("content.delete_unpublished", args=[12711761271176, 1271176, 127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/curriculum-content/delete_unpublished", url)
