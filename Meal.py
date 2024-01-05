from Food import Food


class Meal():
    def __init__(self):
        self._ingredients: [Food] = []

    def add_ingredient(self, ingredient: Food):
        self._ingredients.append(ingredient)

    def remove_ingredient(self, ingredient: Food):
        try:
            self._ingredients.remove(ingredient)
        except:
            print("No such ingredient")
            return

    def get_calories(self):
        calories = 0
        for ingredient in self._ingredients:
            calories += ingredient.calculate_calories()
        return calories