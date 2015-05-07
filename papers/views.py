from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django import forms

from papers.models import Listing, Trade, Message
from users.models import User
from users.views import vet_user

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'edition', 'condition', 'image']

class TradeForm(forms.Form):
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

def trade(request, id=None, trade=None):
    if trade is None:
        if id is None:
            raise Http404
        else:
            trade = get_object_or_404(Trade, id=id)
    user = request.user
    user_is_trader = (trade.trader.id == user.id)
    if user not in [trade.trader, trade.tradee]:
        raise Http404
    if request.method == 'POST':
        text = request.POST.get('message')
        form = TradeForm(request.POST, auto_id=False)
        cancelled = 'cancel_trade' in request.POST
        if form.is_valid() and text and not cancelled:
            message = trade.messages.create(
                    text = text,
                    sent_by_trader = user_is_trader
                    )
            message.save()
            return HttpResponseRedirect(reverse('papers:trade', args=(trade.id,)))
    else:
        for message in trade.messages.all():
            if message.sent_by_trader == (user == trade.tradee):
                message.read = True
        return render(request, 'tradepaper/trade-request.html', 
                {
                    'trade': trade,
                    'listing': trade.listing,
                    'user_is_trader': user_is_trader
                    })

@vet_user("You need to be logged in to make a trade request.")
def new_trade(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    user = request.user

    # don't allow duplicate trades
    old_trade_set = Trade.objects.filter(trader=user, listing=listing)
    if old_trade_set.exists():
        old_trade = old_trade_set[0]
        return HttpResponseRedirect(reverse('papers:trade', args=(old_trade.id,)))

    # don't allow user to trade their own magazine
    if user == listing.user:
        messages.error(request, "You cannot trade for your own magazine.")
        raise Http404

    # create request, but don't save it until it's posted
    trade = Trade(
            trader = user,
            tradee = listing.user,
            listing = listing
            )
    if request.method == 'POST':
        text = request.POST.get('message')
        form = TradeForm(request.POST, auto_id=False)
        cancelled = 'cancel_trade' in request.POST
        if form.is_valid() and text and not cancelled:
            trade.save()
            message = trade.messages.create(
                    text = text,
                    sent_by_trader = True
                    )
            message.save()
            return HttpResponseRedirect(reverse('papers:trade', args=(trade.id,)))
        else:
            messages.error("Please enter a message and try again.")
            return trade(request, trade=trade)
    else:
        return trade(request, trade=trade)
