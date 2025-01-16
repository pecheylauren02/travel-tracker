# Travel Tracker Application

## Overview

The Travel Tracker Application is a Python-based console program designed to help users manage and track their travel experiences. It allows users to add countries they have visited or countries they wish to visit to their travel records. The application includes features for sorting, searching, and deleting countries from the lists, as well as validating input to ensure accuracy.

This program is structured to work with the user's travel records by providing them the ability to interact with a simple menu-driven interface. It utilizes several modules such as `os`, `sys`, `re`, and `datetime` for system operations, input validation, and date handling.

## Features

- **Add a Country**: Allows users to add a country to either their "visited" or "wishlist" categories.
- **Delete a Country**: Enables users to delete countries from either category with confirmation prompts.
- **Search for a Country**: Users can search for a country in their lists and add it if not already present.
- **Sort Countries**: Organize countries in the list by name.
- **Display All Countries**: View all countries across both categories.
- **Age and Date Validation**: Ensures that the user’s age and the travel date are valid and appropriate for each category.

## Prerequisites

This application is written in Python and uses the following Python modules:

- `os`: for interacting with the operating system (e.g., clearing the terminal).
- `sys`: for system-specific parameters and functions.
- `re`: for regular expression matching and operations.
- `datetime`: for working with date and time objects.

Ensure you have Python 3.12.6 installed on your system to run the application.

## Installation

There is no formal installation required to use the application. Just follow these steps:

1. Clone or download the script from the repository:
   - Clone: `git clone https://github.com/your-repository/travel-tracker.git`
   - Or download the ZIP file and extract it.

2. Navigate to the project directory:
   - `cd travel-tracker`

3. Ensure that Python is installed on your machine.

4. Run the script using Python:
   - `python3 main.py`

## How to Use

### Running the Application
After running the script, you will be presented with a menu of options to choose from:
- Add a country
- Delete a country
- Search for a country
- Sort your countries
- Display all countries
- Exit



### Add a Country:
- When prompted, enter the country you want to add to your "visited" or "wishlist" category.
- You will also need to input your age if adding to the "visited" category for the first time.
- The application will validate the entered country, age (if applicable), and travel date.
- The date format should be in `dd-mm-yyyy`.



### Delete a Country:
- You can remove a country from either your "visited" or "wishlist" list by entering the country name.
- A confirmation will be requested to ensure the correct deletion.



### Search for a Country:
- Search for a country in your records. If it is not found, you can choose to add it to your lists.



### Sort Countries:
- This feature will allow you to organize the countries in your lists alphabetically.



### Display All Countries:
- View the entire list of countries in both the "visited" and "wishlist" categories.



### Exit:
- Exit the application when done.



## Input Validations

- **Country**: The application validates the country against a predefined list of valid countries. If the entered country is not on the list, the user will be prompted to re-enter it.
- **Age**: The application asks for the user's age when adding a country to the "visited" list for the first time. The age must be a number between 1 and 120.
- **Date**: The travel date must be entered in the `dd-mm-yyyy` format. The application also ensures that:
  - For "visited" countries, the date cannot be in the future.
  - For "wishlist" countries, the date must be in the future.

## Example Usage

### Menu:


## Data Storage

Travel records are stored in-memory during the session. If you wish to persist data between sessions, you would need to implement file handling (e.g., saving to a CSV or database) to store and retrieve the data.

## Customization

Feel free to modify the `valid_countries` list to include additional countries or adjust the age and date validation rules to suit your needs.

## Testing

To ensure the application is working correctly and follows best practices, thorough testing has been performed, including:

### Manual User Story Testing
The application has been manually tested to validate each user story, ensuring the following functionalities work as expected:
- Adding, deleting, searching, and sorting countries.
- Proper input validation for countries, ages, and travel dates.
- User-friendly interactions via the terminal.

### Pylint
The code was analyzed using **Pylint** to check for any coding standard violations, errors, or warnings. Pylint ensures that the code follows the PEP 8 guidelines and is maintainable.

### Flake8
**Flake8** was used to check the Python code for compliance with style guides and to detect any errors or inconsistencies in the code structure.

### Coverage
The testing process confirmed that the following aspects were thoroughly covered:
- Functional requirements of the application.
- Input validation and edge cases.
- Code readability and consistency with the help of Pylint and Flake8.

If you would like to run the tests yourself or add new tests, you can run **Pylint** and **Flake8** via the following commands:

- To run Pylint:
  ```bash
  pylint main.py

## Conclusion

The Travel Tracker Application provides a simple, interactive way to manage and track travel experiences. Its user-friendly interface and robust validation ensure that users can maintain accurate records of the countries they have visited or wish to visit. The app is easily extensible, allowing developers to add features like data persistence or improved sorting and filtering options.





