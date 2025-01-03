import json

# Initialize travel data structure
travel_data = {
    "visited": [],
    "wishlist": []
}

# Sample data for testing
sample_data = [
    {"country": "France", "date": "2023-05-10"},
    {"country": "Japan", "date": "2022-12-15"},
    {"country": "Australia", "date": ""}
]
travel_data["visited"].extend(sample_data)

print("Travel Tracker Initialized!")


# Function to display the main menu
def display_menu():
    print("\nWelcome to the Travel Tracker Application\n")
    print("This app allows you to keep track of all of the countries you've already visited,")
    print("as well as all of the countries you'd like to add to your Wishlist!")
    print("\nPlease enter an option (1-6) from the menu below:")
    print("\n--- Travel Tracker Menu ---\n")
    print("1. Add a country")
    print("2. Delete a country")
    print("3. Search for a country")
    print("4. Sort and display records")
    print("5. Display all records")
    print("6. Exit")

display_menu()

# Function to confirm an action
def prompt_confirmation(action):
    confirmation = input(f"Are you sure you want to {action}? (yes/no): ").strip().lower()
    return confirmation == 'yes'

# Add a country to a specific category
travel_data = {
    "visited": [],
    "wishlist": []
}

import re
from datetime import datetime

def add_country(travel_data):
    category = input("Enter the category (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("Invalid category. Use 'visited' or 'wishlist'.")
        return
    
    country = input("Enter the country name: ").strip()
    
    # Validate date format, non-empty input, and future date
    while True:
        date = input("Enter the travel date (dd-mm-yyyy): ").strip()
        
        # Check if the date field is empty
        if not date:
            print("Date cannot be empty. Please enter a valid date.")
            continue
        
        # Regular expression to match date in dd-mm-yyyy format
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
            print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
            continue
        
        # Convert input date to a datetime object for comparison
        try:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
            continue
        
        # Check if the entered date is in the future
        if date_obj > datetime.now():
            print("The date cannot be in the future. Please enter a valid date.")
            continue
        
        break  # Exit loop when valid date is entered
    
    travel_data[category].append({"country": country, "date": date})
    print(f"Added {country} to {category.capitalize()} list.")

# Example of calling the function
add_country(travel_data)

# Delete a country from a specific category
def delete_country(travel_data):
    category = input("Enter the category (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("Invalid category. Use 'visited' or 'wishlist'.")
        return
    country = input("Enter the country name to delete: ").strip()
    for record in travel_data[category]:
        if record["country"].lower() == country.lower():
            if prompt_confirmation(f"delete {country} from {category}"):
                travel_data[category].remove(record)
                print(f"Deleted {country} from {category.capitalize()} list.")
            return
    print(f"{country} not found in {category.capitalize()} list.")

# Search for a country in both categories
def search_country(travel_data):
    country = input("Enter the country name to search: ").strip()
    found = False
    for category, records in travel_data.items():
        for record in records:
            if country.lower() in record["country"].lower():
                print(f"Found in {category.capitalize()} list: {record['country']} (Date: {record['date']})")
                found = True
    if not found:
        print(f"{country} not found in any list.")

# Sort and display records
def sort_records(travel_data):
    category = input("Enter the category to sort (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("Invalid category. Use 'visited' or 'wishlist'.")
        return
    travel_data[category].sort(key=lambda x: x["country"].lower())
    print(f"Sorted {category.capitalize()} list alphabetically.")

# Display all records
def display_records(travel_data):
    print("\\n--- Travel Records ---")
    for category, records in travel_data.items():
        print(f"\\n{category.capitalize()} list:")
        for record in records:
            print(f"- {record['country']} (Date: {record['date']})")

# Main application logic
def travel_tracker_app():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_country(travel_data)
        elif choice == "2":
            delete_country(travel_data)
        elif choice == "3":
            search_country(travel_data)
        elif choice == "4":
            sort_records(travel_data)
        elif choice == "5":
            display_records(travel_data)
        elif choice == "6":
            if prompt_confirmation("exit the application"):
                print("Exiting Travel Tracker. Goodbye!")
                break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the app
travel_tracker_app()