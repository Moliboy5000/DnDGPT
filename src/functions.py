import classes
import random

def roll():
    """
    Performs a roll and returns the result.

    Returns:
        int: the result of the roll, between 0 and 20.
    """
    return random.randint(0,20)


def create_character():
    """
    Creates a player character from user prompts

    Returns:
        Entity: the player character.
    """
    name = input("What is your character's name:")
    race = input("What is your character's race (choose one of the classic or create your own with a description):")
    entityclass = input("What is your class  (choose one of the classic or create your own with a description): ")
    description = input("Give your character a short story/background: ")
    stats = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    print("Now, we will roll for stats")
    rolls = []
    for i in range(6):
        result = random.randint(3,20)
        rolls.append(result)
        print(f"You rolled a: {result} ")

    for i in range(6):
        add = input(f"Assign {rolls[i]} to: ")
        stats[add] += rolls[i]
    return classes.Entity(name, race, 100,  entityclass, description, stats)

def set_health(entity, value):
    entity.health = value
    print(f"{entity.name} health now {value}")

def set_stat(entity, stat, value):
    entity.stats[stat] = value
    print(f"{entity.name} {stat} now {value}" )





