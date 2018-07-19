from math import pow

from ..models import BmiModel


class BmiService(object):

    def __init__(self, weight, height):
        self.weight: float = weight
        self.height: float = height

        self.categories = {
            BmiModel.VERY_SEVERELY_UNDERWEIGHT: (0, 15),
            BmiModel.SEVERELY_UNDERWEIGHT: (15.1, 16),
            BmiModel.UNDERWEIGHT: (16.1, 18.5),
            BmiModel.NORMAL: (18.6, 25),
            BmiModel.OVERWEIGHT: (25.1, 30),
            BmiModel.OBESE_CLASS_I: (30.1, 35),
            BmiModel.OBESE_CLASS_II: (35.1, 40),
            BmiModel.OBESE_CLASS_III: (40.1, 45),
            BmiModel.OBESE_CLASS_IV: (45.1, 50),
            BmiModel.OBESE_CLASS_V: (50.1, 60),
            BmiModel.OBESE_CLASS_VI: (60.1, 1000),  # Bigger than 60
        }

    def _get_category(self, bmi):
        for category in self.categories.keys():
            _min, _max = self.categories[category]
            if _min <= bmi <= _max:
                return category

    @property
    def category(self):
        bmi = self.weight / pow(self.height, 2)
        return self._get_category(bmi)
