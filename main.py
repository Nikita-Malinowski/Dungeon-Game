
name = input("Hallo, Wie heißt du? ")

player = {
    "name": name,
    "hp": 100,
    "attack": (5, 10),
    "gold": 0,
    "inventory": []
}

goblin = {
    "name": "goblin",
    "hp": 50,
    "attack": (3, 5),
    "inventory": []
}

wolf = {
    "name": "wolf",
    "hp": 80,
    "attack": (8, 16),
    "inventory": []
}

ork = {
    "name": "ork",
    "hp": 150,
    "attack": (10, 20),
    "inventory": []
}

print("Willkommen im Dungeon" ,name )

import random

while True:
    print("Was möchtest du tun")
    print("1 - Dungeon weiter erkunden")
    print("2 - Werte anschauen")
    print("3 - Das Spiel verlassen")

    choice = input(">>> ")
  

    if choice == "1":
        print("Du gehst tiefer in den Dungeon rein.")
        chance = random.randint(1, 100)

        if chance <= 50:
            enemy = goblin
        elif chance <= 80:
            enemy = wolf
        else:
            enemy = ork

        print(f"Ein {enemy["name"]} erscheint") 
        enemy_hp = enemy["hp"]

        while enemy_hp > 0 and player["hp"] > 0:
            print("1 - Angreifen!!!")
            print("2 - Fliehen")

            action = input(">>> ")

            if action == "1":

                damage = random.randint(*player["attack"])
                enemy_hp -= damage

                print(f"Du machst {damage} Schaden!")

                enemy_damage = random.randint(*enemy["attack"])

                player["hp"] -= enemy_damage
                print(f"Der {enemy['name']} hat {enemy_damage} Schaden gemacht")
                
                if enemy_hp <= 0:
                    print(f"Der {enemy["name"]} wurde besiegt!")
                    
                    loot = random
                    gold = random

                    if enemy == goblin:
                        gold = random.randint(1, 5)
                        loot = random.choices(
                            ["nichts", "Dolch", "Stoff", "Heiltrank"],
                            weights=[50, 29, 20, 1]
                        )[0]
                    elif enemy == wolf:
                        gold = random.randint(2, 8)
                        loot = random.choices(
                            ["nichts", "Fell", "Fleisch", "Klinge"],
                            weights=[40,30, 25, 5]
                        )[0]
                    elif enemy == ork:
                        random.randint(5, 15)
                        random.choices(
                            ["Schwert", "Schild", "Heiltrank", "nichts"],
                            weights=[40, 40, 20, 10]
                        )[0]
                    
                    print(f"Du hast {loot} und {gold} gold bekommen.")

                    player["inventory"].append(loot)
                    player["gold"] += gold
                
            elif action == "2":
                print("Du fliehst")
                break
            
        if player["hp"] <= 0:
            print("Du wurdest besiegt")
            break

    elif choice == "2":
        print("Name", player["name"])
        print("HP", player["hp"])
        print("Attack", player["attack"])
        print("gold", player["gold"])
        print("Inventar", player["inventory"])

    elif choice == "3":
        print("Du hast das Spiel verlassen.")
        break
    else:
        print("Ungültige Eingabe")
        
       