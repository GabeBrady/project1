from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Gabriel Brady'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/')

        else:
            error = 'Oops... the rules are the rules. Try again with valid details.'
            form = UserCreationForm

            args = {'form':form, 'error':error}
            return render(request, 'accounts/reg_form.html', args)

    else:
        form = UserCreationForm

        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}

    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)

        args = {'form':form}

        return render(request,'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile/')
        else:

            return redirect('/account/profile/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form':form}

        return render(request,'accounts/change_password.html', args)
