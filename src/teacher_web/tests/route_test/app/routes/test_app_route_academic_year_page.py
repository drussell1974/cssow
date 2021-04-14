from django.urls import resolve, reverse
from django.test import TestCase
from app.academic_years.views import edit, index, change

# Create your tests here.
class test_app_route_institute_page(TestCase):

    def test__academic_years__url_resolves_to_index(self):
        url = resolve("/institute/12711761277611/academic-years/")
        self.assertEqual("academic-year.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__academic_years__url_resolves_to_index__reverse(self):
        url = reverse("academic-year.index", args=[12711761277611])
        self.assertEqual("/institute/12711761277611/academic-years/", url)

        
    def test__academic_years_new__resolves_to_new(self):
        url = resolve("/institute/12711761277611/academic-years/new")
        self.assertEqual("academic-year.new", url.url_name)
        self.assertEqual(url.func, edit)


    def test__academic_years_new__resolves_to_new__reverse(self):
        url = reverse("academic-year.new", args=[12711761277611])
        self.assertEqual("/institute/12711761277611/academic-years/new", url)


    def test__academic_years_edit__resolves_to_edit(self):
        url = resolve("/institute/12711761277611/academic-years/2021/edit")
        self.assertEqual("academic-year.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__academic_years_edit__resolves_to_edit__reverse(self):
        url = reverse("academic-year.edit", args=[12711761277611, 2021])
        self.assertEqual("/institute/12711761277611/academic-years/2021/edit", url)

        
    def test_change_academic_year__url_resolves_to_change_academic_year(self):
        url = resolve('/institute/12711761277611/academic-years/change')
        self.assertEqual("default.academic-year", url.url_name)
        self.assertEquals(url.func, change)

    
    def test_change_academic_year_url_resolves_to_change_academic_year__reverse(self):
        url = reverse("default.academic-year", args=[12711761277611])
        self.assertEqual("/institute/12711761277611/academic-years/change", url)