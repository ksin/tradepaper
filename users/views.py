import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import ModelForm

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]

def index(request):
  return HttpResponse("This is the user index.")

def profile(request, username):
  user = get_object_or_404(User, username=username)
  return render(request, 'paperapp/profile.html', {'user':user})

def login(request):
    return render(request, 'paperapp/login.html')

def register(request):
    form = UserForm(request.POST, auto_id='signup_%s')
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists()
            return render(request, 'paperapp/signup.html', {
                'form': form,
                'error_message': 'That username is already taken'})
        else if User.objects.filter(email=request.POST['email']).exists()
            return render(request, 'paperapp/signup.html', {
                'form': form,
                'error_message': 'There is already a user with that email address'})
        if form.is_valid():
            u = User.objects.create(
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password'],
                joindate=datetime.datetime.now(),
            )
            u.save()
            return HttpResponseRedirect(reverse('users:profile', args=(u.username,)))
        else:
            return render(request, 'paperapp/signup.html', {
                'form': form,
                'error_message': 'Please fill in all required fields'})
    else:
        return render(request, 'paperapp/signup.html', {'form': form})
