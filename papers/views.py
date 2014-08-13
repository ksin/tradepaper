from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from papers.models import Listing
from users.models import User

def browse(request):
    return render(request, 'tradepaper/browse.html')

def listing(request, name, title, edition):
    u = get_object_or_404(User, name=name)
    listing = get_object_or_404(Listing, user=u, title=title, edition=edition)
    return render(request, 'tradepaper/single-paper.html', {'listing': listing})
