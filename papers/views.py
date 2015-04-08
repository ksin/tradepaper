from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django import forms

from papers.models import Listing, Request, Message
from users.models import User
from users.views import vet_user

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'edition', 'condition', 'image']

class RequestForm(forms.Form):
    message = forms.CharField(max_length=4096)

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

def request(request, id=None, trade_request=None):
    if trade_request is None:
        if id is None:
            raise Http404
        else:
            trade_request = get_object_or_404(Request, id=id)
    user = request.user
    if user not in [trade_request.requester, trade_request.requestee]:
        raise Http404
    if request.method == 'POST':
        text = request.POST.get('message')
        form = RequestForm(request.POST, auto_id=False)
        cancelled = 'cancel_trade' in request.POST
        if form.is_valid() and text and not cancelled:
            message = trade_request.messages.create(
                    text = text,
                    sent_by_requester = True
                    )
            message.save()
            return HttpResponseRedirect(reverse('papers:request', args=(trade_request.id,)))
    else:
        return render(request, 'tradepaper/trade-request.html', 
                {
                    'request': trade_request,
                    'listing': trade_request.listing
                    })

@vet_user("You need to be logged in to make a trade request.")
def new_request(http_request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    user = http_request.user

    # don't allow duplicate requests
    old_request_set = Request.objects.filter(requester=user, listing=listing)
    if old_request_set.exists():
        old_request = old_request_set[0]
        return HttpResponseRedirect(reverse('papers:request', args=(old_request.id,)))

    # don't allow user to trade their own magazine

    if user == listing.user:
        messages.error(http_request, "You cannot trade for your own magazine.")
        raise Http404

    # create request, but don't save it until it's posted
    trade_request = Request(
            requester = user,
            requestee = listing.user,
            listing = listing
            )
    if http_request.method == 'POST':
        text = http_request.POST.get('message')
        form = RequestForm(http_request.POST, auto_id=False)
        cancelled = 'cancel_trade' in http_request.POST
        if form.is_valid() and text and not cancelled:
            trade_request.save()
            message = trade_request.messages.create(
                    text = text,
                    sent_by_requester = True
                    )
            message.save()
            return HttpResponseRedirect(reverse('papers:request', args=(trade_request.id,)))
        else:
            messages.error("Please enter a message and try again.")
            return request(http_request, trade_request=trade_request)
    else:
        return request(http_request, trade_request=trade_request)
