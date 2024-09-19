"""
Question :- For Tourist  Information System, we need to create a class called TouristInfoSystem.
Author :- Varshil Patel
"""
class Tourist:
    id_counter = 1  # Initialize a class variable to generate unique IDs

    def __init__(self, name, age, gender, birthdate):
        self.id = str(Tourist.id_counter).zfill(8)  # Generate a unique 8-character ID
        Tourist.id_counter += 1  # Increment the ID counter
        self.name = name
        self.age = age
        self.gender = gender
        self.birthdate = birthdate
        self.cost = 0
        self.places = []
        self.status = "Not Approved"

    def __str__(self):
        return f"Tourist ID: {self.id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nBirthdate: {self.birthdate}\nCost: ${self.cost:.2f}\nPlaces: {', '.join(self.places)}\nStatus: {self.status}"

class TouristSystem:
    def __init__(self):
        self.tourists = []

    def add_tourist(self, name, age, gender, birthdate):
        tourist = Tourist(name, age, gender, birthdate)
        self.tourists.append(tourist)
        return tourist

    def display_tourist(self, tourist_id):
        for tourist in self.tourists:
            if tourist.id == tourist_id:
                print(tourist)
                return
        print("Tourist not found.")

    def update_cost(self, tourist_id, cost):
        for tourist in self.tourists:
            if tourist.id == tourist_id:
                tourist.cost = cost
                return
        print("Tourist not found.")

    def add_place(self, tourist_id, place):
        for tourist in self.tourists:
            if tourist.id == tourist_id:
                tourist.places.append(place)
                return
        print("Tourist not found.")

    def update_status(self, tourist_id, status):
        for tourist in self.tourists:
            if tourist.id == tourist_id:
                tourist.status = status
                return
        print("Tourist not found.")

# Create a tourist system
system = TouristSystem()

while True:
    print("\nTourist System Menu:")
    print("1. Add Tourist")
    print("2. Display Tourist")
    print("3. Update Cost")
    print("4. Add Place")
    print("5. Update Status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender (M/F): ")
        birthdate = input("Enter birthdate (YYYY-MM-DD): ")
        tourist = system.add_tourist(name, age, gender, birthdate)
        print(f"Tourist ID: {tourist.id} created successfully.")

    elif choice == "2":
        tourist_id = input("Enter tourist ID: ")
        system.display_tourist(tourist_id)

    elif choice == "3":
        tourist_id = input("Enter tourist ID: ")
        cost = float(input("Enter cost: "))
        system.update_cost(tourist_id, cost)

    elif choice == "4":
        tourist_id = input("Enter tourist ID: ")
        place = input("Enter place: ")
        system.add_place(tourist_id, place)

    elif choice == "5":
        tourist_id = input("Enter tourist ID: ")
        status = input("Enter status (Approved/Rejected/Not Approved): ")
        system.update_status(tourist_id, status)

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")