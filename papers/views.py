from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def browse(request):
    return render(request, 'paperapp/browse.html')
