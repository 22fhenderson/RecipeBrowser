import sqlite3
import time
import os
# Establish connection to the SQLite database
conn = sqlite3.connect('RecipeBrowser.db')
cursor = conn.cursor()
  
import sqlite3

# Function to insert a new recipe into the recipes table
def insert_recipe(name, ingredients, instructions, category, prep_time, cook_time, total_time, servings):
    conn = sqlite3.connect('RecipeBrowser.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO recipes (name, ingredients, instructions, category, prep_time, cook_time, total_time, servings)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, ingredients, instructions, category, prep_time, cook_time, total_time, servings))
    conn.commit()
    conn.close()
    print("Recipe added successfully!")
    time.sleep(3)
    os.system('cls')

# Function to get recipe details from the user
def get_recipe_details():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ")
    instructions = input("Enter the instructions: ")
    category = input("Enter the category (Breakfast, Lunch, Dinner or All): ")
    prep_time = float(input("Enter the preparation time (in minutes): "))
    cook_time = float(input("Enter the cooking time (in minutes): "))
    total_time = prep_time + cook_time
    servings = input("Enter the number of servings: ")
    
    return name, ingredients, instructions, category, prep_time, cook_time, total_time, servings

# Function to remove a recipe from the recipes table
def remove_recipe():
    conn = sqlite3.connect('RecipeBrowser.db')
    cursor = conn.cursor()
    
    while True:
        name = input("Enter the name of the recipe to remove (or type 'cancel' to exit): ")
        
        if name.lower() == 'cancel':
            print("Operation cancelled.")
            break
        
        cursor.execute('''
            DELETE FROM recipes WHERE name = ?
        ''', (name,))
        conn.commit()
        
        if cursor.rowcount == 0:
            print("No recipe found with that name. Please try again.")
        else:
            print("Recipe removed successfully!")
            time.sleep(3)
            os.system('cls')
            break
    
    conn.close()

def change_recipe():
    conn = sqlite3.connect('RecipeBrowser.db')
    cursor = conn.cursor()
    while True:
        change = input("What Recipe Would you Like to Change: ")
    

# Function to display the menu options
def display_menu():
    print('''\033[0;35;48m
 ██████   ██████                               
░░██████ ██████                                
 ░███░█████░███   ██████  ████████   █████ ████
 ░███░░███ ░███  ███░░███░░███░░███ ░░███ ░███ 
 ░███ ░░░  ░███ ░███████  ░███ ░███  ░███ ░███ 
 ░███      ░███ ░███░░░   ░███ ░███  ░███ ░███ 
 █████     █████░░██████  ████ █████ ░░████████
░░░░░     ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ 
          \033[0;37;48m''')
    
    print("1. Add a Recipe")
    print("2. Find a Recipe")
    print("3. Change a Recipe")
    print("4. Delete a Recipe")
    print("5. Exit")

# Main function to run the program
def main():
    while True:
        os.system('cls')
        display_menu()
        choice = input("What would you like to do?\n> ")

        if choice == '1':
            print("Add a New Recipe")
            recipe_details = get_recipe_details()
            insert_recipe(*recipe_details)
        elif choice == '2':
            print("Search the Database for a Recipe.")
        elif choice == '3':
            print("Change a Existing Recipe.")
        elif choice == '4':
            print("Remove a Recipe")
            remove_recipe()
        elif choice == '5':
            print("Thank you for using Recipe Browser. Goodbye!")
            break
        elif choice == "Jacob Mcrae Location":
            print("Jacob Mcrae Lives at 1 Helms Court Arrowtown New Zealand")
            time.sleep(2)
            os.system('cls')
        else:
            print("Invalid input. Please try again.")


main()

conn.commit
conn.close