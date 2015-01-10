from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django import forms

from papers.models import Listing
from users.models import User

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
        if user.is_authenticated():
            return render(request, 'tradepaper/new-listing.html')
        else:
            messages.error(request, "You need to be logged in to create a listing.")
            return HttpResponseRedirect(reverse('login'))
