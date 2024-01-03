class Food:
    def __init__(self, name: str, calories_per_100: float, amount_in_g: float = 0, food_id: int = 0):
        self._id = food_id
        self._name = name
        self._calories_per_100 = calories_per_100
        self._amount = amount_in_g

    def __str__(self):
        return f"Food(id={self._id}, name={self._name}, calories_per_100={self._calories_per_100}, amount={self._amount})"

    def calculate_calories(self):
        sum_of_calories = (self._amount / 100) * self._calories_per_100
        return sum_of_calories

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_calories_per_100g(self):
        return self._calories_per_100

    def set_calories_per_100g(self, calories_per_100):
        self._calories_per_100 = calories_per_100

    def get_amount(self):
        return self._amount

    def set_amount(self, amount_in_g):
        self._amount = amount_in_g

    def get_id(self):
        return self._id

    def set_id(self, food_id: int):
        self._id = food_id
