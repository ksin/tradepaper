from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from paperapp.models import User

def index(request):
  return HttpResponse("This is the user index.")

def profile(request, username):
  user = get_object_or_404(User, username=username)
  return render(request, 'paperapp/profile.html', {'user':user})
