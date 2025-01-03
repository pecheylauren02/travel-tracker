import json
import re
from datetime import datetime

# List of valid countries
valid_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", 
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", 
    "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", 
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", 
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", 
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", 
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", 
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kuwait", "Kyrgyzstan", 
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", 
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", 
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", 
    "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", 
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", 
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", 
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

# Initialize travel data structure
travel_data = {
    "visited": [],
    "wishlist": []
}

print("Welcome to the Travel Tracker Application!")
print("This app allows you to keep track of the countries you've visited and those you want to visit.")

# Function to display the main menu
def display_menu():
    print("\n--- Travel Tracker Menu ---")
    print("1. Add a country")
    print("2. Delete a country")
    print("3. Search for a country")
    print("4. Sort and display records")
    print("5. Display all records")
    print("6. Exit")

# Function to confirm an action
def prompt_confirmation(action):
    confirmation = input(f"Are you sure you want to {action}? (yes/no): ").strip().lower()
    return confirmation == 'yes'

# Add a country to a specific category
def add_country():
    print("\nYou are about to add a country to one of your lists. How exciting!")
    
    while True:
        print("\nPlease enter the category you would like to enter below:")
        category = input("Type either 'visited' or 'wishlist' to continue: ").strip().lower()
        
        if category not in travel_data:
            print("Invalid category. Please use 'visited' or 'wishlist'.")
        else:
            break  # Exit loop when a valid category is entered
    
    # Loop until a valid country is entered
    while True:
        print("\nWell done! Now enter the country you'd like to add to your chosen list!")
        print("\nEnsure you spell the country correctly and with a capital letter.")
        country = input("Country name: ").strip()
        
        # Check if the country is in the valid countries list
        if country not in valid_countries:
            print("Oops! You have either entered an invalid country or have spelled it incorrectly!")
            print("Please enter a valid country from the list. E.g. Germany, not German or germany.")
        else:
            break  # Exit the loop if the country is valid
    
    # Validate date format, non-empty input, and future date
    while True:
        print("\nGreat job! Now enter the date you travelled there!")
        date = input("Enter the travel date (dd-mm-yyyy): ").strip()
        
        # Check if the date field is empty
        if not date:
            print("You have not entered anything yet. Please enter the date as dd-mm-yyyy.")
            continue
        
        # Regular expression to match date in dd-mm-yyyy format
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
            print("Uh Oh! The date you entered is wrong! Please enter the date in dd-mm-yyyy format.")
            print("For example: 12-12-2020")
            continue
        
        # Convert input date to a datetime object for comparison
        try:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Uh Oh! The date you entered is wrong! Please enter the date in dd-mm-yyyy format.")
            print("For example: 12-12-2020")
            continue
        
        # Check if the entered date is in the future
        if date_obj > datetime.now():
            print("As much as we love time travel, the date cannot be in the future. Please enter a date from the past!")
            continue
        
        break  # Exit loop when valid date is entered
    
    # Add the country to the chosen category
    travel_data[category].append({"country": country, "date": date})
    print(f"Well done! You have added {country} to your {category.capitalize()} list.")

    # After successfully adding a country, ask if the user wants to add another
    while True:
        add_another = input("\nWould you like to add another country? (yes/no): ").strip().lower()
        
        if add_another == 'yes':
            # If yes, call add_country again to continue the process without category selection
            add_country()  # Recursively call the add_country function
            return
        elif add_another == 'no':
            # If no, ask if the user wants to go back to the main menu
            go_to_menu = input("\nWould you like to go back to the main menu? (yes/no): ").strip().lower()
            
            if go_to_menu == 'yes':
                display_menu()  # Go back to the main menu
                return
            elif go_to_menu == 'no':
                # If no, exit the application
                exit_confirmation = input("\nWould you like to exit the application? (yes/no): ").strip().lower()
                
                if exit_confirmation == 'yes':
                    print("Thank you for using our application! Come back soon and add more to your exciting list!")
                    exit()  # Exit the program
                else:
                    # If no, return to the menu
                    display_menu()  # Go back to the main menu
                    return
        else:
            print("Oops, that was an invalid input. Please answer 'yes' or 'no'.")

# Delete a country from a specific category
def delete_country():
    print("\nWARNING: You are about to delete a country from one of your lists.")
    category = input("Enter the category you wish to delete it from (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("Oops, that was an invalid category. Enter either 'visited' or 'wishlist'.")
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
def search_country():
    country = input("Enter the country name you wish to search for: ").strip()
    found = False
    for category, records in travel_data.items():
        for record in records:
            if country.lower() in record["country"].lower():
                print(f"Yay! We found it in your {category.capitalize()} list: {record['country']} (Date: {record['date']})")
                found = True
    if not found:
        print(f"It appears that {country} is not in any of your lists.")
        response = input(f"Would you like to add {country} to one of your lists? (yes/no): ").strip().lower()
        if response == 'yes':
            add_country()
        else:
            response = input("Would you like to return to the main menu? (yes/no): ").strip().lower()
            if response == 'yes':
                display_menu()
            else:
                response = input("Would you like to exit the application? (yes/no): ").strip().lower()
                if response == 'yes':
                    print("Exiting the Travel Tracker Application.")
                    exit()
                else:
                    display_menu()

# Sort and display records
def sort_records():
    print("\nYou chose to sort records.")
    category = input("Enter the category to sort (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("Invalid category. Use 'visited' or 'wishlist'.")
        return
    travel_data[category].sort(key=lambda x: x["country"].lower())
    print(f"Sorted {category.capitalize()} list alphabetically.")

# Display all records
def display_records():
    print("\n--- Travel Records ---")
    for category, records in travel_data.items():
        print(f"\n{category.capitalize()} list:")
        for record in records:
            print(f"- {record['country']} (Date: {record['date']})")

# Main application logic
def travel_tracker_app():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_country()
        elif choice == "2":
            delete_country()
        elif choice == "3":
            search_country()
        elif choice == "4":
            sort_records()
        elif choice == "5":
            display_records()
        elif choice == "6":
            print("Exiting the Travel Tracker Application.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the application
travel_tracker_app()
