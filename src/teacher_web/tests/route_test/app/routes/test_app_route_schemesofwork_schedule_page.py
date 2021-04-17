from django.urls import resolve, reverse
from django.test import TestCase
from app.schemesofwork_schedule.views import index #, edit, delete_unpublished, schedule

# Create your tests here.
class test_app_route_schemesofwork_schedule_page(TestCase):

    
    def test__schemesofwork_schedule__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/11/schedules")
        self.assertEqual("schemesofwork_schedule.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_schedule__url_resolves_to_index__reverse(self):
        url = reverse("schemesofwork_schedule.index",  args=[12711761271176,1271176, 11])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/11/schedules", url)
    
