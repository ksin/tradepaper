from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'paperapp/home.html')

def about(request):
    return render(request, 'paperapp/about.html')
