from random import randint
from os import system

class Actor():
    def __init__(self):
        self.hp = 10 #health points
        self.hpmax = self.hp
        self.ap = 2 #action points
        self.atk1 = 2 #first attack 
        self.atkap1 = 1 #first attack AP
        self.atk2 = 8 #second attack
        self.atkap2 = 3 #second attack AP

player = Actor()
enemy = Actor()

def attack():

    while True:
        is_blocked = False
        action = input(f"Health Points - {player.hp} Action Points - {player.ap}\nEnemy Health - {enemy.hp}\n1. Weak attack (ap: {player.atkap1} dmg: {player.atk1})\n2. Strong attack (ap: {player.atkap2} dmg: {player.atk2 / 2}-{player.atk2})\n3. Block (AP - 0 Success Chance - 80%\n4. Wait (AP - +2)\n\n>> ")

        if action == "1":
            if player.ap >= player.atkap1:
                print(f"You did {player.atk1} damage!\n\n")
                enemy.hp -= player.atk1
                player.ap -= player.atkap1
                input("Press enter to continue.")
                break
            else:
                print("You don't have enough AP to use that attack...")
                input("Press enter to continue.")
                system("cls")
        elif action == "2":
            if player.ap >= player.atkap2:
                damage = randint(player.atk2/2, player.atk2)
                print(f"You did {damage} damage!\n\n")
                enemy.hp -= damage
                player.ap -= player.atkap2
                input("Press enter to continue.")
                break
            else:
                print("You don't have enough AP to use that attack...")
                input("Press enter to continue.")
                system("cls")
        elif action == "3":
            chance = randint(1, 10)

            if chance <= 8:
                print("The attack was blocked!\n\n")
                is_blocked = True
                input("Press enter to continue.")
                break
            else:
                print("The enemy broke through your block...\n\n")
                is_blocked = False
                input("Press enter to continue.")
                break
        elif action == "4":
            print("You gained 2 AP!")
            player.ap += 2
            input("Press enter to continue.")
            break
        else:
            input("please use one of the given options. Press enter to continue.")
            system("cls")
    system("cls")
    return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked:
        print(f"The enemy did {enemy.atk1} damage")
        player.hp -= enemy.atk1
    else:
        print("The attack is blocked!")

def start():
    print("This is the BATTLE SYSTEM")
    while True:

        blocked = attack()
        if int(enemy.hp) <= 0:
            print("You win!")
            input("Press enter to continue.")
            break
        elif int(player.hp) <= 0:
            print("You died... but I believe in you!")
            input("Press enter to continue.")
            break
        enemy_attack(blocked)
