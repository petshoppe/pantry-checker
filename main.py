import ast  # For loading data from file

def get_pantry_list():
    """Loads pantry list from file or guides the user through initial setup."""
    try:
        with open("pantry.txt", "r") as f:
            return ast.literal_eval(f.read())
    except FileNotFoundError:
        # First-time setup logic here (collect items, categories, etc.)
        # ...

def display_pantry(pantry_list):
    """Prints the pantry list organized by category."""
    # ...

def modify_pantry(pantry_list):
    """Allows the user to add or remove items from the list."""
    # ...

# Main execution
if __name__ == "__main__":
    first_time = input("Is this your first time using the pantry checker? (yes/no): ").lower()

    pantry_list = get_pantry_list() if first_time == "no" else [] 

    # Continue with display_pantry, modify_pantry, and ideal list saving logic...
import ast  # For loading data from file
























