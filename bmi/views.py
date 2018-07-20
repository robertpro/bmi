from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .models import BmiModel
from .forms import SignUpForm, BmiForm

# Create your views here.


@login_required(login_url='/login')
def bmi(request):
    if request.method == 'POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bmi')
    else:
        form = BmiForm()

    try:
        bmi = BmiModel.objects.get(user=request.user)
    except BmiModel.DoesNotExist:
        bmi = None

    context = {
        'form': form,
        'bmi': bmi,
    }
    return render(request, 'bmi/bmi.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bmi')
    else:
        form = SignUpForm()
    return render(request, 'bmi/signup.html', {'form': form})
