from django.shortcuts import render
from django.http import HttpResponse
from openbounty.models import Challenge, BountyUser
from openbounty.forms import ChallengeForm
# Create your views here.

def index(request):
    context = {}
    return render(request, 'openbounty/index.html', context)

def create(request):
    user = BountyUser.objects.get(identifier="dummy",phone_number="555")
    #if not user:
    #user = BountyUser.objects.create_user("dummy","555");
    form = ChallengeForm()
    if request.method == 'POST':
	form = ChallengeForm(request.POST)
	if form.is_valid():
	    bounty = form.cleaned_data['bounty']
	    title = form.cleaned_data['title']
	    challenge = form.cleaned_data['challenge']
	    expiration_date = form.cleaned_data['expiration_date']
	    challenge_object = Challenge.objects.create(user=user,bounty=bounty,title=title,challenge=challenge,expiration_date=expiration_date)
	    challenge_object.save()

    context = {}
    context['challenges'] = Challenge.objects.all()
    #print Challenge.objects.all()
    context['form'] = form
    return render(request, 'openbounty/create.html', context)
