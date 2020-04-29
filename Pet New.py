#bugs--------------------------------------------------------------------------
#
#
#
#------------------------------------------------------------------------------

import random
import time
#Global -----------------------------------------------------------------------

seed = random.randint(1,5)

debug = True

count = 0

#random no.
seed = random.randint(1,5)
rpoints = random.randint(10,20)
rgender = random.randint (1,5)
petrun = random.randint(1,4)
ractivities = random.randint(1,10)



#is the game running?
gameactive = True

#health 
pethealth = (100)

#hunger
hungry = (0)

#boredom
petboredom = (0)

#cleanliness
petdirty = (0)

#Xp points
petxp = (0)

#points that you earned (10 to 20pts every level)
points = (0)

nickname = "none"

pettype = "undefined"

petdraw = "undefined"

store = "undefined"

pethurt = False

#------------------------------------------------------------------------------

#loop--------------------------------------------------------------------------
while gameactive == True:
#slows the loop down
    time.sleep(0.5)
#number of days, and stuff
    count = count+1
#randomly generated point values
    rpoints = random.randint(10,20)
    random.randint(10,20)
    rxp = random.randint (1,5)
    random.randint(1,5)
    rhungry = random.randint(5,10)
    random.randint(5,10)
    rbored = random.randint(5,10)
    random.randint(5,10)
    rdirty = random.randint(5,10)
    random.randint(5,10)
    sick = random.randint(1,10)
    random.randint(1,10)
    random.randint(1,20)
    random.randint(1,100)
    petrun = random.randint(1,4)
    random.randint(1,4)
    ractivities = random.randint(1,10)
    random.randint(1,10)
#hunger
    hungry = hungry + rhungry
#boredom
    petboredom = petboredom + rbored
#dirtyness
    petdirty = petdirty + rdirty
#Xp
    petxp = petxp + petrun + 1
    
    points = points + 1
     
#is the pet injured?
    petinjured = False
    
    sickness = False
#------------------------------------------------------------------------------
  

    if hungry<0:
        hungry = 0
    if petboredom<0:
        petboredom = 0
    if petdirty<0:
        petdirty = 0

    

    if hungry>100:
        hungry = 100
    if petboredom>100:
        petboredom = 100
    if petdirty>100:
        petdirty = 100
        
    if petxp == 20:
        petxp = 0
        points = points + rpoints
        print("You gained", rpoints,"points!")
        
    if sick == 1:
        sickness = True
        
    if sickness == True:
        pethealth = pethealth - 5
        pethurt = True
        print("Your pet is sick!")
        
    if pethealth == 100:
        pethurt = False
    
#pet's type--------------------------------------------------------------------
    if seed == 1 or seed == 2:
        pettype = "Mouse"
    elif seed == 3 or seed == 4:
        pettype = "Cat"
    elif seed == 5:
        pettype = "Fish!"
#------------------------------------------------------------------------------
        
#pet's image-------------------------------------------------------------------
    if seed == 1 or seed == 2:
        petdraw = "<:3 )~~~~"
        
    elif seed == 3 or seed == 4:
        petdraw = "(=^o.o^=)__"
        
    elif seed == 5:
        petdraw = "<`)))><"
#------------------------------------------------------------------------------

#gender of your pet------------------------------------------------------------    
    if rgender == 1 or rgender == 2:
        gender = "Male"
    elif rgender == 3:
        gender = "Your pet wants to keep it as a secret ..."
    elif rgender == 4 or rgender == 5:
        gender = "Female"
#------------------------------------------------------------------------------
        
#print out the stats-----------------------------------------------------------
    print("Days:", count,"-----------------------------------------------------")
    print("Health:", pethealth)
    if pethurt == True:
        print(">>>>>>>>>>>>>>>>>>Oh no! Your pet is hurt!<<<<<<<<<<<<<<<<<<<<<<")
    if sick == 69:
        print(">>>>>>>>>>>>>>>Your pet is sick!<<<<<<<<<<<<<<<<<<<<<<")
        pethealth = pethealth - 5
    print("Hunger:", hungry)
    print("Boredness:", petboredom)
    print("Dirtiness:", petdirty)
    print("XP:", petxp)
    print("Points:", points)
    print("Pet type:", pettype)
    print("Gender:", gender)
    print("Pet's name:",nickname)
    print(petdraw)
    print("-------------------------------------------------------------")
#------------------------------------------------------------------------------
    
#asks what to do---------------------------------------------------------------
    humanin = input(""""What do you want to do?
(help for list of commands)
Answer here:""")
        
    if humanin == "feed" and hungry>5 or humanin == "feed" and hungry == 5:
        hungry = hungry - 25
        petxp = petxp + rxp
        points + 0.1
        print("That was delicious! Your pet gained", rxp,"Xp points!")
        
    elif humanin == "feed" and hungry<5:
        print("Your pet is full.")
        
    elif humanin == "play" and petboredom>5 or humanin == "play" and petboredom == 5:
        petboredom = petboredom - 25
        print("That was fun! Your pet gained", rxp,"Xp points!")
        petxp = petxp + 2
        points + 0.1
        
    elif humanin == "play" and petboredom<5:
        print("Your pet doesn't want to play.")
        
    elif humanin == "clean" and petdirty>5 or humanin == "clean" and petdirty == 5:
        petdirty = petdirty - 25
        print("That feels good! Your pet gained", rxp,"Xp points!")
        petxp = petxp + 2
        points + 0.1
        
    elif humanin == "clean" and petdirty<5:
        print("Your pet is already squeaky clean!")

    elif humanin == "nickname":
        nickname = (input("What would you like to name your pet?"))
        
    if hungry >= 100 or petdirty >= 100:
        pethealth = pethealth - 5
        pethurt = True
        
    if petboredom >= 100:
        print("Oh no! Your pet ran away!")
        if petrun == 1:
            print("Yes! You found your pet and they had alot of fun!")
            petboredom = 0
            
        if petrun >= 2:
            print("You searched everywhere, but you can't find your pet...")
            gameactive = False
            
    if humanin == "help":
        print("""
-------------------------------------------------------------
List of Commands
feed - feeds the pet (-15 from hunger)
play - plays with the pet (-15 from boredom)
clean - cleans the pet (-15 from dirtiness)
store - goes to the store
activities - you did something with your pet
-------------------------------------------------------------""")

    if humanin == "activities":
        if ractivities == 1:
            print("You went on a walk with your pet.")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 2:
            print("You went on vacation with your pet.")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 3:
            print("You dreamt of eating your pet...")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 4:
            print("You dreamt of cooking your pet...")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 5:
            print("Your pet had fun with other pets.")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 6:
            print("Your pet chased an old man in the park.")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 7:
            print("Your pet is chasing the fat man!!")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 8:
            print("You groomed your pet.")
            petxp = petxp + rxp + 5 
            print("Wow! you also gained", rxp + 5,"Xp points!")
        if ractivities == 9:
            print("Your pet found some points!")
            petxp = petxp + rxp + 5 
            points = points + 1
            print("Wow! you also gained", rxp + 5," Xp points!")
        if ractivities == 10:
            print("You did nothing...")
        
#------------------------------------------------------------------------------
        
#store-------------------------------------------------------------------------
    if humanin == "store":
        store = input("""What would you like to buy?
1) Snacks 10 points
2) Trainer 10 points
3) Maid 10 points
4) Medicine 20 points
5) Cancel
Type the number here:""")

        if store == "1" and points >= 10:
            points = points - 10
            hungry = 0
            print("Success! You bought snacks for you pet!")
        
        elif store == "2" and points >= 10:
            points = points - 10
            petboredom = 0
            print("Success! You hired a trainer to play with your pet!")
        
        elif store == "3" and points >= 10:
            points = points - 10
            petdirty = 0
            print("Success! You hired a maid to clean up your pet!!")
            
        elif store == "4" and points >= 20:
            points = points - 10
            pethealth = 100
            sickness = False
            print("Success! The medicine cured your pet back to health!")
        
        elif store == "5":
            print("You went back home.")
        
        else:
            print("Item not found...")
        
#------------------------------------------------------------------------------
        
#admin commands----------------------------------------------------------------
    if humanin == "admin":
        admin = input('What do you want to do? (Admin Commands)')
        if admin == "P":
            points = points + rpoints
            print("Added", rpoints, "points. Your points is:", points)
            print("Command Successful!")
        if admin == "XP":
            petxp = petxp + rpoints
            print("Added", rpoints, "Xp points. Your Xp is now:", petxp, "points.")
            print("Command Successful!")
        if admin == "Hurt":
            hungry = 95
            petboredom = 95
            petdirty = 95
            print("Command Successful!")
        if admin == "Die":
            petinjured = True
            print("Petinjured is:", petinjured)
        if admin == "Reset":
            pethealth = 100
            petboredom = 0
            petdirty = 0
            hungry = 0
            print("Reset complete.")
            
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
            
    elif humanin == "exit":
        gameactive = False
        
    if pethealth == 0:
        print("Your pet passed away, they lived for", count+1,"days.")
        gameactive = False
        
    if gameactive == False:
        print("Game over! Your pet lived for", count+1, "days, you earned", petxp,"Xp points and", points,"points.")
    

#-----------------------------------------------------------------------------
 