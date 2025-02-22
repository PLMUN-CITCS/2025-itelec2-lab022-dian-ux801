"""
Menu-Driven Program
Handles user input and performs operations using functions.
"""

def display_menu():
    """Displays the menu options."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    """Prints a greeting message."""
    print("Hello! Welcome!")

def check_even_odd():
    """Asks for an integer input and checks if it's even or odd."""
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num % 2 == 0:
                print(f"{num} is an Even number.")
            else:
                print(f"{num} is an Odd number.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def handle_menu_choice(choice):
    """Executes actions based on user choice."""
    if choice == 1:
        greet_user()
    elif choice == 2:
        check_even_odd()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
    return False

if __name__ == "__main__":
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(user_choice):
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
