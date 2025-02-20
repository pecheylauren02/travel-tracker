"""
This script manages travel data,
allowing users to add, search, sort, and view countries
they've visited or wish to visit.
It includes functionality for user input, validating
and storing country data, and providing
options to sort or display records.

Modules:
- os: for interacting with the operating system
- sys: for system-specific parameters and functions
- re: for regular expression matching and operations
- datetime: for working with date and time objects
"""

import os
import sys
import re
from datetime import datetime

valid_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Democratic Republic of the Congo", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
    "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kuwait",
    "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
    "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman",
    "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

# Initialise travel data structure
travel_data = {
    "visited": [],
    "wishlist": []
}

STORED_AGE = None


def clear_terminal():
    """
    Allows the user to add a country to their visited or wishlist category.
    Prompts for the country, category, age, and travel date with validations.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """
    Displays the main menu of the Travel Tracker
    application with formatted options.
    """
    menu_border = "=" * 50
    title = "Welcome to the Travel Tracker Application 🌍"
    options = [
        ("\033[1;32m1. Add a country\033[0m"),
        ("\033[1;33m2. Delete a country\033[0m"),
        ("\033[1;35m3. Search for a country\033[0m"),
        ("\033[1;36m4. Sort your countries\033[0m"),
        ("\033[1;37m5. Display all countries\033[0m"),
        ("\033[1;31m6. Exit\033[0m"),
    ]

    print("\033[1;34m" + menu_border + "\033[0m")
    print("\033[1;37m" + f"  {title}".ljust(48) + "\033[0m")
    print("\033[1;34m" + menu_border + "\033[0m\n")

    print("Choose an option:")
    for option in options:
        print(f"  {option}")

    print("\n\033[1;34m" + menu_border + "\033[0m")


def prompt_confirmation(action):
    """
    Prompts the user to confirm an action.

    Parameters:
        action (str): The action to confirm.

    Returns:
        bool: True if the user confirms the action, False otherwise.
    """
    confirmation = input(f"Are you sure you want to {action}? (yes/no): "
                         ).strip().lower()
    return confirmation == 'yes'


def validate_category():
    """
    Ensures the user enters a valid category ('visited' or 'wishlist').
    """
    while True:
        category = input("\nType either 'visited' or 'wishlist' to continue: "
                         ).strip().lower()
        if category not in travel_data:
            print("\nInvalid category. Please use 'visited' or 'wishlist'.")
        else:
            return category


def validate_age():
    """
    Validates the user's age input if needed.
    """
    while True:
        age_input = input("\nPlease enter your age: ").strip()
        if not age_input.isdigit() or not 1 <= int(age_input) <= 120:
            print("\nPlease enter a valid age between 1 and 120.")
        else:
            return int(age_input)


def validate_country():
    """
    Validates the country input against valid countries.
    """
    while True:
        country = input("\nCountry name: ").strip().title()
        if country not in valid_countries:
            print("\nOops! You have either entered an invalid country!")
            print("\nTry entering it again.")
        else:
            print(f"\nSuccessfully added {country}.")
            return country


def validate_date(min_date, category):
    """
    Validates the travel date entered by the user.
    """
    while True:
        date = input("\nEnter the travel date (dd-mm-yyyy): ").strip()

        if not date:
            print("\nYou have not entered anything yet.")
            print("\nPlease enter the date as dd-mm-yyyy")
            continue

        if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
            print("\nUh Oh! Please enter the date in dd-mm-yyyy format.")
            continue

        try:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("\nUh Oh! The date you entered is wrong!")
            continue

        if min_date and date_obj < min_date:
            print("\nYou cannot enter a date before your birthyear.")
            continue

        if category == "wishlist" and date_obj <= datetime.now():
            print("\nYou can only add countries with a future date!")
            continue

        if category == "visited" and date_obj > datetime.now():
            print("\nYou cannot enter a future date for a visited country.")
            continue

        return date_obj


def add_country():
    """
    Allows the user to add a country to
    their visited or wishlist category.
    Prompts for the country, category,
    age, and travel date with validations.
    """
    global STORED_AGE  # Remember the user's age across multiple calls
    clear_terminal()
    print("\nYou are about to add a country to one of your lists!")

    category = validate_category()

    if category == "visited" and STORED_AGE is None:
        STORED_AGE = validate_age()

    age = STORED_AGE if category == "visited" else None
    today = datetime.now()
    min_year = today.year - (age or 0)
    min_date = datetime(min_year, today.month, today.day) if age else None

    country = validate_country()

    date_obj = validate_date(min_date, category)

    travel_data[category].append({"country": country,
                                 "date": date_obj.strftime("%d-%m-%Y")})

    print(f"\nSuccess! You have added {country} to: ")
    print(f"\n{category.capitalize()} for {date_obj.strftime('%d-%m-%Y')}")

    while True:
        add_another = input("\nNeed to add another country? (yes/no): "
                            ).strip().lower()
        if add_another == 'yes':
            add_country()
            return
        if add_another == 'no':
            print("\nReturning to the main menu...")
            clear_terminal()
            return
        print("\nInvalid input. Please answer 'yes' or 'no'.")


def delete_country():
    """
    Allows the user to delete a country
    from their visited or wishlist category.
    Prompts for the category and country
    with confirmation before deletion.
    """
    clear_terminal()
    print("\nWARNING: You are about to delete a country!")

    # Get the category
    while True:
        category = input("\nEnter the category (visited/wishlist): "
                         ).strip().lower()
        if category not in travel_data:
            print("\nEnter either 'visited' or 'wishlist'.")
        else:
            break

    # Loop for country deletion
    while True:
        country = input("\nEnter the country you wish to delete: ").strip()
        # Check if the country exists in the category
        found = False
        for record in travel_data[category]:
            if record["country"].lower() == country.lower():
                found = True
                if prompt_confirmation(f"delete {country} from {category}"):
                    travel_data[category].remove(record)
                    print(f"\nSuccessfully deleted {country} from: ")
                    print(f"\n{category.capitalize()} list.")
                break

        if not found:
            print(f"\n{country} is not in your {category.capitalize()} list.")
            retry = input("\nWould you like to try again? (yes/no): "
                          ).strip().lower()
            if retry == "yes":
                continue
            else:
                return

        while True:
            delete_another = input("\nNeed to delete another? (yes/no): "
                                   ).strip().lower()
            if delete_another == "yes":
                break
            elif delete_another == "no":
                return
            else:
                print("\nPlease enter 'yes' or 'no'.")


def search_country():
    """
    Allows the user to search for a country
    in their travel records.
    If the country is not found,
    provides an option to add it
    or return to the menu.
    """
    clear_terminal()
    country = input("\nSearch for your country here: ").strip()
    found = False
    for category, records in travel_data.items():
        for record in records:
            if country.lower() in record["country"].lower():
                print(
                    f"\nWe found it in your {category.capitalize()} places: "
                )
                print(
                    f"\n{record['country']} (Date: {record['date']}"
                    )
                found = True
    if not found:
        print(f"\nIt appears that {country} is not in any of your lists.")
        response = input(
            f"\nWant to add {country} to one of your lists? (yes/no): "
                         ).strip().lower()
        if response == 'yes':
            add_country()
        else:
            response = input("\nReturn to the main menu? (yes/no): "
                             ).strip().lower()
            if response == 'yes':
                display_menu()
            else:
                print("\nThank you for using our application!")
                sys.exit()


def sort_records():
    """
    Sorts the records of a specified category
    (visited/wishlist) by different criteria.
    """
    clear_terminal()
    print("\nYou chose to sort records.")

    category = input("\nEnter the category to sort (visited/wishlist): "
                     ).strip().lower()
    while category not in travel_data:
        print("\nInvalid category. Use 'visited' or 'wishlist'.")
        category = input("\nEnter the category to sort (visited/wishlist): "
                         ).strip().lower()

    print("\n\033[1;34mChoose a sorting option:\033[0m")
    print("\033[1;32m1. Ascending order by country (A-Z)\033[0m")
    print("\033[1;33m2. Descending order by country name (Z-A)\033[0m")
    print("\033[1;36m3. Ascending order by date\033[0m")
    print("\033[1;35m4. Descending order by date\033[0m")

    sorting_choice = input("\nEnter the number corresponding to your choice: "
                           ).strip()
    clear_terminal()

    # Dictionary to map sorting choices to sorting functions
    sort_functions = {
        '1': (lambda x: x["country"].lower(), False, "A-Z"),
        '2': (lambda x: x["country"].lower(), True, "Z-A"),
        '3': (lambda x: x["date"], False, "ascending by date"),
        '4': (lambda x: x["date"], True, "descending by date")
    }

    # Perform sorting based on user's choice
    if sorting_choice in sort_functions:
        key_func, reverse, order = sort_functions[sorting_choice]
        travel_data[category].sort(key=key_func, reverse=reverse)
        print(f"\nSorted ({order}).")
    else:
        print("\nInvalid choice. Returning to the main menu.")
        display_menu()
        return

    # Display the sorted records
    print(f"\nSorted {category.capitalize()} List:")
    if travel_data[category]:
        for record in travel_data[category]:
            print(f"{record['country']} (Date: {record['date']})")
    else:
        print("No records found.")

    # Simplified exit/menu logic
    response = input("\nReturn to the main menu? (yes/no): ").strip().lower()
    if response == 'yes':
        print("Welcome back!")
    elif input("\nDo you want to exit the app? (yes/no): "
               ).strip().lower() == 'yes':
        print("\nThank you for using our application! Come back soon!")
        sys.exit()
    else:
        display_menu()


def display_records():
    """
    Displays the travel records for visited and wishlist countries.
    Prompts the user to add more countries if desired.
    """
    clear_terminal()
    print("\nHere are your travel records:")

    if travel_data["visited"]:
        print("\n\033[1;32mVisited Countries:\033[0m")
        for record in travel_data["visited"]:
            print(f"- {record['country']} (Visited on: {record['date']})")
    else:
        print("\n\033[1;32mVisited Countries:\033[0m No records yet!")

    if travel_data["wishlist"]:
        print("\n\033[1;33mWishlist Countries:\033[0m")
        for record in travel_data["wishlist"]:
            print(f"- {record['country']} (Planned for: {record['date']})")
    else:
        print("\n\033[1;33mWishlist Countries:\033[0m No records yet!")

    while True:
        choice = input("\nDo you want to add more countries? (yes/no): "
                       ).strip().lower()
        if choice == "yes":
            add_country()
            return  # Return immediately after calling add_country()
        if choice == "no":
            print("\nReturning to the main menu...\n")
            clear_terminal()
            break  # Exit the loop to return to the main menu
        print("\nInvalid input. Please answer 'yes' or 'no'.")


def travel_tracker_app():
    """
    Main function to run the Travel Tracker application.
    Provides the user with a menu to navigate through available options.
    """
    while True:
        display_menu()
        choice = input("\nChoose an option from the list (1-6): ").strip()
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
            print("\nThank you for using the Travel Tracker! 🌍\n")
            print("We hope your next adventure is unforgettable! 👋\n")
            sys.exit()
        else:
            print("Invalid choice, please try again.")


# Start the application
travel_tracker_app()

if __name__ == "__main__":
    display_menu()
