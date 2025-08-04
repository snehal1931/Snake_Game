
import random
Dict = {"1":1, "2":-1, "3": 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun" }

# """snake => 1
# water => -1
# gun => 0"""

print("-----------------Welcome to Snake-Water-Gun Game-----------------")
while True:
    computer = random.choice([-1,0,1])
    user_str = input("\t1.Snake\n\t2.Water\n\t3.Gun\nEnter your choice among above options: ")

    user = Dict[user_str]
    print(f"\n\tYou chose {reverseDict[user]}\n\tComputer chose {reverseDict[computer]}")
    if (computer == user):
         print("\n\t It's a DRAW")
    else:
        if(computer == -1 and user == 1):
             print("\n\tYou WIN!")
        elif(computer == -1 and user == 0):
            print("\n\tYou Lose!")
        elif(computer == 1 and user == -1):
            print("\n\tYou Lose!")
        elif( computer == 1 and user == 0):
            print("\n\tYou WIN!")
        elif( computer == 0 and user == -1):
             print("\n\tYou WIN!")
        elif( computer == 0 and user == 1):
             print("\n\tYou Lose!")
        else:
             print("\n\tSomething went Wrong. Please try again!")
        
    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again != "Yes" or "yes" or "YES":
         print("Thanks for playing! Goodbye!")
         break 
     
            

    
