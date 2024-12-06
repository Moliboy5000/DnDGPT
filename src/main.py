import apirequests
import classes
import functions
import os
import time

baseprompt = {"role": "system", "content": """
Your role is to act as a DM (and game engine) for a group of people playing a classic game of DnD.'
You will be describing the adventure and what happens and taking in player actions.
Each player has created a set of characters, whose information you will have for your disposal.
You are responsible for every aspect of the game including but not limited to
 player stats, abilites, items, leveling up and so forth.
Either on your own or by performing a function call on one of the provided functions.
 Note that any changes you made by a function called will be stored for your future convenience, good luck!



"""}



def main():
    players = []
    messages = [baseprompt]
    print("Welcome to DnDGPT, your DnD adventure powered by AI!")
    print("You will be playing an AI generated DnD adventure, note that this is an experimental version and may contain bugs, errors and unexpected results!")
    playeramount = int(input("How many players: "))
    os.system("clear")
    for i in range(playeramount):
        players.append(functions.create_character())
        os.system("clear")
    start = input("Character creation done, press enter to start your adventure: ")
    playing = True
    playerdata = ""
    for i in range(playeramount):
        playerdata += players[i].toString()
    messages.append({"role": "user", "content": f"Information about the players: {playerdata} " })


    while playing:
        response = apirequests.send_prompt(messages)
        print(response)
        messages.append({"role": "assistant", "content": response})
        prompt = input("Response: ")
        messages.append({"role": "user", "content": prompt})


        


if __name__ == "__main__":
    main()