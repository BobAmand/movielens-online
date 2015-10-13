from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
#from xxxxxxxx
from .models import Profile   # from within Citizens.models
from .forms import UserForm, ProfileForm
# Create your views here.


def user_register(request):
    if request.methon == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = Profile(
                user=user,
                favorite_color='blue',
            )
            profile.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('rater_detail')
    else:
        form = UserForm()
    return render(request, 'citizens/register.html',
                  {'form': form})


def user_logout(request):
    logout(request)

    return redirect('rater_detail')


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExit:
        profile = Profile(user=request.user)

    if request.method == 'GET':
        profile_form = ProfileForm(instance=profile, data=request.POST)
        # attempting to log in
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your profile has been updated.')

    return render(request, 'citizens/edit_profile.html',
                  {'form': profile_form})


def profile_detail(request, profile_id=None, profile_username=None):
    if profile_id:
        profile = get_object_or_404(Profile, pk=profile_id)
    elif profile_username:
        profile = get_object_or_404(Profile, user__username=profile_username)
    else:
        raise Http404("You must specify a user")

    return render(request, 'citizen/citizen_detail.html',
        {'profile': profile})


    #
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None and user.is_active:
    #         login(request, user)
    #         return redirect('movie_detail')
    #     else:
    #         return render(request,
    #                       'citizens/login.html',
    #                       {'failed': True,
    #                        'username': username})
    #
    # return render(request,
    #               'citizens/login.html')
