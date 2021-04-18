from django.urls import resolve, reverse
from django.test import TestCase
from app.topic.views import index, edit #delete_item, delete_unpublished, publish_item

# Create your tests here.
class test_app_route_topic_page(TestCase):
    
    def test__topic_index__url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/topics/')
        self.assertEqual("topic.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__topic_index__url_resolves_to_index__reverse(self):
        url = reverse("topic.index", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/topics/", url)


    def test__topic_edit__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/topics/1/edit')
        self.assertEqual("topic.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__topic_edit__url_resolves_to_edit__reverse(self):
        url = reverse("topic.edit", args=[12711761271176, 1271176, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/topics/1/edit", url)


    def test__topic_new__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/topics/new')
        self.assertEqual("topic.new", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__topic_new__url_resolves_to_edit__reverse(self):
        url = reverse("topic.new", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/topics/new", url)
    