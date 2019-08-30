import random #dice
import sys    #for exit()

#Functions
def destination():
    desti = input("")
    #try and reset the input that the user gives so desti isnt always dice and wont be stuck in a loop
    if desti in ("help", "Help"):
       help() 
       UserInp()  
              
    elif desti in ("Dice", "dice"):
        dicefunction()
        print("dice stuff here")

    elif desti in ("russki", "Russki", "Russian"):
   
       russki()

    elif desti in ("language", "Language"):

       print("this is gonna take a while.")

    elif desti in ("Simon's list", "simon's list", "Simons list", "simons list", "slist"):
   
       sList()
   
    else:
        print("Goodbye then.")
        exit()

def dicefunction():
    dicex = ["You rolled a one twice in a row!","You rolled a two twice in a row!", "You rolled a three twice in a row!", "You rolled a four twice in a row!", "You rolled a five twice in a row!", "You rolled a six twice in a row!"]
    min = 1
    max = 6

    #define roll_again & roll_again2
    roll_again = "yes"
    roll_again2 = "yes"

    if roll_again == "yes" or roll_again == "y":
        randomnumber0 = random.randint(min, max)
        print ("Rolling the dice...")
        print ("The value is...")
        print (randomnumber0)
                

#If user wants to roll the dice more than once. 
    y = input("Do you want to roll the dice? ")
    if y in ("yes", "y", "Yes", "Y"):
        
        roll_again2 = "yes" 
        
    elif y in ("no", "n", "No", "N"):
    
        print("Have a good day.")
        exit()
         

    if roll_again2 == "yes" or roll_again2 == "y":
        randomnumber2 = random.randint(min,max)
        print ("Rolling the dice...")
        print ("The value is...")
        print (randomnumber2)
        
       #Dice if statements
    if randomnumber0 == randomnumber2 and randomnumber0 == 1:
   
        print(dicex[0])
    
    elif randomnumber0 == randomnumber2 and randomnumber0 == 2:
   
        print(dicex[1])
   
    elif randomnumber0 == randomnumber2 and randomnumber0 == 3:
   
        print(dicex[2])
   
    elif randomnumber0 == randomnumber2 and randomnumber0 == 4:
   
        print(dicex[3])
  
    elif randomnumber0 == randomnumber2 and randomnumber0 == 5:
   
        print(dicex[4])
            
    elif randomnumber0 == randomnumber2 and randomnumber == 6:
   
        print(dicex[5])

   
    print("") 
    print("")
    print("")
    print("Have a good day.")

def sList(): 
    
    print("you cant use 2 libraries which are at 2 different version\n it's badly written\n pip is cancer on linux \n no switch case\n it cant hold enough info\n python is slow\n python takes all youre memory\n python is bad with databases\n errors goes to run time instead of compile time\n you can only get a job with python in india\n simon thinks python is not a simple program and the syntax is not simple\n it's quote on quote easy to code\n no templates\n python er skrald\n python is hard to read\n missing features\n documentation is not very good")
    
def Russki():
    print("why you talk to me men")
    exit()

def help(): #Make it so this is in alphabetic order. Call "destination" when thats made
    
    print("These commands can be case sensetive.\nCurrent commands are as follows: \nHelp\nRusski\nsList\nLanguage\nDice")
    
def lang():
    
    exit()

def UserInp():
    desti = ("Hello, please select your wanted destination: ")
    print(desti)
    destination()
    
#This is the beginning of the code
UserInp()