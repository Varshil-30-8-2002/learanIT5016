"""
Program : Movie Rental System
Author : Varshilkumar
"""

class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True

    def mark_as_rented(self):
        self.available = False

    def __str__(self):
        return f"{self.title} {self.year} - {self.genre} - {"Available" if self.available else "Rented"}

        


class Customer:
    def __init__(self, name):
        self.name = name
        self.return_movie = []

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()
            self.return_movie.append(movie)
            print(f"{self.name} rented {movie.title}")
        else:
            print(f"{self.name} cannot rent {movie.title} - It is already available")
        
    def return_movie(self, movie):
        if movie in self.return_movie:
            self.return_movie.remove(movie)
            movie.available = True
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} cannot return {movie.title} - They have not rented it")

    def list_rented_movie(self):
        if self.return_movie:
            print(f"{self.name}'s Rented Movied:")
            for movie in self.return_movie:
                print(movie)
        else:
            print(f"{self.name} has not rented movie")

    class RentalStore:
        def __init__(self):
            self.movie = []
            
    def add_movie(self, movie):
        self.movie.append(movie)
        # print(f"{movie.title} added to the store")
    def list_movies(self):
        if self.movie:
            print("List of Movies:")
            for movie in self.movie:
                print(movie)
        else:
            print("No movies available")

    def find_movie(self,title):
        for movie in self.movie:
            if movie.title == title.lower():
                return movie
        return None

def menu():
    print("\nMovie Rental System Menu")
    print("1. List available Movies")
    print("2. Rent a Movie")
    print("3. Return a Movie")
    print("4. List rented Movies")
    print("5. Add a Movie to Store")
    print("6. Exit")

    def main():
    #Initialize the store and Movies
    store = rentalStore()
    store.add_movie(Movie("Inception", "Sci-Fi", 2010))
    store.add_movie(Movie("The Matrix", "Action", 1999))
    store.add_movie(Movie("The Godfather", "Crime", 1972))

    # Initialize Customer 
    customer = {
        "Alice" : Customer("Alice"),
        "Bob" : Customer("Bob")
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            store.list_movies()
        elif choice == "2":
            customer_name = input("Enter the name of the customer: ").strip()
            movie_title = input("Enter the title of the movie: ").strip()
            customer = customer.get(customer_name)
            movie = store.find_movie(movie_title)
            if movie customer and movie:
                    customer.rent_movie(movie)
            else not customer
                    print("Customer not found")
        elif not movie:
            print("Movie not found")
            
           





