import random #dice
import sys    #for exit()

#Functions
def destination():
    desti = input("Hello, please select your wanted destination: ")
    #try and reset the input that the user gives so desti isnt always dice and wont be stuck in a loop
    if desti in ("help"):
       help() 
       UserInp()  
              
    elif desti in ("dice"):
        dicefunction()


    elif desti in ("russki"):
   
        russki()

    elif desti in ("language"):

        print("this is gonna take a while.")

    elif desti in ("simon's list", "simons list", "slist"):
   
        sList()
   
    else:
        print("Invalid path.")
        destination()

def dicefunction():
    dicex = ["You rolled a one twice in a row!","You rolled a two twice in a row!", "You rolled a three twice in a row!", "You rolled a four twice in a row!", "You rolled a five twice in a row!", "You rolled a six twice in a row!"]
    def diceArr(): #this could just be a for loop
        if randomnumber0 == 1:
            print(dicex[0])
    
        elif randomnumber0 == 2:
            print(dicex[1])
   
        elif randomnumber0 == 3:
            print(dicex[2])
   
        elif randomnumber0 == 4:
            print(dicex[3])
    
        elif randomnumber0 == 5:
            print(dicex[4])
                
        elif randomnumber0 == 6:
            print(dicex[5])
        
    min = 1
    max = 6
    roll_again = "yes"

    while roll_again == "yes":
        roll_again = input("Do you want to roll the dice? ")
        if roll_again in ("yes", "y"):
            randomnumber0 = random.randint(min, max)
            print ("Rolling the dice...")
            print ("The value is...")
            print (randomnumber0)
            diceArr()
            
        elif roll_again in ("no", "n"):
            print("Have a good day. \n")
            destination()

        else:
            print("invalid input")
            roll_again = "yes" #bad fix

def sList(): 

    print("")
    
def Russki():
    print("why you talk to me men")
    exit()

def help(): #Make it so this is in alphabetic order. Call "destination" when thats made
    
    print("These commands can be case sensetive.\nCurrent commands are as follows: \n--Help\n--Russki\n--sList\n--Language\n--Dice\n")
    
def lang():
    
    exit()

def UserInp():
    
    destination()
    
while UserInp() == True: #idk how this works but it does
    UserInp()
