
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        b = int(input("Write a number: "))
        print(pokemons[b-1])

        pass
    elif choice == '2':
        def custom_sort(pokemons):
            return int(pokemons["attack"])  

        sorted_pokemons = sorted(pokemons, key=custom_sort, reverse=True)

        for i in range(10):
            print(sorted_pokemons[i])
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def custom_sort(pokemons):
            return int(pokemons["attack"])  

        sorted_pokemons = sorted(pokemons, key=custom_sort)

        for i in range(10):
            print(sorted_pokemons[i])
        pass
    elif choice == '4':
        # Battle
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health - lost
        bot = random.choice(pokemons)
        print(bot)
        p = int(input("Choose your pokemon: "))
        pok = pokemons[p-1]
        print("Your Pokemon: ", pok)
        print("The battle starts")
        print("Your pokemon attacks first")
        total_bot = bot["total"]
        total_pok = pok["total"]
        attack_bot = bot["attack"]
        attack_pok = pok["attack"]
        defense_bot = bot["defense"]
        defense_pok = pok["defense"]
        while True:
            pok_attack = attack_pok - defense_bot + random.choice(range(0, 20))
            if pok_attack < 0:
                pok_attack = 0
            
            total_bot = total_bot - pok_attack
            print("Your pokemon's attack: ", pok_attack, "Bot's hp: ", total_bot)
            if total_bot < 0:
                print("You won")
                break
            bot_attack = attack_bot - defense_pok + random.choice(range(0, 20))
            if bot_attack < 0:
                bot_attack = 0
            total_pok = total_pok - bot_attack
            print("Bot's attack: ", bot_attack, "Your pokemon's hp: ", total_pok)
            if total_pok < 0:
                print("Bot won")
                break
            
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")



