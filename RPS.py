import random
options = ["rock", "paper", "scissors"]
computer = options[random.randint(0,2)] #this range includes the 2
countComputer = 0
countYou = 0 

for x in range(0,5,1):

        yourChoice = input("rock, paper or scissors? please write all lowercase same spelling. thank you")
        computer = options[random.randint(0,2)] #this range includes the 2
        if (computer == yourChoice):
            print("The computer also chose " + yourChoice + " it is a tie!")
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "paper") and (yourChoice == "rock"):
            print("computer chose " + computer + " you lose")
            countComputer +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "paper") and (yourChoice == "scissors"):
            print("computer chose " + computer + " you win")
            countYou +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "rock") and (yourChoice == "paper"):
            print("computer chose " + computer + " you win")
            countYou +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "rock") and (yourChoice == "scissors"):
            print("computer chose " + computer + " you lose")
            countComputer +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "scissors") and (yourChoice == "rock"):
            print("computer chose " + computer + " you win")
            countYou +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))
        elif (computer == "scissors") and (yourChoice == "paper"):
            print("computer chose " + computer + " you lose")
            countComputer +=1
            print("Your score is " + str(countYou) + " the computer's score is " + str(countComputer))

        if (countComputer == 3):
            print("Computer Wins!")
            break
        elif(countYou == 3):
            print(" You Win!")
            break
        elif(countComputer == countComputer) and (x == 4) : # 0 1 2 3 4 ... 5 games total
            print("Tie")
        elif(x ==4) and (countYou > countComputer):
            print("You Win!")
        elif(x == 4) and (countComputer > countYou):
            print("Computer Wins!")

        
        

        
