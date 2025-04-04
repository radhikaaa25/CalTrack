from django import forms
from .models import FoodEntry, UserProfile, Food

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['food', 'quantity']
    food = forms.ModelChoiceField(queryset=Food.objects.all(), empty_label="Select a food")
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['daily_calorie_goal']
