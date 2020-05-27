from django.test import TestCase, Client
from django.urls import reverse

from .models import *

class DepartmentTestCase(TestCase):
    def setUp(self):
        Show.objects.create(title="Show 1", department=Department.objects.create(name="Lighting"), sort_order=1)
        Show.objects.create(title="Show 2", department=Department.objects.create(name="Scenic"), sort_order=2)

    def test_to_str(self):
        lx = Department.objects.get(name="Lighting")

        self.assertEqual(str(lx), 'Lighting')

    def test_get_shows(self):
        lx = Department.objects.get(name="Lighting")
        self.assertQuerysetEqual(
            lx.getShows(),
            ['<Show: Show 1>'])

class ShowTestCase(TestCase):
    def setUp(self):
        Show.objects.create(title="Show 1", department=Department.objects.create(name="Lighting"), sort_order=1)
        Show.objects.create(title="Show 2", department=Department.objects.create(name="Scenic"), sort_order=2)


    def test_index_view_performance(self):

        with self.assertNumQueries(6):
            response = self.client.get(reverse('portfolio:index'))

        self.assertEqual(response.context["show_list"], 2)