stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    count = 0
    print("Inventory:")
    for item in inventory:
        print(inventory[item], item)
        count = count + inventory[item]
    print("Total number of items:", count)
if __name__ == "__main__":
    displayInventory(stuff)
