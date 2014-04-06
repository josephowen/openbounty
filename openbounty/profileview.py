from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openbounty.models import Challenge, BountyUser, Backing
from openbounty.forms import MoneyForm
from openbounty.views import get_base_context

def profile(request):
    if request.user.is_authenticated():        
        if request.method == 'POST':
            form = MoneyForm(request.POST)
            if form.is_valid():
                request.user.wallet += form.cleaned_data['money']
                request.user.save()
        context = get_base_context(request)
        context['form'] = MoneyForm()
        context['wallet'] = request.user.wallet
        context['name'] = request.user.username        
        context['email'] = request.user.email
        context['phone'] = request.user.phone_number
        try:        
            context['started_challenges'] = Challenge.objects.filter(user=request.user)
        except Challenge.DoesNotExist:
            context['backed_challenges']  = None        
        try:
            context['backed_challenges'] = Backing.objects.filter(user=request.user)
        except Backing.DoesNotExist:
            context['backed_challenges']  = None
        
        return render(request, 'openbounty/profile.html', context)    
    else:
        return HttpResponse("You need to login");
