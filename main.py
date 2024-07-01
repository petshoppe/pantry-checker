import ast

def get_pantry_list():
    """Loads pantry list from file or guides the user through initial setup."""
    # (Implementation from previous response) 

def display_pantry(pantry_list):
    """Prints the pantry list organized by category."""
    if not pantry_list:
        print("Your pantry is empty.")
        return

    categorized_pantry = {}
    for item, category in pantry_list:
        categorized_pantry.setdefault(category, []).append(item)

    for category, items in categorized_pantry.items():
        print(f"\n{category}:")
        for item in sorted(items):
            print(f"  - {item}")

def modify_pantry(pantry_list):
    """Allows the user to add or remove items from the list."""
    while True:
        action = input("Do you want to add or remove items? (add/remove/done): ").lower()

        if action == "add":
            item = input("Enter grocery item: ").title()
            category = input("Enter category for {}: ".format(item)).title()
            pantry_list.append([item, category])
        elif action == "remove":
            item = input("Enter grocery item to remove: ").title()
            if any(item in sublist for sublist in pantry_list):
                pantry_list = [sublist for sublist in pantry_list if item not in sublist]
            else:
                print(f"{item} not found in your pantry.")
        elif action == "done":
            break
        else:
            print("Invalid input. Please enter 'add', 'remove', or 'done'.")

    # Save modified list back to file
    with open("pantry.txt", "w") as f:
        f.write(str(pantry_list))


if __name__ == "__main__":
    first_time = input(
        "Is this your first time using the pantry checker? (yes/no): "
    ).lower() == "yes"
    pantry_list = get_pantry_list() if not first_time else []

    display_pantry(pantry_list)

    while True:
        if input("Is this list correct? (yes/no): ").lower() == "no":
            modify_pantry(pantry_list)
            display_pantry(pantry_list)
        else:
            break

    if input(
        "Do you want to save this as your ideal pantry? (yes/no): "
             ).lower() == "yes":
        with open("ideal_pantry.txt", "w") as f:
            f.write(str(pantry_list))

    print("Pantry saved. Goodbye!")

