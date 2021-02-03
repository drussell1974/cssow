from django.urls import resolve, reverse
from django.test import TestCase
from app.eventlogs.views import index, delete

# Create your tests here.
class test_app_route_eventlog_page(TestCase):

    def test_eventlog_index_url_resolves_to_index(self):
        url = resolve('/schemesofwork/99/event-log/')
        self.assertEqual("eventlog.index", url.url_name)
        self.assertEquals(url.func, index)

    
    def test_eventlog_index_resolves_to_index__reverse(self):
        url = reverse("eventlog.index", args=[99])
        self.assertEqual("/schemesofwork/99/event-log/", url)


    def test_eventlog_delete_url_resolves_to_delete(self):
        url = resolve('/schemesofwork/99/event-log/delete')
        self.assertEqual("eventlog.delete", url.url_name)
        self.assertEquals(url.func, delete)

    
    def test_eventlog_delete_resolves_to_delete__reverse(self):
        url = reverse("eventlog.delete", args=[98])
        self.assertEqual("/schemesofwork/98/event-log/delete", url)



        