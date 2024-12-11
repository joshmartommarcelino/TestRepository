items = {
    "001" : ("sprite", 1.25),
    "002" : ("pepsi", 1.25),
    "003" : ("coke", 1.25),
    "004" : ("pepsi max", 1.50),    
}

def display():
    """Displays all items and their prices."""
    print("\nAvailable Products:")
    for item_code, (name,price)in items.items(): #Loops and goes through the dictionary of items
        print(f"{item_code} : {name} is ${price:.2f}") #Prints the item code, name, and price

display() #call the function to display the items
def select_item():
    code = input("\nEnter the item you wish to purchase: ").upper() #Takes user input for item code
    if code in items: #checks if the code you entered is in the dictionary
        return code
    else:
        print("Invalid item code. Please try again.")
        return None