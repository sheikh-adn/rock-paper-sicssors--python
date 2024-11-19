import random
'''
 1 for rock
-1 for paper
0 for siccors

'''
computer = random.choice([-1,1,0])
youstr = { "rock": 1 , "paper": -1 , "siccors": 0 }
rdict = { 1 : "Rock",-1 : "Paper",0 : "Siccors"}

print("YOUR CHOICE!") 
yourin = input("-")
y = yourin.lower()
yourchoice = (youstr[y])
print(f"You choosed {rdict[yourchoice]} \nComputer choosed {rdict[computer]}")

if(computer == yourchoice):
    print("Its a draw!")

 
    
elif((yourchoice - computer) == 2 or (yourchoice - computer) == -1):
    print("You loose!")
else:
        print("You win!")

