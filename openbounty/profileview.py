from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openbounty.models import Challenge, BountyUser, Backing

def profile(request):
    if request.user.is_authenticated():
        context = {}
        context['wallet'] = request.user.wallet
        context['name'] = request.user.username        
        context['email'] = request.user.email
        context['phone'] = request.user.phone_number
        context['started_challenges'] = Challenge.objects.filter(user=request.user)
        try:
            context['backed_challenges'] = Backing.objects.get(user=request.user)
        except Backing.DoesNotExist:
            context['backed_challenges']  = None
        
        return render(request, 'openbounty/profile.html', context)    
    else:
        return HttpResponse("You need to login");
