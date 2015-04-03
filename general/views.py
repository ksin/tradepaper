from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'tradepaper/home.html')

def about(request):
    return render(request, 'tradepaper/about.html')

def faq(request):
    return render(request, 'tradepaper/faq.html')

def shipping(request):
    return render(request, 'tradepaper/shippinginstructions.html')

def reset_password(request):
    return render(request, 'tradepaper/resetpassword.html')

def reset_link(request):
    return render(request, 'tradepaper/resetpasswordhere.html')
