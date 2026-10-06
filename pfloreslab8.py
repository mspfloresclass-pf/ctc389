#Patricia Flores
#Lab 8 
# In this lab you will create an interactive story for a user to play. It will be similiar to a choose your own adventure.
#Your program must guide the user through at least 5 different decisions and each decision must have at least 3 options to choose from. 
#Your story must be different from the example below. The example only shows 3 different decisions because the user died but your game should have at lease 5 decisions to win. After the game is over ask the user if they would like to play again. 
#The user should be able to play the game as long las they choose "yes" at the end. 


next_play = "yes"

while next_play =="yes":
    username = input("Welcome Jedi Knight! What is your name:")
    print("Hello",username,"The Storm Troopers just landed on the peaceful planet of Naboo. You will be teleported to create an army and fight and save the princess.You must make the right decisions to fight the battle against the Storm Troopers and win")
    print("You have landed on the planet of Naboo. You see three trails, a trail to your right, a trail to your left, and a trail on the middle. Choose your trail")

# Decision 1 - Choose your Trail
    trails = ["Trail to your Right","Trail to your Left", "Trail in the Middle"]
    print(1, trails[0])
    print(2, trails[1])
    print(3, trails[2])

    your_pick = int(input("Select your options:1: Trail to your Right. Select 2: Trail to your Left. Select 3: Trail in the Middle"))
    
    if your_pick == 1:
        print ("It looks like you chose the trail to your right.",username)
        print ("You will encounter Captain Panaka Head of the Royal Security Force,")
        print ("He greets you and gives you secret information to save the princess. You must choose what transportation you will use to save the princess.")

# Decision 2 - Choose your Transportation
        travel = ["Royal Starfighter"," Water Tunnels"," Kaadu Calvary"]
        print(1, travel[0])
        print(2, travel[1])
        print(3, travel[2])
        travel_pick = int(input("Select your transportation: 1: Royal Starfighter Select 2: Water Tunnels  Select 3: Kaadu Calvary")
        if   travel_pick ==1:
             print("You have Chosen the Starfighter and you have crashed and burned. You died")
             next_play= input("Do you want to play again? Type yes or no")
        elif travel_pick ==2:
             print("You have chosen to use the dense swamps and forest to save the princess. You encounter a Falumpaset and you have to make a choice.")

# Decision 3 - Choose what to do with the Falumpaset
            falumpaset = ["Kill the Falumpaset", "Make it your friend", "Ignore the Falumpaset"] 
            print(1, falumpaset[0])
            print(2, falumpaset[1])
            print(3, falumpaset[2])
            falumpaset_pick = int(input("Select your options:1: Kill the Falumpaset. Select 2: Make it your Friend. Select 3: Ignore the Falumpaset")
            if falumpaset_pick == 1:
                print ("You killed the Falumpaset. It fought back and left you severly injured you are now dead.")
                next_play=input("Do you want to play again?Type yes or no")
            elif falumpaset_pick == 2: 
                print("It looks like you made it your friend, you will be riding thru the dense swamps and forest to save the princess with your new friend.You see the castle.")  

# Decision 4 - Choose what to do at the Castle
                castle = ["Wait", "Retreat", "Proceed"]
                print(1, castle[0])
                print(2, castle[1])
                print(3, castle[2])
                castle_pick = int(input("Select your action: 1: Wait. Select 2: Retreat. Select 3 Proceed")
                if castle_pick ==1: 
                	print ("You waited to long and you died of hunger")
                    next_play= input("Do you want to play again? Type yes or no")
                elif castle_pick ==2:
                     print ("You are a coward!. You retreated and died.")
                     next_play = input("Do you want to play again? type yes or no")
                elif castle_pick ==3:
                     print("Wise choice to proceed. You see three doors to the castle. Which one do you choose?")

# Decision 5 - Choose a Door

                     Door=["Door 1", "Door 2", "Door 3"]
                     print(1, Door[0])
                     print(2, Door[1])
                     print(3, Door[2])
                     door_pick = int(input("Select your Door: 1, 2, or 3")
                     if door_pick ==1:
                         print ("You met Darth Vader and dualed you to the death with a lightsaver. You loose!")
                         next_play = input("Do you want to play again? type yes or no")
                     elif door_pick ==2:
                          print ("You saved the princess!", username,"she was behind this door! Good job!")
                     elif door_pick ==3:
                          print("You encountered Storm Troopers. You fought a terrific battle but died!")
                          next_play = input("Do you want to play again? Type yes or no")
                     else:
                       print("You ended the game.")
                       next_play = input("Do you want to play again? Type yes or no")


            
            elif falumpaset_pick == 3: 
                print("It looks like you chose to ignore the Falumpaset. You died by yourself")
                next_play=("Do you want to play again. Type yes or no")
            else: 
                print ("You ended the game.")
                next_play = input("Do you want to play again? Type yes or no")

        elif travel_pick ==3:
             print("You have chosen Kaadu Calvary and died.")
             next_play =("Do you want to play again? Type yes or no")
        else:
            print("You ended the game.")
            next_play = ( "Do you want to play again? Type yes or no")

    elif your_pick ==2:
        print(" It looks like you chose the trail to your left. ", username, "This rode leads you to the sea and when you tried to find food in the sea you are eaten by a Colo Claw fish and died.")
        next_play = input("Do you want to play again? Type yes or no")
    elif your_pick == 3:
        print ("It looks like you chose the trail in the Middle.",username, "You encounter a forest and a witch casts a spell and you are not able to move for a 1000 years. Game Ended")
        next_play = input("Do you want to play again? Type yes or no")
    else:
        print("You ended the game")
        next_play = input("Do you want to play again? Type yes or no")
        print("Thank for playing!")




   
           



