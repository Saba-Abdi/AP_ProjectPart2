from django.shortcuts import render, redirect
from django.contrib import messages
from signup.models import User
from signin.models import Clinic, Transaction, CapacityIncrease


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


def reserving_appointment(request):
    clinics = Clinic.objects.all()
    return render(request, 'reserve_appointment_first.html', {'clinics': clinics})


def payment_page(request):
    if 'username' in request.session and 'clinic' in request.POST:
        username = request.session['username']
        clinic_id = request.POST['clinic']
        has_insurance = 'insurance' in request.POST and request.POST['insurance'] == 'on'

        clinic = Clinic.objects.get(id=clinic_id)
        visit_cost = clinic.cost
        if has_insurance:
            visit_cost *= 0.8  # apply 20% discount

        return render(request, 'payment_page.html', {
            'username': username,
            'clinic_name': clinic.name,
            'visit_cost': visit_cost,
        })
    else:
        return redirect('patient_page')


def pay(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        visit_cost = request.POST.get('visit_cost')
        clinic_name = request.POST.get('clinic_name')

        context = {
            'username': username,
            'visit_cost': visit_cost,
            'clinic_name': clinic_name,
        }

        return render(request, 'gateway.html', context)


def payment_success(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        visit_cost = request.POST.get('visit_cost')
        clinic_name = request.POST.get('clinic_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv2 = request.POST.get('cvv2')

        Transaction.objects.create(username=username, clinic_name=clinic_name, amount_paid=visit_cost)

        # Reduce the clinic's capacity by 1
        clinic = Clinic.objects.get(name=clinic_name)
        clinic.capacity -= 1
        clinic.save()

        context = {
            'username': username,
            'clinic_name': clinic_name,
            'visit_cost': visit_cost
        }

        return render(request, 'payment_successful.html', context)
    else:
        return redirect('patient_page')
def previous_appointments(request):
    username = request.session.get('username')
    if username is not None:
        user_appointments = Transaction.objects.filter(username=username)
        return render(request, 'previous_appointments.html',
                      {'appointments': user_appointments})
    else:
        return redirect('signin')


def current_appointment(request):
    username = request.session.get('username')
    if username is not None:
        the_current_appointment = Transaction.objects.filter(
            username=username).last()
        return render(request, 'current_appointment.html',
                      {'appointment': the_current_appointment})
    else:
        return redirect('signin')


def increase_capacity_info(request):
    username = request.session.get('username')
    if username is not None:
        return render(request, 'increase_capacity.html', {'username': username})
    else:
        return redirect('signin')


def increase_capacity(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        clinic_name = request.POST.get('clinic_name')
        increase_amount = int(request.POST.get('increase_amount'))

        try:
            clinic = Clinic.objects.get(name=clinic_name)
            clinic.capacity += increase_amount
            clinic.save()

            # Create a new CapacityIncrease record
            CapacityIncrease.objects.create(username=username, clinic_name=clinic_name, increase_amount=increase_amount)

            context = {
                'username': username,
                'clinic_name': clinic_name,
                'new_capacity': clinic.capacity,
            }

            return render(request, 'increase_capacity_success.html', context)
        except Clinic.DoesNotExist:
            context = {
                'username': username,
                'message': 'There is no clinic with this information. Please try again.',
            }
            return render(request, 'increase_capacity.html', context)
    else:
        return render(request, 'increase_capacity.html')


def current_appointments_info(request):
    username = request.session.get('username')
    if username is not None:
        return render(request, 'clinic_appointments_info.html')
    else:
        return redirect('signin')


def get_clinic_appointments(request):
    if request.method == 'POST':
        clinic_name = request.POST.get('clinic_name')
        try:
            clinic = Clinic.objects.get(name=clinic_name)
            transactions = Transaction.objects.filter(clinic_name=clinic_name)
            return render(request, 'get_clinic_appointments.html',
                          {'transactions': transactions})
        except Clinic.DoesNotExist:
            context = {
                'message': 'There is no clinic with this information. Please try again.',
            }
            return render(request, 'clinic_appointments_info.html', context)
    else:
        return render(request, 'clinic_appointments_info.html')
