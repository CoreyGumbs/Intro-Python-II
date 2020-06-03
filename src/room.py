# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def addItem(self, item):
        if item not in self.items:
            self.items.append(item)
        elif item in self.items:
            raise Exception(f"Item is already located in {self.name}\n")

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        elif item not in self.items:
            raise Exception(f"Item does not exist in {self.name}\n")
    
    def showItems(self):
        if len(self.items) == 0:
            print(f"ROOM ITEMS:\n")
            print("There are currenly no items in this room.")
        elif len(self.items) >= 1: 
            print(f"ROOM ITEMS:\n")
            for i, val in enumerate(self.items):
                print(f"{val.name}: {val.description}") 
        print("\n\n")
    
    def __str__(self):
        return f"{self.name} : {self.description}"