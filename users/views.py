import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import sessions
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.forms import ModelForm
from django.contrib import messages

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'city']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'city', 'website',]

def vet_user(message="You need to be logged in to do that."):
    def _decorated(view):
        def _view(request, *args, **kwargs):
            user = request.user
            if user is None or not user.is_authenticated():
                messages.error(request, message)
                return HttpResponseRedirect("{0}?next={1}".format(reverse('login'), request.path))
            else:
                return view(request, *args, **kwargs)
        return _view
    return _decorated

@vet_user("You need to be logged in to view your account.")
def my_account(request):
    return render(request, 'tradepaper/myaccount.html')

@vet_user("You need to be logged in to manage your account.")
def manage(request):
    return render(request, 'tradepaper/addremove.html', {'listings': user.listing_set.all()})

@vet_user("You need to be logged in to view your preferences.")
def preferences(request):
    return render(request, 'tradepaper/preferences.html')

@vet_user("You need to be logged in to edit your profile.")
def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST, instance=user, auto_id="edit%s")

    if request.method != 'POST':
        return render(request, 'tradepaper/editprofile.html', {'form': form})

    email = request.POST.get('email')
    city = request.POST.get('city')
    name = request.POST.get('name')

    if email != user.email:
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email already has an account')
            return render(request, 'tradepaper/editprofile.html', {'form': form})
    if name != user.name:
        if User.objects.filter(name=name).exists():
            messages.error(request, 'There is already a user with that name')
            return render(request, 'tradepaper/editprofile.html', {'form': form})
    if form.is_valid():
        if (email is not None):
            user.email = email
        if (city is not None):
            user.city = city
        if (name is not None):
            user.name = name
        user.save()
        messages.error(request, 'Successfully Updated!')
    else:
        messages.error(request, 'Please fill in all required fields')
    return render(request, 'tradepaper/editprofile.html', {'form': form})

@vet_user("You need to be logged in to view your requests.")
def trades(request):
    user = request.user
    sent = user.trades_sent.all()
    received = user.trades_received.all()
    return render(request, 'tradepaper/pending-requests.html', 
            {'sent_trades': sent, 'received_trades': received})

def profile(request, name):
    user = get_object_or_404(User, name=name)
    return render(request, 'tradepaper/profile.html', {'user':user})

def login(request):
    form = LoginForm(request.POST, auto_id='login%s')
    if request.method != 'POST':
        return render(request, 'tradepaper/login.html', {'form': form})
    u = authenticate(email=request.POST['email'],
                     password=request.POST['password'])
    form = LoginForm(request.POST, auto_id='login%s', instance=u)
    if u is None:
        messages.error(request, "That email and password didn't match.")
        return render(request, 'tradepaper/login.html', {
                                'form': form})
    if not(u.is_active):
        messages.error(request, "That account has been disabled.")
        return render(request, 'tradepaper/login.html', {
                                'form': form})
    # User has authenticated successfully
    auth_login(request, u)
    next = request.GET.get('next')
    if next is None:
        return HttpResponseRedirect(reverse('my_account'))
    else:
        return HttpResponseRedirect(next)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    form = UserForm(request.POST, auto_id='register%s')
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'That email already has an account')
            return render(request, 'tradepaper/register.html', {'form': form})
        elif User.objects.filter(name=request.POST['name']).exists():
            messages.error(request, 'There is already a user with that name')
            return render(request, 'tradepaper/register.html', {'form': form})
        if form.is_valid():
            u = User.objects.create_user(
                email = request.POST['email'],
                password = request.POST['password'],
                name = request.POST['name'],
                city = request.POST['city']
            )
            u.save()
            auth_user = authenticate(email=request.POST['email'],
                                    password=request.POST['password'])
            auth_login(request, auth_user)
            return HttpResponseRedirect(reverse('users:profile', args=(u.name,)))
        else:
            messages.error(request, 'Please fill in all required fields')
            return render(request, 'tradepaper/register.html', {'form': form})
    else:
        return render(request, 'tradepaper/register.html', {'form': form})
