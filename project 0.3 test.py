#game project 0.3
#Cameron Ulrich
#CMPT120
#9/27/16
#
#
#
#           W
#           |
#        C-Ch
#        |
#        G
#        |
#        D-R
#          |
#map:      Du

locations = ["You wake up in a cold, dark dungeon. The last thing you remembered was a big rock hurtling towards your head."
             "You get up and decide to take a look around. You see a light and what appears to be a rainforest in the distance.", #first loc
             "You find yourself now in a giant rainforest with a tiger approaching you. The rainforest is vast and dark. You become soaked with water because it is raining so hard.", #second loc
             "You come upon a looming desert. You look up to see nothing but sand. The sand is prevalent. Your skin becomes dry.", #third loc
             "You are now in a creepy graveyard. You see monsters awaking from the grave. They are hungry. For you.", #fourth loc
             "You come upon a giant crypt. You decide to open it and explore inside. Cobwebs are everywhere.", #fifth loc
             "You stumble upon a giant church. The church looks hundreds of years old and is deteriorating.", #sixth loc
             "A giant field is in front of you. A beautiful waterfall is spraying mist on your face. You've reached the Garden of Eden. Suddenly a demon appears and charges at you!"] #seventh loc #lists all of the locations in an array
             
isVisited = [False, False, False, False, False, False, False] #determines that all of the locations are not visited yet.

def map(): #function which stores the map as a string for when the user types in map they can see it. 
    map = ( "                  W\n"
"                  |\n"
"               C-Ch\n"
"               |\n"
"               G\n"
"               |\n"
"               D-R\n"
"                 |\n"
"                 Du\n")
    print(map)





def game(): #function that stores basic info 
    help = ("Type North, South, East, or West to choose which direction you want to go or type N,S,E, or W to choose your direction.\n"
            "Type any m or map to display the map.\nType points or the letter p to display your current score.\n") #if called helps the user know what to type"
    
    title = "Unexpected: The Game\n" #the title of the game that gets printed at the beginning of the game
    currentloc = locations[0] #sets the user's current location to Dungeon
    print(title) 
    name = input("What is your hero's name? ") #asks user for their name which will be used the whole game.
    copyright = "\nCopyright (c) 2016 Cameron K. Ulrich, cameron.ulrich1@marist.edu" #copyright
    print("Hello" , name,"!\n") #prints the user's name
    intro = name + (" began his days working on the farm. Just like any normal day. A normal, boring day. But that all changed when a man appeared at your door asking for money. He was dressed in a weird looking cloak." + " " + name + " " + "kindly refused and told him to leave. However, that answer wasn't good enough for the man."
                    "He waved his hands weirdly and then all of a sudden a giant rock appeared and came hurtling towards you. Black out") #sets story
    ending = name + " awakes in a cold sweat and realizes they had an awful dream. " + name + " needs to lay off the alcohol.\n" #sets ending to printed at the end of game
    print(intro) #prints intro
    score = 0 #score variable begins with zero

    print(locations[0]) #prints the first location which is dungeon
    #starts the loop
    if isVisited[0] == False: #checks if the location has been visited yet. If not... +5 points
        score += 5
        print ("+5 points! Your score right now is" , score)
    elif isVisited[0] == True: #if this place is already visited, don't add more points
        score += 0
        
    isVisited[0] = True #sets that the place has been visited so you don't get points if you visit it again
    while True: #starts direction loop
        
        chooseDir = input("Choose your direction\n") #asks user for another direction
        chooseDir = chooseDir.lower() #forces the string to all lower cases so if user types NORTH it still will be correct
        if (chooseDir == "north") or (chooseDir == "n"): #if the user types in north or any word that begins with the letter 'n' it checks the user's location and if they can actually go north or not.
            if (currentloc == locations[0]): #checks user's loc
                currentloc = locations[1] #sets user loc
                
                if isVisited[1] == False:
                    score += 5 #add five points if the user has not visited this area yet
                    print(locations[1])
                    isVisited[1] = True #the user has visited it now so it is set to true so they wont get any more points for coming back
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the rainforest.")
                
                
            elif (currentloc == locations[2]):
                
                currentloc = locations[3]
                if isVisited[3] == False:
                    score += 5
                    print(locations[3])
                    isVisited[3] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the graveyard")
                    
                
                
            elif (currentloc == locations[3]):
                
                currentloc = locations[4]
                if isVisited[4] == False:
                    score += 5
                    print(locations[4])
                    isVisited[4] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the crypt")
                    
                
            elif (currentloc == locations[5]):
                
                currentloc = locations[6]
                if isVisited[6] == False:
                    score += 5
                    print(locations[6])
                    isVisited[6] = True
                    print ("+5 points! Your score right now is" , score)
                    break
                else:
                    print("You've returned back to the waterfall")
                    
                              
               
                

            else:
                print("Sorry, you can't go that way. Enter another location.") #if the user cant go north where they are then it tells them to enter a new direction to go.
                    
                    

        if (chooseDir == "west") or (chooseDir == "w"): #if the user types in west or any word that begins with the letter 'w' it checks the user's location and if they can actually go west or not.
            if (currentloc == locations[1]):
                
                currentloc = locations[2]
                if isVisited[2] == False:
                    score += 5
                    print(locations[2])
                    isVisited[2] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the desert")
                    
                

            elif (currentloc == locations[5]):
                
                currentloc = locations[4]
                if isVisited[4] == False:
                    score += 5
                    isVisited[4] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the crypt")
                    
                
            else:
                print("Sorry, you can't go that way. Enter another location.")
                    

        if (chooseDir == "east") or (chooseDir == "e"): #if the user types in east or any word that begins with the letter 'e' it checks the user's location and if they can actually go east or not.
            if (currentloc == locations[2]):
                
                currentloc = locations[1]
                if isVisited[1] == False:
                    score += 5
                    isVisited[1] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the rainforest")

            
                    

            elif (currentloc == locations[4]):
                
                currentloc = locations[5]
                if isVisited[5] == False:
                    score += 5
                    print(locations[5])
                    isVisited[5] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the church")
                   
            else:
                print("Sorry, you can't go that way. Enter another location.")
                            

        if (chooseDir == "south") or (chooseDir == "s"): #if the user types in south or any word that begins with the letter 's' it checks the user's location and if they can actually go south or not.
            if (currentloc == locations[1]):
                
                currentloc = locations[0]
                if isVisited[0] == False:
                    score += 5
                    isVisited[0] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the dungeon")
                    
            
                
                

            
            elif (currentloc == locations[3]):
                
                currentloc = locations[2]
                if isVisited[2] == False:
                    score += 5
                    isVisited[2] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the desert")
                    
            
               
                

            elif (currentloc == locations[4]):
                
                currentloc = locations[3]
                if isVisited[3] == False:
                    score += 5
                    isVisited[3] = True
                    print ("+5 points! Your score right now is" , score)
                else:
                    print("You've returned back to the graveyard")
                    
            
                
                
            else:
                print("Sorry, you can't go that way. Enter another location.")

                           
                  
                
        elif (chooseDir == "quit") or (chooseDir == "q"): #if the user types quit or any word that begins with the letter 'q' it will quit the program
            quit()
        elif (chooseDir == "points") or (chooseDir == "p"): #if the user types points or any word that begins with the letter 'p' it will display the user's current points
            print("Your current score is:" , score)
            continue
        elif (chooseDir == "help") or (chooseDir == "h"): #if the user types help or any word that begins with the letter 'h' it will display what the user can type to move, quit, or check the points and map.
            print(help)
            continue
        elif (chooseDir == "map") or (chooseDir == "m") : #if the user types map or any word that begins with the letter 'm' it will display the map as a string by calling he function map()
            map()
            continue
        
            
    
    print("\nScore: " , score , "\n") #prints score
    

    print(ending) #prints ending message
    print(copyright) #prints copyright
game() #runs game
