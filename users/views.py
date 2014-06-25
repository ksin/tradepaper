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
        fields = ['email', 'password', 'name', 'city']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]

def index(request):
    user = User.objects.get(id=request.session['user_id'])
    if user:
        return HttpResponse("Welcome %s!" % user.name)
    else:
        return HttpResponse("You're not logged in, but welcome anyway!")

def profile(request, name):
  user = get_object_or_404(User, name=name)

  return render(request, 'tradepaper/profile.html', {'user':user})

def login(request):
    form = LoginForm(request.POST, auto_id='login%s')
    if request.method != 'POST':
        return render(request, 'tradepaper/login.html', {'form': form})
    try:
        u = User.objects.get(email=request.POST['email'])
        form = LoginForm(request.POST, auto_id='login%s', instance=u)
        if u.password == request.POST['password']:
            request.session['user_id'] = u.id
            return HttpResponseRedirect(reverse('users:profile', args=(u.name,)))
        else:
            return render(request, 'tradepaper/login.html', {
                'form': form,
                'error_message': "Your email and password didn't match."})
    except User.DoesNotExist:
        return render(request, 'tradepaper/login.html', {
            'form': form,
            'error_message': "There is no account for that email."})

def register(request):
    form = UserForm(request.POST, auto_id='register%s')
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'That email already has an account'})
        elif User.objects.filter(name=request.POST['name']).exists():
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'There is already a user with that name'})
        if form.is_valid():
            u = User.objects.create(
                email = request.POST['email'],
                password = request.POST['password'],
                name = request.POST['name'],
                city = request.POST['city']
            )
            u.save()
            return HttpResponseRedirect(reverse('users:profile', args=(u.name,)))
        else:
            return render(request, 'tradepaper/register.html', {
                'form': form,
                'error_message': 'Please fill in all required fields'})
    else:
        return render(request, 'tradepaper/register.html', {'form': form})
