from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms import ModelForm

from papers.models import Listing
from users.models import User

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'edition', 'condition']

def browse(request):
    return render(request, 'tradepaper/browse.html')

def listing(request, id):
    l = get_object_or_404(Listing, id=id)
    return render(request, 'tradepaper/single-paper.html', {'listing':l})

def new_listing(request):
    user = request.user
    form = ListingForm(request.POST, auto_id='new_listing%s')
    if request.method == 'POST':
        if form.is_valid():
            l = Listing.objects.create(
                title = request.POST['title'],
                edition = request.POST['edition'],
                condition = request.POST['condition'],
                # image_url = request.POST['image_url'],
                user = user
            )
            l.save()
            return HttpResponseRedirect(reverse('papers:listing', args=(l.id,)))
            # return HttpResponseRedirect(listing(request, l.id))
        else:
            messages.error(request, 'Please fill in all required fields')
            return render(request, 'tradepaper/new-listing.html', {'form': form})
    else:
        if user.is_authenticated():
            return render(request, 'tradepaper/new-listing.html')
        else:
            messages.error(request, "You need to be logged in to create a listing.")
            return HttpResponseRedirect(reverse('login'))
