import random
'''
 1 for rock
-1 for paper
0 for scissors

'''
computer = random.choice([-1,1,0])
youstr = { "rock": 1 , "paper": -1 , "scissors": 0 }
rdict = { 1 : "Rock",-1 : "Paper",0 : "Scissors"}

print("YOUR CHOICE!") 
yourin = input("-")
y = yourin.lower()


yourchoice = (youstr[y])
 
print(f"You choosed {rdict[yourchoice]} \nComputer choosed {rdict[computer]}")

if(computer == yourchoice):
    print("Its a draw!")
else:
    if(computer == 1 and yourchoice == -1): 
        print("You Win!")
    elif(computer == 1 and yourchoice == 0): 
        print("You loose!")
    elif(computer == -1 and yourchoice == 1):
        print("You loose!")
    elif(computer == -1 and yourchoice == 0): 
        print("You Win!")
    elif(computer == 0 and yourchoice == -1): 
        print("You loose!")
    elif(computer == 0 and yourchoice == 1): 
        print("You Win!")
    else:
        print("Enter one of Rock,Paper,Scissors")
    
 
