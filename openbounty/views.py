from django.shortcuts import render
from django.http import HttpResponse
from openbounty.models import Challenge, BountyUser
from openbounty.forms import ChallengeForm
from django.core.exceptions import ObjectDoesNotExist 
# Create your views here.

def index(request):
    context = {}
    return render(request, 'openbounty/index.html', context)

def create(request):
    form = ChallengeForm()
    if request.method == 'POST':
	form = ChallengeForm(request.POST)
	if form.is_valid() and request.user.id:
	    bounty = form.cleaned_data['bounty']
	    title = form.cleaned_data['title']
	    challenge = form.cleaned_data['challenge']
	    expiration_date = form.cleaned_data['expiration_date']
	    challenge_object = Challenge.objects.create(user=request.user,bounty=bounty,title=title,challenge=challenge,expiration_date=expiration_date)
	    challenge_object.save()
	elif not request.user.id:
	    return HttpResponse("You need to login");

    context = {}
    context['challenges'] = Challenge.objects.all()
    context['form'] = form
    return render(request, 'openbounty/create.html', context)
