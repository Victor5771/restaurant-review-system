import sqlite3

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews WHERE customer_first_name = ? AND customer_last_name = ?;", (self.first_name, self.last_name))
        results = cursor.fetchall()
        connection.close()
        return results

    def restaurants(self):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT restaurant_name FROM reviews WHERE customer_first_name = ? AND customer_last_name = ?;", (self.first_name, self.last_name))
        results = cursor.fetchall()
        connection.close()
        return results

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT restaurant_name FROM reviews WHERE customer_first_name = ? AND customer_last_name = ? ORDER BY star_rating DESC LIMIT 1;", (self.first_name, self.last_name))
        result = cursor.fetchone()
        connection.close()
        if result:
            return result[0]
        else:
            return None

    def add_review(self, restaurant, rating):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO reviews (restaurant_name, star_rating, customer_first_name, customer_last_name) VALUES (?, ?, ?, ?);", (restaurant.name, rating, self.first_name, self.last_name))
        connection.commit()
        connection.close()

    def delete_reviews(self, restaurant):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM reviews WHERE restaurant_name = ? AND customer_first_name = ? AND customer_last_name = ?;", (restaurant.name, self.first_name, self.last_name))
        connection.commit()
        connection.close()
