from django.urls import resolve, reverse
from django.test import TestCase
from app.learningobjectives.views import index, new, edit, delete_unpublished, save, publish_item

# Create your tests here.
class test_app_route_learningobjectives_page(TestCase):
    def test__learningobjective_index__url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/')
        self.assertEqual("learningobjective.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__learningobjective_index__url_resolves_to_index__reverse(self):
        url = reverse("learningobjective.index", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/", url)


    def test__learningobjective_edit__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/1/edit')
        self.assertEqual("learningobjective.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__learningobjective_edit__url_resolves_to_edit__reverse(self):
        url = reverse("learningobjective.edit", args=[12711761271176, 1271176, 127, 32, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/1/edit", url)


    def test__learningobjective_new__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/new')
        self.assertEqual("learningobjective.new", url.url_name)
        self.assertEqual(url.func, new)

    
    def test__learningobjective_new__url_resolves_to_edit__reverse(self):
        url = reverse("learningobjective.new", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/new", url)
    

    def test__learningobjective_save__url_resolves_to_save(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/99/save')
        self.assertEqual("learningobjective.save", url.url_name)
        self.assertEqual(url.func, save)

    
    def test__learningobjective_save__url_resolves_to_save__reverse(self):
        url = reverse("learningobjective.save", args=[12711761271176, 1271176, 127, 32, 99])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/99/save", url)


    def test__learningobjective_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/delete_unpublished')
        self.assertEqual("learningobjective.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)

    
    def test__learningobjective_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("learningobjective.delete_unpublished", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/learning-objectives/delete_unpublished", url)
    
    
    def test__learningobjective_publish__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/learning-objectives/348/publish")
        self.assertEqual("learningobjective.publish_item", url.url_name)
        self.assertEqual(url.func, publish_item)


    def test__learningobjective_publish__url_resolves_to_index__reverse(self):
        url = reverse("learningobjective.publish_item", args=[12711761271176, 1271176, 127,13,348])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/learning-objectives/348/publish", url)
