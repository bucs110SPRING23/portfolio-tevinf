import random

num = random.randrange(1,11)

for _ in range(3): #this is how many times it will loop 
    guess = int(input("Guess a Number 1-10:" ))
    if guess != num: 
        if guess == num:
            print ("You got it!")
        elif guess < num:
            print("Too Low.")
        else:
            print("Too high.")

