from Restaurant import Restaurant
from Customer import Customer
from Review import Review
import sqlite3
from tabulate import tabulate

# Create database and tables
def create_tables():
    connection = sqlite3.connect('restaurant_reviews.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS restaurants (name TEXT, price INTEGER);")
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name TEXT, last_name TEXT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS reviews (restaurant_name TEXT, star_rating INTEGER, customer_first_name TEXT, customer_last_name TEXT);")
    connection.commit()
    connection.close()

# data creation
def create_sample_data():
    connection = sqlite3.connect('restaurant_reviews.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO restaurants VALUES ('Kamakis', 3);")  
    cursor.execute("INSERT INTO restaurants VALUES ('Bulleys', 4);")
    cursor.execute("INSERT INTO customers VALUES ('Jack', 'Sparrow');")
    cursor.execute("INSERT INTO customers VALUES ('Jane', 'Smith');")
    cursor.execute("INSERT INTO reviews VALUES ('Kamakis', 5, 'Jack', 'Sparrow');") 
    cursor.execute("INSERT INTO reviews VALUES ('Bulleys', 4, 'Jack', 'Sparrow');")
    cursor.execute("INSERT INTO reviews VALUES ('Kamakis', 3, 'Jane', 'Smith');")  
    connection.commit()
    connection.close()

# Main function to test the methods
def main():
    create_tables()
    create_sample_data()

    # Restaurant methods
    kamakis = Restaurant("Kamakis", 3) 
    print("Reviews for Kamakis:") 
    print(tabulate(kamakis.reviews(), headers=["Restaurant Name", "Star Rating", "Customer First Name", "Customer Last Name"]))
    print("\nCustomers who reviewed Kamakis:") 
    print(tabulate(kamakis.customers(), headers=["Customer First Name", "Customer Last Name"]))
    print("\nAll reviews for Kamakis:")  
    print(tabulate(kamakis.all_reviews(), headers=["Review"]))

    # Customer methods
    jack_sparrow = Customer("Jack", "Sparrow")
    print("\nReviews by Jack Sparrow:")
    print(tabulate(jack_sparrow.reviews(), headers=["Restaurant Name", "Star Rating", "Customer First Name", "Customer Last Name"]))
    print("\nRestaurants reviewed by Jack Sparrow:")
    print(tabulate(jack_sparrow.restaurants(), headers=["Restaurant Name"]))
    print("\nFull name of Jack Sparrow:")
    print("Favorite restaurant of Jack Sparrow:")
    print(jack_sparrow.full_name())
    print(jack_sparrow.favorite_restaurant())

    # adding and deleting reviews
    bulleys = Restaurant("Bulleys", 5)  
    jack_sparrow.add_review(bulleys, 7) 
    print("\nReviews by Jack Sparrow after adding a new review:") 
    print(tabulate(jack_sparrow.reviews(), headers=["Restaurant Name", "Star Rating", "Customer First Name", "Customer Last Name"]))
    jack_sparrow.delete_reviews(bulleys) 
    print("\nReviews by Jack Sparrow after deleting reviews for Bulleys:") 
    print(tabulate(jack_sparrow.reviews(), headers=["Restaurant Name", "Star Rating", "Customer First Name", "Customer Last Name"]))

   
if __name__ == "__main__":
    main()


