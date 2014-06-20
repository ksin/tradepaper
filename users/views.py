import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import sessions

from django.forms import ModelForm

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]

def index(request):
    user = User.objects.get(id=request.session['user_id'])
    if user:
        return HttpResponse("Welcome %s!" % user.username)
    else:
        return HttpResponse("You're not logged in, but welcome anyway!")

def profile(request, username):
  user = get_object_or_404(User, username=username)

  return render(request, 'tradepaper/profile.html', {'user':user})

def login(request):
    # user = get_object_or_404(User, username=request.POST['username'])
    form = LoginForm(request.POST, auto_id='login%s')
    if request.method != 'POST':
        return render(request, 'tradepaper/login.html', {'form': form})
    try:
        u = User.objects.get(username=request.POST['username'])
        form = LoginForm(request.POST, auto_id='login%s', instance=u)
        if u.password == request.POST['password']:
            request.session['user_id'] = u.id
            return HttpResponseRedirect(reverse('users:profile', args=(u.username,)))
        else:
            return render(request, 'tradepaper/login.html', {
                'form': form,
                'error_message': "Your username and password didn't match."})
    except User.DoesNotExist:
        return render(request, 'tradepaper/login.html', {
            'form': form,
            'error_message': "There is no account for that username."})

def register(request):
    form = UserForm(request.POST, auto_id='register%s')
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'That username is already taken'})
        elif User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'There is already a user with that email address'})
        if form.is_valid():
            u = User.objects.create(
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
            u.save()
            return HttpResponseRedirect(reverse('users:profile', args=(u.username,)))
        else:
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'Please fill in all required fields'})
    else:
        return render(request, 'tradepaper/register.html', {'form': form})
