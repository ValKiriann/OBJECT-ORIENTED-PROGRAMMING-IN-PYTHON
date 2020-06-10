from room import Room
from character import Enemy
from character import Friend
from item import Item

backpack = []

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(kitchen, "east")

cheese = Item("Cheese", "A tasty piece of Brie cheese is lying on the counter")
kitchen.set_item(cheese)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("Cheese")
dining_hall.set_character(dave)

# Add a new character
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

current_room = kitchen
game = True

while game:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("Nobody is here")
    elif command == "fight":
        if inhabitant is None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            if not backpack:
                print("You dont have anything in your backpack")
            else:
                item = ""
                while item.capitalize() not in backpack:
                    print("Choose an item in your backpack")
                    print("Things in your backpack: " + ', '.join(backpack))
                    item = input()
                if inhabitant.fight(item.capitalize()):
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    game = False
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
    elif command == "exit":
        print("See you soon!")
        game = False

    elif command == "take":
        if item is not None:
            backpack.append(item.name)
            print("You take " + item.name + " and put it into your backpack")
            current_room.set_item(None)
        else:
            print("There's nothing to take from this room")
