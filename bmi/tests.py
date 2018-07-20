from django.test import TestCase
from django.contrib.auth.models import User

from .models import BmiModel
from .services.bmi import BmiService

# Create your tests here.


class BmiModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def test_create_valid(self):
        BmiModel.objects.create(user=self.user, category=BmiModel.NORMAL)
        bmi = BmiModel.objects.get(user=self.user)
        self.assertEqual(bmi.user, self.user)
        self.assertEqual(bmi.category, BmiModel.NORMAL)


class BmiServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def test_category(self):
        bmi_test_data = {
            # Category: (Weight, Height)
            BmiModel.VERY_SEVERELY_UNDERWEIGHT: (30, 1.5),
            BmiModel.SEVERELY_UNDERWEIGHT: (35, 1.5),
            BmiModel.UNDERWEIGHT: (40, 1.5),
            BmiModel.NORMAL: (50, 1.5),
            BmiModel.OVERWEIGHT: (60, 1.5),
            BmiModel.OBESE_CLASS_I: (70, 1.5),
            BmiModel.OBESE_CLASS_II: (80, 1.5),
            BmiModel.OBESE_CLASS_III: (90.5, 1.5),
            BmiModel.OBESE_CLASS_IV: (110, 1.5),
            BmiModel.OBESE_CLASS_V: (120, 1.5),
            BmiModel.OBESE_CLASS_VI: (200, 1.5),  # Bigger than 60
        }

        for k in bmi_test_data.keys():
            weight, height = bmi_test_data[k]
            category = BmiService(weight, height).category
            self.assertEqual(category, k)
