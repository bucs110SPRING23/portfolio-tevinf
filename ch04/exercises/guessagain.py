import random

num = random.randrange(1,1001)

guessamount = ()

for _ in range(guessamount): #this is how many times it will loop 
    guess = int(input("Guess a Number 1-10:" ))
    if guess != num: 
        if guess == num:
            print ("You got it!")
        elif guess < num:
            print("Too Low.")
        else:
            print("Too high.")

for i in guessamount: 
    while guessamount == True: 
        guessamount[0] = 1 
    if guess == num: 
        print(guessamount) 