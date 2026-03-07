
name = input("Hallo, Wie heißt du?")

player = {
    "name": name,
    "hp": 100,
    "attack": 10,
    "inventory": []
}

goblin = {
    "name": "goblin",
    "hp": 50,
    "attack": 5,
    "inventory": []
}

wolf = {
    "name": "wolf",
    "hp": 80,
    "attack": 16,
    "inventory": []
}

ork = {
    "name": "ork",
    "hp": 150,
    "attack": 20,
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
        enemy = random.choice([goblin, wolf, ork])
        print(f"Ein {enemy["name"]} erscheint") 
        enemy_hp = enemy["hp"]

        while enemy_hp > 0 and player["hp"] > 0:
            print("1 - Angreifen!!!")
            print("2 - Fliehen")

            action = input(">>> ")

            if action == "1":
                enemy_hp -= player["attack"]
                print(f"Du machst {player['attack']} Schaden!")
                
                if enemy_hp <= 0:
                    print(f"Der {enemy["name"]} wurde besiegt!")
                    break

                player["hp"] -= enemy["attack"]
                print(f"Der {enemy['name']} hat {enemy['attack']} gemacht")
                
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
        print("Inventar", player["inventory"])

    elif choice == "3":
        print("Du hast das Spiel verlassen.")
        break
    else:
        print("Ungültige Eingabe")
        
       