from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account is successfully created. Click below to go to the home page.')
            return redirect('signup_success')
    else:
        form = UserForm()

    return render(request, 'signup_page.html', {'form': form})


def signup_success(request):
    return render(request, 'signup_success.html')
