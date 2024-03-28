import sqlite3

class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def fanciest(cls):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1;")
        result = cursor.fetchone()
        connection.close()
        if result:
            return cls(result[0], result[1])
        else:
            return None

    def reviews(self):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews WHERE restaurant_name = ?;", (self.name,))
        results = cursor.fetchall()
        connection.close()
        return results

    def customers(self):
        connection = sqlite3.connect('restaurant_reviews.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT customer_first_name, customer_last_name FROM reviews WHERE restaurant_name = ?;", (self.name,))
        results = cursor.fetchall()
        connection.close()
        return results

    def all_reviews(self):
        reviews = self.reviews()
        formatted_reviews = []
        for review in reviews:
            formatted_review = f"Review for {self.name} by {review[2]} {review[3]}: {review[1]} stars."
            formatted_reviews.append(formatted_review)
        return formatted_reviews
