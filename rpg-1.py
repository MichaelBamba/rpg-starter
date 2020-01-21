class Hero:
    health = 10
    power = 5
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin:
    health = 6
    power = 2
    def __init__ (self, health, power):
        self.health
        self.power

class Dragon:
    health = 100
    power = 1000000000
    
while Hero.health > 0:
    while Goblin.health > 0 and Hero.health > 0:
        print("You have %d health and %d power." % (Hero.health, Hero.power))
        print("The Goblin has %d health and %d power." % (Goblin.health, Goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight Goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input =="1":
            Goblin.health -= Hero.power
            print("You do %d damage to the Goblin." % Hero.power)
            if Goblin.health <= 0:
                print("The Goblin is dead.")
        elif user_input == "2":
            print ("you lazy bum its gonna kill you")
            pass
        elif user_input == "3":
            print ("coward don't come back")
            break
        else :
            print("you are confused")


        if Goblin.health > 0:
            Hero.health -= Goblin.power
            print ("Goblin does %d damage to you." % Goblin.power)
            if Hero.health <=0:
                print("you are dead how?")
    while Goblin.health < 0 and Dragon.health == 100:
        print("you won this fight")
        print ("1. go back to town")
        print ("4. fight dragon")
        user_input = input()
        if user_input == "1":
            print("you return to Gobstrum")
            print ("1. go to the black smith")
            print("2. go to the wizard")
            print("3. go to the cleric")
            print ("4. go fight the dragon")
            user_input = input()
            if user_input == "1":
                print("you recieved a anti dragon sword from the buff blacksmith")
                Hero.power = 20

            elif user_input == "2":
                print("you recieved antimagic shield from the crazy wizard")
                Dragon.power = 10

            elif user_input == "3":
                print("the cleric increases your vitaltiy and heals you")
                Hero.health = 100
            else:
                print("you go to the bar. Get drunk and lose a bar fight")
                print("you become a drunkard mercenary")
                break
        if user_input == "4":
                print("You have %d health and %d power." % (Hero.health, Hero.power))
                print()
                print("What do you want to do?")
                print("1. fight Dragon")
                print("2. do nothing")
                print("3. flee")
                print("4.seduce the dragon")
                print("> ",)
                user_input = input()
                if user_input =="1":
                    Dragon.health -= Hero.power
                    print("You do %d damage to the Dragon." % Hero.power)
                    if Dragon.health <= 0:
                        print("The Dragon is dead.")
                        print("You saved the realm")
                        break
                elif user_input == "2":
                    print ("you lazy bum its gonna kill you")
                    pass
                elif user_input == "3":
                    print ("coward don't come back")
                    break
                elif user_input== "4":
                    print("this is not DnD it is to big")
                    print("it breaks you")
                    break
                else :
                    print("you are confused")


                if Dragon.health > 0:
                    Hero.health -= Dragon.power
                    print ("Dragon does %d damage to you." % Dragon.power)
                    if Hero.health <=0:
                        print("you are dead")
                        print ("better luck next time")
                        break
                else:
                    ("you fall off a cliff in confusion")
                    break
        while Dragon.health > 0 and Dragon.health < 100:
            print("You have %d health and %d power." % (Hero.health, Hero.power))
            print()
            print("What do you want to do?")
            print("1. fight Dragon")
            print("2. do nothing")
            print("3. flee")
            print("4.seduce the dragon")
            print("> ",)
            user_input = input()
            if user_input =="1":
                Dragon.health -= Hero.power
                print("You do %d damage to the Dragon." % Hero.power)
                if Dragon.health <= 0:
                    print("The Dragon is dead.")
                    print("You saved the realm")
                    break
            elif user_input == "2":
                print ("you lazy bum its gonna kill you")
                pass
            elif user_input == "3":
                print ("coward don't come back")
                break
            elif user_input== "4":
                print("this is not DnD it is to big")
                print("it breaks you")
                break
            else :
                print("you are confused")


            if Dragon.health > 0:
                Hero.health -= Dragon.power
                print ("Dragon does %d damage to you." % Dragon.power)
                if Hero.health <=0:
                    print("you are dead")
                    print ("better luck next time")
                    break
            else:
                ("you fall off a cliff in confusion")
                break