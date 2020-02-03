from django.test import TestCase
from .models import Images, Location,Category

# Create your tests here.

class LocationTest(TestCase):
    def setUp(self):
        self.location = Location(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
