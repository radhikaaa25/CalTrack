from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FoodEntry, UserProfile
from .forms import FoodEntryForm, UserProfileForm
import json

@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    food_entries = FoodEntry.objects.filter(user=request.user).order_by('-date')

    # Preparing data for the graph
    daily_calories = {}
    for entry in food_entries:
        daily_calories[entry.date] = daily_calories.get(entry.date, 0) + entry.calories

    dates = list(daily_calories.keys())
    calories = list(daily_calories.values())

    context = {
        'food_entries': food_entries,
        'calorie_goal': user_profile.daily_calorie_goal,
        'dates': json.dumps(dates, default=str),
        'calories': json.dumps(calories),
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.save()
            return redirect('dashboard')
    else:
        form = FoodEntryForm()
    return render(request, 'tracker/add_food.html', {'form': form})

@login_required
def set_goal(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'tracker/set_goal.html', {'form': form})
