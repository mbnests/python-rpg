import random

#Parent class.
class Character:

    #Defining init function that takes name, hp, and attack power as an input.
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.max_hp = hp

    #Take damage method contains new input amount that will be subtracted from the hp.
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

        print(f"{self.name} took {amount} damage! Health is now {self.hp}.")

    #Checking if hp is greater than zero to return true else return false inside is alive method.
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    #Defining attack method that will return the random attack value from attack veriable and returns it.
    def attack(self):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        return damage

#Child class hero that will inherit from the class Character.
class Hero(Character):

    #Defining new init method with new input potions
    def __init__(self, name, hp, attack_power, potions):
        #super function is defined so parent charaterstics can remain inside hero class.
        super().__init__(name, hp, attack_power)
        self.potions = potions

    #Heal mwthod will heal the hero.
    def heal(self):
        if self.potions > 0:
            self.potions -= 1
            self.hp += 30
        elif self.potions <= 0:
            print("Out of potions!")

        #Max hp should be equal tot he hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
        print(f"{self.name} now have {self.potions} potions! Health is now {self.hp}.")

#Another child class boss inherited from Character class .
class Boss(Character):

        #This will return randomly created attack power and give damage to hero.
        def heavy_attack(self):
            return random.randint(self.attack_power, self.attack_power + 15)

#Creating multiple monsters using tuple inside a list.
monster_data = [
    ("Goblin", 50, 10),
    ("Orc", 80, 15),
    ("Troll", 120, 18),
    ("Dragon", 150, 25),
]

#Creating a hero.
player = Hero("Arthur", 100, 20, 3)
monsters_defeated = 0


print("--- WELCOME TO THE ENDLESS DUNGEON ---")
#The outer while loop which spawns the monsters.
while player.is_alive():

    #Creating random monsters.
    random_monster_spawn = random.choice(monster_data)
    #Unpacking the tuple.
    name, hp, attack_power = random_monster_spawn
    current_enemy = Boss(name, hp, attack_power)
    print(f"ROOM {monsters_defeated + 1}: A wild {current_enemy.name} appeared with {current_enemy.hp} hp and have {current_enemy.attack_power} attack power.")

    #Inner loop where user will decide to attack or to heal.
    while player.is_alive() and current_enemy.is_alive():

        choice = input("Enter 1 to attack or enter 2 to heal: ")

        #Hero attacks and monster attacks back when user press the 1.
        if choice == "1":
            damage = player.attack()
            print(f"{player.name} strikes!")
            current_enemy.take_damage(damage)

            if current_enemy.is_alive():
                enemy_damage = current_enemy.heavy_attack()
                print(f"{current_enemy.name} strikes back!")
                player.take_damage(enemy_damage)

        #When user press the 2 hero will heal.
        elif choice == "2":
            player.heal()
        else:
            print("You hvae entered the invalid digit.")

    if player.is_alive():
        print(f"You have defeated the {current_enemy.name}.")
        monsters_defeated += 1
        player.potions += 1

print("--- GAME OVER ---")
print(f"You survived {monsters_defeated} rooms!")
