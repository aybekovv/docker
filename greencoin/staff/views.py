from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from guide.models import Profile
from django.contrib.auth.decorators import user_passes_test
from .forms import ProfileUpdateForm, TrashAddForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Trash


User = get_user_model()

# Create your views here.


def staff_view(request):
    return render(request, 'staff/staff-page.html', locals())


@user_passes_test(lambda u: u.is_superuser)
def coins_view(request, name):
    query = request.GET.get('q', '')
    if query:
        try:
            user = User.objects.get(username=query)
            profile = Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            return redirect('staff-page-url')

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user.profile)
        t_form = TrashAddForm(request.POST)
        if p_form.is_valid() and t_form.is_valid():
            trash_type = t_form.cleaned_data.get('trash_type')
            trash_weight = t_form.cleaned_data.get('weight')
            trash = Trash.objects.create(
                user=user,
                trash_type=trash_type,
                weight=trash_weight)
            # t_form.save()
            coins_from_form = p_form.cleaned_data.get('coins')
            p_form.save()
            profile.profile_level_up(coins_from_form)
            profile.save()
    else:
        t_form = TrashAddForm()
        p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        't_form': t_form,
        'p_form': p_form,
        'profile': profile,
    }

    return render(request, 'staff/profile-coins.html', context)


def trash_statistics(request):
    maculature = Trash.objects.filter(trash_type='mc')
    glass = Trash.objects.filter(trash_type='gl')
    iron = Trash.objects.filter(trash_type='ir')
    plastic = Trash.objects.filter(trash_type='pl')

    mac_weight = maculature.values()
    mac_weight_sum = 0
    for i in mac_weight:
        mac_weight_sum += i['weight']
    print(mac_weight_sum)

    glass_weight = glass.values()
    glass_weight_sum = 0
    for i in glass_weight:
        glass_weight_sum += i['weight']

    iron_weight = iron.values()
    iron_weight_sum = 0
    for i in iron_weight:
        iron_weight_sum += i['weight']

    plastic_weight = iron.values()
    plastic_weight_sum = 0
    for i in plastic_weight:
        plastic_weight_sum += i['weight']

    context = {
        'mac_weight': mac_weight_sum,
        'iron_weight': iron_weight_sum,
        'glass_weight': glass_weight_sum,
        'plastic_weight': plastic_weight_sum,
        'maculature': maculature,
        'glass': glass,
        'iron': iron,
        'plastic': plastic
    }

    return render(request, 'staff/statistics.html', context)
