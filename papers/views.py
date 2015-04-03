from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django import forms

from papers.models import Listing, Request
from users.models import User
from users.views import vet_user

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'edition', 'condition', 'image']

def browse(request):
    listings = Listing.objects.all()
    if (listings == None):
        raise Http404
    return render(request, 'tradepaper/browse.html', {'listings' : listings})

def listing(request, id):
    l = get_object_or_404(Listing, id=id)
    return render(request, 'tradepaper/single-paper.html', {'listing':l})

@vet_user("You need to be logged in to create a listing.")
def new_listing(request):
    user = request.user
    form = ListingForm(request.POST, request.FILES, auto_id='new_listing_%s')
    if request.method == 'POST':
        if form.is_valid():
            l = Listing.objects.create(
                title = request.POST['title'],
                edition = request.POST['edition'],
                condition = request.POST['condition'],
                image = request.FILES['image'],
                user = user
            )
            l.save()
            return HttpResponseRedirect(reverse('papers:listing', args=(l.id,)))
        else:
            messages.error(request, 'Please fill in all required fields')
            return render(request, 'tradepaper/new-listing.html', {'form': form})
    else:
        return render(request, 'tradepaper/new-listing.html')

def request(request, id):
    r = get_object_or_404(Request, id=id)
    return render(request, 'tradepaper/trade-request.html', {'request': r})

@vet_user("You need to be logged in to make a trade request.")
def new_request(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    user = request.user
    # create request, but don't save it until it's posted
    r = Request(
            requester = user,
            requestee = listing.user,
            listing = listing
            )
    if request.method == 'POST':
        r.save()
        return HttpResponseRedirect(reverse('papers:request', args=(r.id,)))
    else:
        return render(request, 'tradepaper/trade-request.html', {'request': r})
