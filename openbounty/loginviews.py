from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model

from openbounty.models import Challenge, BountyUser
from openbounty.forms import ChallengeForm
from openbounty.views import get_base_context

def register(request):
    errors = []
    username = email = phone = first = last = password = reenterpassword = ''
    next = request.GET.get('next', '/')
    
    context = get_base_context(request)

    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')
        next = request.POST.get('next')

        failed = False

        if username == "":
            errors.append("Username required.")
            failed = True
        elif len(get_user_model().objects.filter(username=username)) != 0:
            errors.append("This username has been used.")
            failed = True
        if first == "":
            errors.append("First Name required.")
            failed = True
        if last == "":
            errors.append("Last Name required.")
            failed = True
        if email == "":
            errors.append("Email required.")
            failed = True
        elif len(get_user_model().objects.filter(email=email)) != 0 and not remake:
            errors.append("Email already used.")
            failed = True
        if password == "":
            errors.append("Password required.")
            failed = True
        elif password != reenterpassword:
            errors.append("Passwords don't match.")
            failed = True
            
        if not failed:
            print username
            user = get_user_model().objects.create_user(username=username, first_name=first, last_name=last, email=email, phone_number=phone, password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect(request.POST.get('next'))
                else:
                    errors = ["Your account is not active, please contact the site admin."]
            else:
                errors = ["Failed to register."]
            
    errors = "\n".join(errors)
    context.update({'logged_in': request.user.is_authenticated(), 'errors': errors, 'username': username, 'email': email, 'first': first, 'last': last, 'next': next})
    return render_to_response('openbounty/register.html', context, RequestContext(request))

def login(request):
    usernameEntered = username = password = ''
    errors = []
    next = request.GET.get('next', '/')
    
    context = get_base_context(request)
    
    if request.POST:
        usernameEntered = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')

        username = usernameEntered

        if len(get_user_model().objects.filter(username=username)) < 1 and len(get_user_model().objects.filter(email=username)) < 1:
            errors = "Your username and/or password are incorrect."
        else:
            user = authenticate(username=username, password=password)
            if user == None and len(get_user_model().objects.filter(email=username)) != 0:
                username = get_user_model().objects.get(email=username).username
                user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect(request.POST.get('next'))
                else:
                    errors = "Your account is not active, please contact the site admin."
            else:
                errors = "Your username and/or password are incorrect."

    context.update({'logged_in': request.user.is_authenticated(), 'errors':errors, 'username': usernameEntered, 'next': next})
    return render_to_response('openbounty/login.html', context, RequestContext(request))

def logout(request):
    auth_logout(request)
    #render(request, 'checkout/logout.html')
    return redirect(request.GET.get('next','/'))
