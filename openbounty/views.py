import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from openbounty.models import Challenge, BountyUser, Backing
from openbounty.forms import ChallengeForm
# Create your views here.

def get_base_context(request):
    links = [{"url":"index", "label":"Home"}, {"url":"view_bounties","label":"Bounties"},]
    logged_in = request.user.is_authenticated()
    username = ''
    # Add conditional navbar links
    if logged_in:
        username = request.user.username
        links.append({"url":"create_bounty","label":"Create a New Bounty"})
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

DATE_FORMAT = '%A, %B %d'
def dateToString(date):
    return datetime.datetime.strftime(date, DATE_FORMAT)

def create(request):
    form = ChallengeForm()
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            bounty = 1
            title = form.cleaned_data['title']
            challenge = form.cleaned_data['challenge']
            expiration_date = json.loads(request.session['expiration'])
            challenge_object = Challenge.objects.create(user=request.user,bounty=bounty,title=title,challenge=challenge,expiration_date=expiration_date)
            return HttpResponseRedirect('')     
    context = get_base_context(request)
    exp_date = datetime.datetime.now() + datetime.timedelta(60)    
    json_exp_date = json.dumps(exp_date, cls=DjangoJSONEncoder)
    request.session['expiration'] = json_exp_date
    context['expiration'] = dateToString(exp_date)
    context['form'] = form
    return render(request, 'openbounty/create.html', context)

def view_challenges(request):
    if request.method == 'POST':
        back_challenge(request, request.POST['challenge_id'], request.POST['action'])
    context = get_base_context(request)
    challenges = Challenge.objects.all()
    challengelist = []
    for challenge in sorted(challenges, key=lambda c: c.bounty, reverse=True):
        challenge_and_backers = {}
        challenge_and_backers['challenge'] = challenge
        try:
            all_backers = Backing.objects.filter(challenge=challenge)
            challenge_and_backers['backers'] = len(all_backers)
            if Backing.objects.filter(user=request.user, challenge=challenge):
                 challenge_and_backers['backed'] = True
        except Backing.DoesNotExist:
            challenge_and_backers['backers']  = None
            challenge_and_backers['backed'] = False
        
        challenge.bounty = int(challenge.bounty)
        challengelist.append(challenge_and_backers)
        
    context['challenges'] = challengelist
    return render(request, 'openbounty/list_challenges.html', context)

def back_challenge(request, challenge_id, action):
    if not request.user.is_authenticated:
        redirect("index")
    challenge = Challenge.objects.get(id = challenge_id)
    user = request.user   
    if action == 'back':     
        backer = Backing(user=user, challenge=challenge)
        backer.save()
    else:
        backer = Backing.objects.filter(user=user, challenge=challenge)[0]
        backer.delete()

def challenge(request, challenge_id):
    context = get_base_context(request)
    context['challenge'] = Challenge.objects.get(id = challenge_id)
    return render(request, 'openbounty/challenge.html', context)
    
