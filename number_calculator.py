import random
secret = random.randint(1,20)
attempt=0
MAX_ATTEMPTS=5
while attempt <= MAX_ATTEMPTS:
    num = int(input("Enter a guess number between 1 to 20"))
    if num == secret:
        print("Correct Guess")
        break
    elif num > secret:
        print("Too High")
        attempt+=1
        
    else:
        print("Too Low")
        attempt+=1
            