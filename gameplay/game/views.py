from django.shortcuts import render, redirect

from gameplay.game.models import Profile, Game

from gameplay.game.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm

# CarEditForm, \
#     CarDeleteForm, ProfileDeleteForm, CarCreateForm, ProfileEditForm


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile


def home_page(request):
    profile = get_profile()
    # if profile is None:
    #     return create_profile(request)

    context = {
        'profile': profile,
    }

    return render(
        request,
        'home-page.html',
        context,
    )


def create_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,

    }

    return render(
        request,
        'create-profile.html',
        context,
    )


def details_profile(request):
    # profile = Profile.objects.filter().get()
    profile = get_profile()
    games_all = Game.objects.all()
    games_count = Game.objects.all().count()

    try:
        average_games_rating = sum([g.rating for g in games_all]) / games_count
    except ZeroDivisionError:
        average_games_rating = 0.0

    context = {
        'profile': profile,
        'games_all': games_all,
        'games_count': games_count,
        'average_games_rating': average_games_rating,

    }

    return render(
        request,
        'details-profile.html',
        context,
    )


def edit_profile(request):
    # profile = Profile.objects.filter().get()
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'edit-profile.html',
        context,
    )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(
        request,
        'delete-profile.html',
        context,
    )


def game_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'create-game.html',
        context,
    )


def details_game(request, pk):
    game = Game.objects \
        .filter(pk=pk) \
        .get()

    profile = get_profile()

    context = {
        'game': game,
        'profile': profile,
    }

    return render(
        request,
        'details-game.html',
        context,
    )


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    profile = get_profile()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }

    return render(
        request,
        'edit-game.html',
        context,
    )


def delete_game(request, pk):
    game = Game.objects \
        .filter(pk=pk) \
        .get()

    profile = get_profile()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }

    return render(
        request,
        'delete-game.html',
        context,
    )


def dashboard(request):
    profile = Profile.objects.first()
    games_all = Game.objects.all()

    context = {
        'profile': profile,
        'games_all': games_all,
    }

    return render(
        request,
        'dashboard.html',
        context,
    )