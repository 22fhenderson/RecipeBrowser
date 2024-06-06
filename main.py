import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect('RecipeBrowser.db')
cursor = conn.cursor()



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

def get_recipe_details():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ")
    instructions = input("Enter the instructions: ")
    category = input("Enter the category: ")
    prep_time = float(input("Enter the preparation time (in minutes): "))
    cook_time = float(input("Enter the cooking time (in minutes): "))
    total_time = prep_time + cook_time
    servings = input("Enter the number of servings: ")
    
    return name, ingredients, instructions, category, prep_time, cook_time, total_time, servings

def remove_recipe():
    conn = sqlite3.connect('RecipeBrowser.db')
    cursor = conn.cursor()
    name = input("Enter the name of the recipe to remove: ")
    cursor.execute('''
        DELETE FROM recipes WHERE name = ?
    ''', (name,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No recipe found with that name.")
    else:
        print("Recipe removed successfully!")
    conn.close()


     


 


def display_menu():
    print('''
 ██████   ██████                               
░░██████ ██████                                
 ░███░█████░███   ██████  ████████   █████ ████
 ░███░░███ ░███  ███░░███░░███░░███ ░░███ ░███ 
 ░███ ░░░  ░███ ░███████  ░███ ░███  ░███ ░███ 
 ░███      ░███ ░███░░░   ░███ ░███  ░███ ░███ 
 █████     █████░░██████  ████ █████ ░░████████
░░░░░     ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ 
           ''')
    """Display the menu options."""
    print("1. Add a Recipe")
    print("2. Find a Recipe")
    print("3. Change a Recipe")
    print("4. Delete a Recipe")
    print("5. Exit")

display_menu()

choice = input("What Would you like to do?\n> ")

while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
    print("That is not a valid input")
    again = input("try again\n> ")

if choice == '1':
            recipe_details = get_recipe_details()
            insert_recipe(*recipe_details)
elif choice == '4':
     remove_recipe()
elif choice == '5':
    print("Thank You For Using Recipe Browser")

# Commit the transaction
conn.commit()

# Close the connection

conn.close()
