import random

pokemon = {
    "Shruptile": {
        "hp": 100,
        "moves": {
            "Shrubs": 20,
            "Thorns": 20
        }
    },
    "Zennar": {
        "hp": 100,
        "moves": {
            "Meditation": 10,
            "Mind Control": 30
        }
    }
}

player = {
    "name": "hehehe",
    "pokemon": "Ultramechachu"
}

enemy = {
    "name": "oh noes",
    "pokemon": "Electriciachu"
}

playerHP = pokemon[player["pokemon"]]["hp"]
enemyHP = pokemon[enemy["pokemon"]]["hp"]

while playerHP > 0 and enemyHP > 0:
    print(f"\n{player['pokemon']} HP: {playerHP}")
    print(f"{enemy['pokemon']} HP: {enemyHP}")

    moves = list(pokemon[player["pokemon"]]["moves"].keys())

    print("\nYour moves:")
    for i in range (len(moves)):
        move = moves[i]
        damage = pokemon[player["pokemon"]]["moves"][move]
        print(f"{i + 1}. {move} ({damage} dmg)")

    choice = int(input("Choose a move: ")) - 1

    move = moves[choice]
    damage = pokemon[player["pokemon"]]["moves"][move]

    enemyHP -= damage
    print(f"\n{player['pokemon']} used {move}!")
    print(f"It did {damage} damage!")

    if enemyHP <= 0:
        print("\nYou won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break

    enemy_moves = list(pokemon[enemy["pokemon"]]["moves"].keys())
    enemy_move = random.choice(enemy_moves)
    enemy_damage = pokemon[enemy["pokemon"]]["moves"][enemy_move]

    playerHP -= enemy_damage
    print(f"{enemy["pokemon"]} used {enemy_move}!")
    print(f"It did {enemy_damage} damage!")

    if playerHP <= 0:
        print("YOU LOST!!! AHAHHAHAHHAHHAHHAHHHA!!!!!!!!!!!!!!!!!!!!!!!!!!!")
