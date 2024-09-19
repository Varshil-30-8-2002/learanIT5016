"""
Program to data catogrization
Author : Varshilkumar
"""

print() # empty line
def collect_user_information(id_counter):
    # Prompt user for input
    print("Enter User Information:")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email Address: ").strip()

    uniqe_id =id_counter + 1
    id_counter = uniqe_id

    print(f"\nUser Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email Address: {email}")
    print(f"Unique ID: {uniqe_id}")

    return id_counter,uniqe_id,name,age,email

def main():
    """
    Main function to initialize counter and collect user information.
    """
    id_counter = 5000
    id_counter, uniqe_id, name, age, email = collect_user_information(id_counter)

main()