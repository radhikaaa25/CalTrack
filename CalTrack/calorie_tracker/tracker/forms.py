from django import forms
from .models import FoodEntry, UserProfile

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['food_name', 'calories']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['daily_calorie_goal']
