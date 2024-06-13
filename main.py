import sqlite3
import time
import os
# Establish connection to the SQLite database
conn = sqlite3.connect('RecipeBrowser.db')
cursor = conn.cursor()
  

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
    print("Returning to the Menu")
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
            print("Returning to Main Menu")
            time.sleep(3)
            os.system('cls')
            break
    

def change_recipe():
    while True:
        name = input("Enter the name of the recipe to change (or type 'cancel' to exit): ")
        
        if name.lower() == 'cancel':
            print("Operation cancelled.")
            break
        
        cursor.execute('''
            SELECT * FROM recipes WHERE name = ?
        ''', (name,))
        recipe = cursor.fetchone()
        
        if recipe is None:
            print("No recipe found with that name. Please try again.")
        else:
            print("Enter the new details for the recipe (leave blank to keep the current value):")
            print(f"Current name: {recipe[1]}")
            new_name = input("Enter the new recipe name: ") or recipe[1]
            print(f"Current ingredients: {recipe[2]}")
            new_ingredients = input("Enter the new ingredients (comma-separated): ") or recipe[2]
            print(f"Current instructions: {recipe[3]}")
            new_instructions = input("Enter the new instructions: ") or recipe[3]
            print(f"Current category: {recipe[4]}")
            new_category = input("Enter the new category (Breakfast, Lunch, Dinner or All): ") or recipe[4]
            print(f"Current preparation time: {recipe[5]} minutes")
            new_prep_time = input("Enter the new preparation time (in minutes): ")
            new_prep_time = float(new_prep_time) if new_prep_time else recipe[5]
            print(f"Current cooking time: {recipe[6]} minutes")
            new_cook_time = input("Enter the new cooking time (in minutes): ")
            new_cook_time = float(new_cook_time) if new_cook_time else recipe[6]
            new_total_time = new_prep_time + new_cook_time
            print(f"Current servings: {recipe[8]}")
            new_servings = input("Enter the new number of servings: ") or recipe[8]

            cursor.execute('''
                UPDATE recipes
                SET name = ?, ingredients = ?, instructions = ?, category = ?, prep_time = ?, cook_time = ?, total_time = ?, servings = ?
                WHERE name = ?
            ''', (new_name, new_ingredients, new_instructions, new_category, new_prep_time, new_cook_time, new_total_time, new_servings, name))
            conn.commit()
            print("Recipe updated successfully!")
            time.sleep(1)
            print("Returning to the Menu")
            time.sleep(2)
            break
    
    
    

def find_all_recipes():
    cursor.execute('''
        SELECT * FROM recipes
    ''')
    recipes = cursor.fetchall()

    if recipes:
        print("All Recipes:")
        for recipe in recipes:
            print_recipe(recipe)
    else:
        print("No recipes found.")

def find_recipe_by_keyword():
    print("Choose a search option:")
    print("1. Name")
    print("2. Ingredients")
    print("3. Instructions")
    print("4. Category")
    print("5. Preparation Time")
    print("6. Cooking Time")
    print("7. Total Time")
    print("8. Servings")
    option_choice = input("Enter your choice: ")

    if option_choice == '1':
        keyword = input("Enter a name to search for: ").lower()
        cursor.execute('''
            SELECT * FROM recipes
            WHERE LOWER(name) LIKE ?
        ''', ('%' + keyword + '%',))
    elif option_choice == '2':
        keyword = input("Enter ingredients to search for: ").lower()
        cursor.execute('''
            SELECT * FROM recipes
            WHERE LOWER(ingredients) LIKE ?
        ''', ('%' + keyword + '%',))
    elif option_choice == '3':
        keyword = input("Enter instructions to search for: ").lower()
        cursor.execute('''
            SELECT * FROM recipes
            WHERE LOWER(instructions) LIKE ?
        ''', ('%' + keyword + '%',))
    elif option_choice == '4':
        keyword = input("Enter a category to search for: ").lower()
        cursor.execute('''
            SELECT * FROM recipes
            WHERE LOWER(category) LIKE ?
        ''', ('%' + keyword + '%',))
    elif option_choice == '5':
        prep_time = float(input("Enter maximum preparation time (in minutes): "))
        cursor.execute('''
            SELECT * FROM recipes
            WHERE prep_time <= ?
        ''', (prep_time,))
    elif option_choice == '6':
        cook_time = float(input("Enter maximum cooking time (in minutes): "))
        cursor.execute('''
            SELECT * FROM recipes
            WHERE cook_time <= ?
        ''', (cook_time,))
    elif option_choice == '7':
        total_time = float(input("Enter maximum total time (in minutes): "))
        cursor.execute('''
            SELECT * FROM recipes
            WHERE total_time <= ?
        ''', (total_time,))
    elif option_choice == '8':
        servings = int(input("Enter minimum number of servings: "))
        cursor.execute('''
            SELECT * FROM recipes
            WHERE servings >= ?
        ''', (servings,))
    else:
        print("Invalid choice.")
        return

    results = cursor.fetchall()

    if results:
        print("Recipes found:")
        for result in results:
            print_recipe(result)
    else:
        print("No recipes found with the specified criteria.")

def print_recipe(recipe):
    print(f'''
    ID: {recipe[0]}
    Name: {recipe[1]}
    Ingredients: {recipe[2]}
    Instructions: {recipe[3]}
    Category: {recipe[4]}
    Preparation Time: {recipe[5]} minutes
    Cooking Time: {recipe[6]} minutes
    Total Time: {recipe[7]} minutes
    Servings: {recipe[8]}
    ''')


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
    print("Welcome to Recipe Browser")
    print("This code will allow you to add, search, change and delete recipes from a database. ")
    print("\n1. Add a Recipe")
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
            while True:
                print("\n1. Show all recipes")
                print("2. Search for a recipe by keyword")
                sub_choice = input("Enter your choice (or 'exit' to return to the main menu): ")
                
                if sub_choice == '1':
                    find_all_recipes()
                elif sub_choice == '2':
                    find_recipe_by_keyword()
                elif sub_choice.lower() == 'exit':
                    break
                else:
                    print("Invalid choice. Please enter '1', '2', or 'exit'.")
        elif choice == '3':
            print("Change a Existing Recipe.")
            change_recipe()
        elif choice == '4':
            print("Remove a Recipe")
            remove_recipe()
        elif choice == '5':
            print("Thank you for using Recipe Browser. \nGoodbye!")
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