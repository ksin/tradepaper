import datetime
import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import ModelForm

from users.models import User

logger = logging.getLogger('user')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'joindate']

def index(request):
  return HttpResponse("This is the user index.")

def profile(request, username):
  user = get_object_or_404(User, username=username)
  return render(request, 'paperapp/profile.html', {'user':user})

def login(request):
    return render(request, 'paperapp/login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, auto_id='signup_%s')
        form.joindate = datetime.datetime.now()
        if form.is_valid():
            new_user = form.save()
            logger.debug('User Registration was valid. Redirecting to profile')
            return profile(request, new_user.username)
        else:
            logger.debug('User Registration was not valid')
    else:
        form = UserForm() # An unbound form
        logger.debug('Request method was not POST')

    return render(request, 'paperapp/signup.html', {'form': form,})
