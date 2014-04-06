import requests, math
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openbounty.models import Challenge, BountyUser, Backing
from openbounty.forms import MoneyForm
from openbounty.views import get_base_context


def profile(request):
    if request.user.is_authenticated():
        user = request.user    
        context = get_base_context(request)    
        context = venmo(request, context)
        context['committed'] = len(Backing.objects.filter(user=user))
        context['wallet'] = request.user.wallet
        context['name'] = request.user.username        
        context['email'] = request.user.email
        context['phone'] = request.user.phone_number
        try:        
            context['started_challenges'] = Challenge.objects.filter(user=user)
        except Challenge.DoesNotExist:
            context['backed_challenges']  = None        
        try:
            context['backed_challenges'] = Backing.objects.filter(user=user)
        except Backing.DoesNotExist:
            context['backed_challenges']  = None
        return render(request, 'openbounty/profile.html', context)    
    else:
        return HttpResponse("You need to login");

def venmo(request, context):
    user = request.user    
    if request.method == 'GET' and 'access_token' in request.GET.viewkeys():
        access_token = request.GET['access_token']
        user.access_token = access_token        
        user.save()
    r = requests.get('https://api.venmo.com/v1/me?access_token='+user.access_token)   
    if r.status_code == 200:
        r_json = r.json()
        user.venmo = r_json['data']['actor']['id']
        balance = r_json['data']['balance']
        context['venmo'] = balance
        context['form'] = MoneyForm()
        if request.method == 'POST':
            form = MoneyForm(request.POST)
            if form.is_valid():
                money = form.cleaned_data['money']
                if 'add' in request.POST.viewkeys():                    
                    if int(user.wallet + money < float(balance)):
                        user.wallet += money
                        user.save()
                else:
                    if (user.wallet - money) >= 0:
                        user.wallet -= money
                        user.save()            
        if user.wallet:        
            user.wallet = min(user.wallet, math.floor(float(balance)))
            user.save()
    else:
        context['venmo'] = None
    return context
