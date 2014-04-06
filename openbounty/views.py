import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openbounty.models import Challenge, BountyUser, Backing
from openbounty.forms import ChallengeForm
# Create your views here.

def get_base_context(request):
    links = [{"url":"index", "label":"Home"}, {"url":"view_challenges","label":"Challenges"},{"url":"create_challenge","label":"Create a New Challenge"},]
    logged_in = request.user.is_authenticated()
    username = ''
    # Add conditional navbar links
    if logged_in:
        username = request.user.username
        links.append({"url":"profile", "label":"Account"})
        links.append({"url":"logout", "label":"Log out"})
    else:
        links.append({"url":"register", "label":"Register"})
        links.append({"url":"login", "label":"Log in"})

    context = {'request':request, 'navlinks':links, 'logged_in':logged_in, 'username':username}
    return context

def index(request):
    context = get_base_context(request)
    return render(request, 'openbounty/index.html', context)

def create(request):
    form = ChallengeForm()
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            bounty = form.cleaned_data['bounty']
            title = form.cleaned_data['title']
            challenge = form.cleaned_data['challenge']
            expiration_date = form.cleaned_data['expiration_date']
            challenge_object = Challenge.objects.create(user=request.user,bounty=bounty,title=title,challenge=challenge,expiration_date=expiration_date)     
            return HttpResponseRedirect('')     
        elif not request.user.is_authenticated():
            return HttpResponse("You need to login");

    context = get_base_context(request)
    context['form'] = form
    return render(request, 'openbounty/create.html', context)

def view_challenges(request):
    context = get_base_context(request)
    challenges = Challenge.objects.all()
    challengelist = []
    for challenge in challenges:
        challenge.bounty = int(challenge.bounty)
        challengelist.append(challenge)

    context['challenges'] = challengelist
    return render(request, 'openbounty/all_challenges.html', context)

def back_challenge(request, challenge_id):
    if not user.is_authenticated:
        redirect("index")
    challenge = Challenge.objects.get(id = challenge_id)
    user = request.user
    backer = Backing(user=user, challenge=challenge)
    backer.save()

def challenge(request, challenge_id):
    context = get_base_context(request)
    context['challenge'] = Challenge.objects.get(id = challenge_id)
    return render(request, 'openbounty/challenge.html', context)
    
