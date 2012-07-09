from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    servings = models.IntegerField()
    directions = models.TextField()
    published_on = models.DateField()
    public = models.BooleanField()

    user = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField()
    unit = models.CharField(max_length=200)