import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.forms import ModelForm

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]

def index(request):
  return HttpResponse("This is the user index.")

def profile(request, username):
  user = get_object_or_404(User, username=username)
  return render(request, 'paperapp/profile.html', {'user':user})

def login(request):
    return render(request, 'paperapp/login.html')

def register(request):
    try:
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

    if request.method == 'POST':
        form = UserForm(request.POST, auto_id='signup_%s')
        if form.is_valid():
            u = User.objects.create(
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password'],
                joindate=datetime.datetime.now(),
            )
            u.save()
            HttpResponseRedirect(reverse('users:profile', args=(u.username,)))
    else:
        return render(request, 'paperapp/signup.html', {
            'form': form,
            'error_message': 'Please fill in all required fields'})
