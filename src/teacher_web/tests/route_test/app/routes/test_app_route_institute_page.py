from django.urls import resolve, reverse
from django.test import TestCase
from app.institute.views import edit, all, index, delete_unpublished, schedule

# Create your tests here.
class test_app_route_institute_page(TestCase):

    def test__institute__url_resolves_to_index(self):
        url = resolve("/institute/")
        self.assertEqual("institute.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__institute__url_resolves_to_index__reverse(self):
        url = reverse("institute.index")
        self.assertEqual("/institute/", url)


    def test__institute__url_resolves_to_all(self):
        url = resolve("/institute/all")
        self.assertEqual("institute.all", url.url_name)
        self.assertEqual(url.func, all)


    def test__institute__url_resolves_to_all__reverse(self):
        url = reverse("institute.all")
        self.assertEqual("/institute/all", url)
    
    
    def test__department__url_resolves_to_schedule(self):
        url = resolve("/institute/12711761271176/schedule")
        self.assertEqual("institute.schedule", url.url_name)
        self.assertEqual(url.func, schedule)


    def test__department__url_resolves_to_schedule__reverse(self):
        url = reverse("institute.schedule", args=[12711761271176])
        self.assertEqual("/institute/12711761271176/schedule", url)
    
        
    def test__institute_new__resolves_to_new(self):
        url = resolve("/institute/new")
        self.assertEqual("institute.new", url.url_name)
        self.assertEqual(url.func, edit)


    def test__institute_new__resolves_to_new__reverse(self):
        url = reverse("institute.new")
        self.assertEqual("/institute/new", url)


    def test__institute_view__resolves_to_view(self):
        url = resolve("/institute/12711761271176")
        self.assertEqual("institute.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__institute_view__resolves_to_view__reverse(self):
        url = reverse("institute.view", args=[12711761271176])
        self.assertEqual("/institute/12711761271176", url)


    def test__institute_edit__resolves_to_edit(self):
        url = resolve("/institute/127/edit")
        self.assertEqual("institute.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__institute_edit__resolves_to_edit__reverse(self):
        url = reverse("institute.edit", args=[127])
        self.assertEqual("/institute/127/edit", url)


    def test__institute_delete_unpublished__resolves_to_delete_unpublished(self):
        url = resolve("/institute/delete_unpublished")
        self.assertEqual("institute.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)


    def test__institute_delete_unpublished__resolves_to_delete_unpublished__reverse(self):
        url = reverse("institute.delete_unpublished")
        self.assertEqual("/institute/delete_unpublished", url)


    def test__institute_publish_item__resolves_to_publish(self):
        url = resolve("/institute/127/publish")
        self.assertEqual("institute.publish_item", url.url_name)
        self.assertEqual(url.func, index)


    def test__institute_publish_item__resolves_to_publish__reverse(self):
        url = reverse("institute.publish_item", args=[127])
        self.assertEqual("/institute/127/publish", url)
