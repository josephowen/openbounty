from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from openbounty.models import Challenge, BountyUser
from openbounty.forms import ChallengeForm
from django.core.exceptions import ObjectDoesNotExist 
# Create your views here.

def listusers(request):
    context = {}
    users = BountyUser.objects.all()
    userList = []
    for u in users:
        name = u.first_name + " " + u.last_name
        print name
        userList.append({"name":name, "username":u.username, "email":u.email, "phone":u.phone_number})

    context.update({"users": userList})

    return render(request, 'openbounty/listusers.html', context)