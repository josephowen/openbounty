import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openbounty.models import Challenge, BountyUser, Comment
from openbounty.forms import ChallengeForm, CommentForm
# Create your views here.

def get_base_context(request):
    username = ''
    logged_in = request.user.is_authenticated()
    if logged_in:
        username = request.user.username
    links = [{"url":"index", "label":"Home"}, {"url":"login", "label":"Log in"}, {"url":"register", "label":"Register"}, {"url":"logout", "label":"Log out"}]
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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            title = form.cleaned_data['title']
            comment = form.cleaned_data['comment']
            challenge_id = request.POST['challenge_id']
            challenge = Challenge.objects.get(id = challenge_id)
            user = request.user
            date_posted = datetime.datetime.now()
            comment_object = Comment.objects.create(user=user,title=title,comment=comment,challenge=challenge,date_posted=date_posted)
            return HttpResponseRedirect('')

        elif not request.user.is_authenticated():
            return HttpResponse("You need to login");
    context = get_base_context(request)
    challenges = Challenge.objects.all()
    context['contents'] = []
    for challenge in challenges:
        data = {}        
        data['challenge'] = challenge       
        data['comments'] = len(Comment.objects.filter(challenge=challenge))
        context['contents'].append(data)
    context['form'] = form
    return render(request, 'openbounty/view.html', context)
