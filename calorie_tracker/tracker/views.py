from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FoodEntry, UserProfile, FoodDatabase
from .forms import FoodEntryForm, UserProfileForm
import json

@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    food_entries = FoodEntry.objects.filter(user=request.user).order_by('-date')

    total_calories = sum(entry.total_calories() for entry in food_entries)
    total_carbs = sum(entry.total_carbs() for entry in food_entries)
    total_fats = sum(entry.total_fats() for entry in food_entries)
    total_proteins = sum(entry.total_proteins() for entry in food_entries)

    macros = {
        "Carbs": total_carbs,
        "Fats": total_fats,
        "Proteins": total_proteins
    }

    context = {
        'food_entries': food_entries,
        'calorie_goal': user_profile.daily_calorie_goal,
        'total_calories': total_calories,
        'macros': json.dumps(macros),
    }
    return render(request, 'tracker/dashboard.html', context)

def add_food(request):
    if request.method == "POST":
        form = FoodEntryForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect("add_food")
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.save()
            return redirect("add_food")
    else:
        form = FoodEntryForm()

    foods = FoodDatabase.objects.all()

    print("DEBUG: Foods retrieved from DB ->", foods)  # Debugging output in console

    return render(request, "tracker/add_food.html", {"form": form, "foods": foods})

def set_goal(request):
    return render(request, 'tracker/set_goal.html')