from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .services.bmi import BmiService
from .models import BmiModel


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class BmiForm(forms.Form):
    weight = forms.FloatField(help_text='Weight in Kg')
    height = forms.FloatField(help_text='Height in meters')

    def save(self, user: User):
        weight = self.cleaned_data.get('weight')
        height = self.cleaned_data.get('height')

        category = BmiService(weight, height).category

        try:
            bmi = BmiModel.objects.get(user=user)
            bmi.category = category
        except BmiModel.DoesNotExist:
            bmi = BmiModel.objects.create(user=user, category=category)

        bmi.save()
