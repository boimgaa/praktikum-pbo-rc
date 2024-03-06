import random

class Animal:
    def __init__(self, name, attack, hp, attack_accuracy=0.8):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.attack_accuracy = attack_accuracy

    def attack_enemy(self, enemy):
        if random.random() < self.attack_accuracy:
            damage = self.attack
            enemy.receive_attack(damage)
            print(f"{self.name} attacks {enemy.name} and deals {damage} damage!")
        else:
            print(f"{self.name}'s attack missed!")

    def receive_attack(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} receives {damage} damage. {self.name}'s HP: {self.hp}")

    def heal_hp(self):
        self.hp = min(self.max_hp, self.hp + 10)  # Heal 10 HP

class BattleAnimals:
    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2
        self.rounds = 0

    def start_game(self):
        print("----- Battle Begins -----")
        while self.animal1.hp > 0 and self.animal2.hp > 0:
            self.rounds += 1
            print(f"--- Round {self.rounds} ---")
            self.animal1.attack_enemy(self.animal2)
            if self.animal2.hp <= 0:
                break  # Animal 2 is defeated
            self.animal2.attack_enemy(self.animal1)
            if self.animal1.hp <= 0:
                break  # Animal 1 is defeated
            self.animal1.heal_hp()
            self.animal2.heal_hp()

        print("----- Battle Ends -----")
        print(f"Total Rounds: {self.rounds}")
        if self.animal1.hp <= 0:
            print(f"{self.animal2.name} wins!")
        elif self.animal2.hp <= 0:
            print(f"{self.animal1.name} wins!")

# Example Usage:
animal1 = Animal("Animal1", attack=80, hp=400)
animal2 = Animal("Animal2", attack=30, hp=340)

battle = BattleAnimals(animal1, animal2)
battle.start_game()
