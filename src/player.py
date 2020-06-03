# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    
    def movePlayer(self, room):
        self.room = room

    def playerRoom(self):
        return self.room

    def getItem(self, item):  
        self.inventory.append(item)
    
    def dropItem(self, item):
        self.inventory.remove(item)

    def showInventory(self):
        print("Player Inventory: \n")
        if len(self.inventory) >= 1:
            for i, val in enumerate(self.inventory):
                print(f"{val.name}: {val.description}")
        else:
            print('There is nothing in your inventory')
        print("\n\n")

    def __str__(self):
        return f"{self.name}: {self.room.name}"