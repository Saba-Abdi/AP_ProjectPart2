from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm

# This view function handles the user sign up process using a form
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

# This view function renders the sign up success page
def signup_success(request):
    return render(request, 'signup_success.html')
