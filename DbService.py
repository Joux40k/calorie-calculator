import sqlite3

from Food import Food


class DbService:
    def __init__(self):
        self.conn = sqlite3.connect('calorie_calculator.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS foods (id INTEGER PRIMARY KEY, name TEXT, calories_per_100 REAL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, food INTEGER, amount REAL)")
        self.conn.commit()

    def add_food(self, food, calories_per_100):
        self.cursor.execute("INSERT INTO foods (name, calories_per_100) VALUES (?,?)", (food, calories_per_100))
        self.conn.commit()
    def get_all_foods(self):
        self.cursor.execute("SELECT * FROM foods")
        foods = []
        for food in self.cursor.fetchall():
            foods.append(Food(food[1], food[2], food_id=food[0]))
        return foods

    def get_food_by_id(self, food_id: int):
        self.cursor.execute("SELECT name, calories_per_100 FROM foods WHERE id = ?", (food_id,))
        food_entry = self.cursor.fetchone()
        food: Food = Food(food_entry[0], food_entry[1], 100, food_id)
        return food

    def delete_food(self, food_id):
        self.cursor.execute("DELETE FROM foods WHERE id = ?", (food_id,))
        self.conn.commit()

    def historize_food(self, food: Food):
        self.cursor.execute("INSERT INTO history (food, amount) VALUES (?, ?)", (food.get_id(), food.get_amount()))
        self.conn.commit()

    def get_all_history(self):
        self.cursor.execute("SELECT food, amount, created_at FROM history")
        return self.cursor.fetchall()

db = DbService()
print(db.get_all_foods())
print(db.get_food_by_id(1))
print(db.get_all_history())