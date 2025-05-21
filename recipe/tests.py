from django.test import TestCase
from .models import Recipe, Category

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")

class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        category = Category.objects.create(name="Main Course")
        recipe = Recipe.objects.create(
            title="Borscht",
            description="Traditional soup",
            instructions="Boil and mix",
            ingredients="Beetroot, cabbage, meat",
            category=category
        )
        self.assertEqual(str(recipe), "Borscht")
        self.assertEqual(recipe.category.name, "Main Course")
