from django.test import TestCase
from .models import Crop

class CropModelTest(TestCase):

    def setUp(self):
        Crop.objects.create(name="Wheat", region="Midwest", image="wheat.jpg")
        Crop.objects.create(name="Rice", region="Southeast", image="rice.jpg")

    def test_crop_creation(self):
        wheat = Crop.objects.get(name="Wheat")
        rice = Crop.objects.get(name="Rice")
        self.assertEqual(wheat.region, "Midwest")
        self.assertEqual(rice.image, "rice.jpg")

    def test_crop_str(self):
        crop = Crop.objects.get(name="Wheat")
        self.assertEqual(str(crop), "Wheat")