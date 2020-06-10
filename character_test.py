from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()
dave.talk()
dave.set_conversation("AGGGGHHHHH")
dave.talk()

dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
