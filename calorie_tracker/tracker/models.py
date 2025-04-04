from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_calorie_goal = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.user.username} - Goal: {self.daily_calorie_goal} kcal"
class FoodDatabase(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()

    def __str__(self):
        return self.name
class Food(models.Model):  # Pre-loaded food data
    name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    carbs = models.FloatField(default=0)  # in grams
    fats = models.FloatField(default=0)  # in grams
    proteins = models.FloatField(default=0)  # in grams

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=1)  # Ensure ID 1 exists
    date = models.DateField(auto_now_add=True)
    quantity = models.FloatField(default=1)  # Multiplier for food portions

    def total_calories(self):
        return self.food.calories * self.quantity

    def total_carbs(self):
        return self.food.carbs * self.quantity

    def total_fats(self):
        return self.food.fats * self.quantity

    def total_proteins(self):
        return self.food.proteins * self.quantity

    def __str__(self):
        return f"{self.food.name} x {self.quantity} - {self.total_calories()} kcal"
