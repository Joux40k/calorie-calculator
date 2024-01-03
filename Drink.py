class Beverage:
    def __init__(self, name: str, calories_per_100ml: float, volume_in_ml: float):
        self._name = name
        self._calories_per_100ml = calories_per_100ml
        self._volume = volume_in_ml

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_calories_per_100ml(self):
        return self._calories_per_100ml

    def set_calories_per_100ml(self, calories_per_100ml):
        self._calories_per_100ml = calories_per_100ml

    def get_volume(self):
        return self._volume

    def set_volume(self, volume_in_ml):
        self._volume = volume_in_ml

    def calculate_total_calories(self):
        total_calories = (self._volume / 100) * self._calories_per_100ml
        return total_calories