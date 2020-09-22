#!/usr/bin/env python3

try:
    round=1
    points=0
    userInput=input("Who is the main actor in Mad Max: ").lower()

    if userInput == 'mel gibson':
    
        points += 10
        round +=1
        print("Correct! You won :"+ points +"points")
        userInput == input("Who is the actor in Iron Man? ").lower() # user prompt for another question answer
        
        if userInput== 'robert downey jr':
            print("Correct Answer")
            points +=10
            round +=1
        
            userInput == input('Who is the actor in Captain America? ') # user prompt to answer question
            
            if userInput == 'chris evans':
            
                points +=10
                round +=1
                print("Correct Answer! You have won:"+ points +"points")
            else:
                print(" wrong answer! You have won"+points)
            

        else:
            print("Wrong Answer! You have won"+ points)
            
    else: # ensure that round has not reached to 3
        points +=0
        print("You have answered wrong. You won:"+ points+"points")
        
except:
    print("You have invalid/incorrect answer")
