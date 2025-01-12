import os
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

print("\nWelcome to the Travel Tracker Application!")
print("\nThis app allows you to keep track of the countries you've visited and those you want to visit.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the main menu with added formatting
def display_menu():
    menu_border = "=" * 40
    print(menu_border)
    print("\033[1;34m" + "--- Travel Tracker Menu ---" + "\033[0m")  # Blue text for the title
    print(menu_border)
    print("\033[1;32m" + "1. Add a country" + "\033[0m")  # Green text for options
    print("\033[1;33m" + "2. Delete a country" + "\033[0m")  # Yellow text for options
    print("\033[1;35m" + "3. Search for a country" + "\033[0m")  # Magenta text for options
    print("\033[1;36m" + "4. Sort records alphabetically" + "\033[0m")  # Cyan text for options
    print("\033[1;37m" + "5. Display all records" + "\033[0m")  # White text for options
    print("\033[1;31m" + "6. Exit" + "\033[0m")  # Red text for the exit option
    print(menu_border)

# Function to confirm an action
def prompt_confirmation(action):
    confirmation = input(f"Are you sure you want to {action}? (yes/no): ").strip().lower()
    return confirmation == 'yes'


def add_country():
    clear_terminal()
    print("\nYou are about to add a country to one of your lists. How exciting!")
    
    while True:
        print("\nPlease enter the category you would like to enter below:")
        category = input("\nType either 'visited' or 'wishlist' to continue: ").strip().lower()
        
        if category not in travel_data:
            print("\nInvalid category. Please use 'visited' or 'wishlist'.")
        else:
            break  # Exit loop when a valid category is entered
    
    # Loop until a valid country is entered
    while True:
        print("\nEnter the country you would like to add to your chosen list!")
        country = input("\nCountry name: ").strip()
        
        # Normalize case for validation
        country = country.title()
        
        # Check if the country is in the valid countries list
        if country not in valid_countries:
            print("\nOops! You have either entered an invalid country or have spelled it incorrectly!")
            print("\nPlease enter a valid country from the list. E.g. Germany, not German or germany.")
        else:
            print(f"\nWell done! You have added {country} to your {category.capitalize()} countries.")
            break  # Exit the loop if the country is valid
    
    # Validate date format, non-empty input, and future/past date based on category
    while True:
        date = input("\nEnter the travel date (dd-mm-yyyy): ").strip()
        
        # Check if the date field is empty
        if not date:
            print("\nYou have not entered anything yet. Please enter the date as dd-mm-yyyy.")
            continue
        
        # Regular expression to match date in dd-mm-yyyy format
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
            print("\nUh Oh! The date you entered is wrong! Please enter the date in dd-mm-yyyy format.")
            print("\nFor example: 12-12-2020")
            continue
        
        # Convert input date to a datetime object for comparison
        try:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("\nUh Oh! The date you entered is wrong! Please enter the date in dd-mm-yyyy format.")
            print("\nFor example: 12-12-2020")
            continue
        
        # Check if the entered date is valid for the category
        if category == "wishlist" and date_obj <= datetime.now():
            print("\nPlease note: You can only add countries to your wishlist with a future date!")
            continue
        elif category == "visited" and date_obj > datetime.now():
            print("\nYou cannot enter a future date for a visited country. Please enter a date in the past.")
            continue
        
        break  # Exit loop when valid date is entered
    
    # Add the country to the chosen category
    travel_data[category].append({"country": country, "date": date})

    print(f"\nSuccess! You have added {country} to your {category.capitalize()} list on {date}.")

    # Prompt to add another country
    while True:
        add_another = input("\nWould you like to add another country? (yes/no): ").strip().lower()
        
        if add_another == 'yes':
            add_country()  # Recursively call the add_country function
            return
        elif add_another == 'no':
            print("\nReturning to the main menu...")
            return
        else:
            print("\nInvalid input. Please answer 'yes' or 'no'.")


# Delete a country from a specific category
def delete_country():
    clear_terminal()
    print("\nWARNING: You are about to delete a country from one of your lists.")
    
    while True:
        category = input("\nEnter the category you wish to delete it from (visited/wishlist): ").strip().lower()
        
        if category not in travel_data:
            print("\nOops, that was an invalid category. Enter either 'visited' or 'wishlist'.")
        else:
            break  # Exit loop when valid category is entered
    
    country = input("\nEnter the country you wish to delete: ").strip()
    
    for record in travel_data[category]:
        if record["country"].lower() == country.lower():
            if prompt_confirmation(f"delete {country} from {category}"):
                travel_data[category].remove(record)
                print(f"\nSuccessfully deleted {country} from {category.capitalize()} list.")
                
                # After successfully deleting, ask the user if they want to delete another country
                while True:
                    delete_another = input("\nWould you like to delete another country? (yes/no): ").strip().lower()
                    
                    if delete_another == 'yes':
                        delete_country()  # Recursively call the delete_country function
                        return
                    elif delete_another == 'no':
                        # If no, ask if the user wants to go back to the main menu
                        go_to_menu = input("\nWould you like to go back to the main menu? (yes/no): ").strip().lower()
                        
                        if go_to_menu == 'yes':
                            display_menu()  # Go back to the main menu
                            return
                        elif go_to_menu == 'no':
                            # If no, exit the application
                            exit_confirmation = input("\nWould you like to exit the application? (yes/no): ").strip().lower()
                            
                            if exit_confirmation == 'yes':
                                print("\nThank you for using our application! Come back soon and add more to your exciting list!")
                                exit()  # Exit the program
                            else:
                                # If no, return to the menu
                                display_menu()  # Go back to the main menu
                                return
                    else:
                        print("\nInvalid input. Please answer 'yes' or 'no'.")
                return
    print(f"{country} not found in {category.capitalize()} list.")

# Search for a country in both categories
def search_country():
    clear_terminal()
    country = input("\nEnter the country name you wish to search for: ").strip()
    found = False
    for category, records in travel_data.items():
        for record in records:
            if country.lower() in record["country"].lower():
                print(f"\nYay! We found it in your {category.capitalize()} countries: {record['country']} (Date: {record['date']})")
                found = True
    if not found:
        print(f"\nIt appears that {country} is not in any of your lists.")
        response = input(f"\nWould you like to add {country} to one of your lists? (yes/no): ").strip().lower()
        if response == 'yes':
            add_country()
        else:
            response = input("\nWould you like to return to the main menu? (yes/no): ").strip().lower()
            if response == 'yes':
                display_menu()
            else:
                response = input("\nWould you like to exit the application? (yes/no): ").strip().lower()
                if response == 'yes':
                    print("Thank you for using our application! Come back soon and add more to your exciting list!")
                    exit()
                else:
                    display_menu()

# Sort and display records
def sort_records():
    clear_terminal()
    print("\nYou chose to sort records.")
    category = input("\nEnter the category to sort (visited/wishlist): ").strip().lower()
    if category not in travel_data:
        print("\nInvalid category. Use 'visited' or 'wishlist'.")
        return
    travel_data[category].sort(key=lambda x: x["country"].lower())
    print(f"Sorted {category.capitalize()} list alphabetically.")

# Display all records
def display_records():
    clear_terminal()
    print("\nHere are your travel records:")

    # Display visited records
    if travel_data["visited"]:
        print("\n\033[1;32mVisited Countries:\033[0m")
        for record in travel_data["visited"]:
            print(f"- {record['country']} (Visited on: {record['date']})")
    else:
        print("\n\033[1;32mVisited Countries:\033[0m No records yet!")

    # Display wishlist records
    if travel_data["wishlist"]:
        print("\n\033[1;33mWishlist Countries:\033[0m")
        for record in travel_data["wishlist"]:
            print(f"- {record['country']} (Planned for: {record['date']})")
    else:
        print("\n\033[1;33mWishlist Countries:\033[0m No records yet!")

    # Prompt for adding more countries
    while True:
        choice = input("\nWould you like to add more countries to your records? (yes/no): ").strip().lower()
        if choice == "yes":
            add_country()
            return
        elif choice == "no":
            print("\nReturning to the main menu...")
            break
        else:
            print("\nInvalid input. Please answer 'yes' or 'no'.")


# Main application logic
def travel_tracker_app():
    while True:
        display_menu()
        choice = input("\nChoose an option from the list above (1-6): ").strip()
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

if __name__ == "__main__":
    display_menu()  