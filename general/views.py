from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'paperapp/index.html')

def about(request):
    return render(request, 'paperapp/about.html')
