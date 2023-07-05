from django.shortcuts import render, redirect, redirect
from django.db.models import Q, Case, When, IntegerField
from django.contrib.auth.decorators import login_required
from lmsapp.forms import PackageForm
from lmsapp.models import Package, User
import random
import string
from lmsapp.utils import get_time_of_day
from django.shortcuts import redirect
from django.contrib import messages


"""
Renders out a sender dashboard template and shows packages with the statuses 
'ongoing' & 'upcoming' that are for a specific sender.
"""
@login_required
def sender_dashboard(request):
    packages = Package.objects.filter(
        Q(status='ongoing') | Q(status='upcoming')
    ).order_by(
        Case(
            When(status='upcoming', then=0),
            When(status='ongoing', then=1),
            default=2,
            output_field=IntegerField()
        ),
        '-created_at'  # Sort by creation day in descending order
    )

    greeting_message = get_time_of_day()
    context = {
        'greeting_message': greeting_message,
        'packages': packages
        }
    return render(request, 'sender/sender_dashboard.html', context)

"""  
Handles the registration of new packages by senders, ensuring the form data is valid 
and saving the package to the database with the appropriate details.
""" 
def register_package(request):
    drop_pick_zones = User.objects.filter(role='drop_pick_zone') 

    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.user
            package.package_number = generate_package_number()
            
            # Check if the selected courier is already assigned to a package
            courier = package.courier
            if courier and courier.assigned_packages.exists():
                messages.error(request, 'Selected courier is already assigned to a package.')
                return redirect('register_package')
            
            package.status = 'upcoming'
            package.save()
            return redirect('sender_dashboard')
        else:
            error_message = 'Error processing your request'
    else:
        form = PackageForm()
        error_message = None

    return render(request, 'sender/register_package.html', {'form': form, 'error_message': error_message, 'drop_pick_zones': drop_pick_zones})

# Generates a random selection of five digits, concatenated with pn to work as the package number
def generate_package_number():
    prefix = 'pn'
    digits = ''.join(random.choices(string.digits, k=5))
    return f'{prefix}{digits}'

# Renders the 'sender_history.html' template which should display all the packages that a sender has interacted with
def sender_history(request):
    return render(request, 'sender/sender_history.html', {})
