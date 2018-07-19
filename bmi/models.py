from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BmiModel(models.Model):
    VERY_SEVERELY_UNDERWEIGHT = 1
    SEVERELY_UNDERWEIGHT = 2
    UNDERWEIGHT = 3
    NORMAL = 4
    OVERWEIGHT = 5
    OBESE_CLASS_I = 6
    OBESE_CLASS_II = 7
    OBESE_CLASS_III = 8
    OBESE_CLASS_IV = 9
    OBESE_CLASS_V = 10
    OBESE_CLASS_VI = 11

    CATEGORY_CHOICES = (
        (VERY_SEVERELY_UNDERWEIGHT, "Very severely underweight"),
        (SEVERELY_UNDERWEIGHT, "Severely underweight "),
        (UNDERWEIGHT, "Underweight"),
        (NORMAL, "Normal (healthy weight) "),
        (OVERWEIGHT, "Overweight"),
        (OBESE_CLASS_I, "Obese Class I (Moderately obese) "),
        (OBESE_CLASS_II, "Obese Class II (Severely obese) "),
        (OBESE_CLASS_III, "Obese Class III (Very severely obese)"),
        (OBESE_CLASS_IV, "Obese Class IV (Morbidly Obese) "),
        (OBESE_CLASS_V, "Obese Class V (Super Obese) "),
        (OBESE_CLASS_VI, "Obese Class VI (Hyper Obese) "),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField()
