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

    #define roll_again
    roll_again = "yes"

#    while roll_again == 'yes':
#        if roll_again == "yes" or roll_again == "y":
#            randomnumber0 = random.randint(min, max)
#            print ("Rolling the dice...")
#            print ("The value is...")
#            print (randomnumber0
                

#If user wants to roll the dice more than once. 
    while roll_again == "yes":
        print(roll_again)
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

    print("you cant use 2 libraries which are at 2 different version\n it's badly written\n pip is cancer on linux \n no switch case\n it cant hold enough info\n python is slow\n python takes all youre memory\n python is bad with databases\n errors goes to run time instead of compile time\n you can only get a job with python in india\n simon thinks python is not a simple program and the syntax is not simple\n it's quote on quote easy to code\n no templates\n python er skrald\n python is hard to read\n missing features\n documentation is not very good")
    
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
