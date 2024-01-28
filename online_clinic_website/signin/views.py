from django.shortcuts import render, redirect
from django.contrib import messages
from signup.models import User


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_position = request.POST['user_position']

        user = User.objects.filter(username=username, password=password, position=user_position)

        if user:
            request.session['username'] = username
            request.session['user_position'] = user_position
            if user_position == 'patient':
                return render(request, 'patient_profile.html',
                              {'message': 'You successfully logged in.'})
            else:
                return render(request, 'secretary_profile.html',
                              {'message': 'You successfully logged in.'})
        else:
            return render(request, 'signin_first.html', {
                'message': 'There is no user with this information. Please try again.'})

    else:
        return render(request, 'signin_first.html')


def secretary_page(request):
    if 'username' in request.session and 'user_position' in request.session:
        if request.session['user_position'] == 'secretary':
            username = request.session['username']
            user_position = request.session['user_position']
            return render(request, 'secretary_profile_page.html', {'username': username, 'user_position': user_position})
        else:
            return redirect('signin')
    else:
        return redirect('signin')


def patient_page(request):
    if 'username' in request.session and 'user_position' in request.session:
        if request.session['user_position'] == 'patient':
            username = request.session['username']
            user_position = request.session['user_position']
            return render(request, 'patient_profile_page.html', {'username': username, 'user_position': user_position})
        else:
            return redirect('signin')
    else:
        return redirect('signin')