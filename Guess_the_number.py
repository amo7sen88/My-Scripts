import random
game = True
while game:
    user = input("\nPlease choose the end number you wish to select between 0 to your choice randomly: ")
    try:
        num = int(user)
        x = random.randint(0,num)
        user_choice = input("\nPlease enter your guesing number:  ")
        try:
            choice = int(user_choice)
            if choice > x and choice -x < 2:
                print("You were so Close")
                print(f"Your guess was: {choice}, and my Computer has Chosed {x}")

            elif x > choice and x-choice < 2:
                print("You were so Close")
                print(f"Your guess was: {choice}, and my Computer has Chosed {x}")

            elif x == choice:
                print(f"You are right, the number is {x}")
            else:
                print("You were so Far")
                print(f"Your guess was: {choice}, and my Computer has Chosed {x}")
     

            while True:
                replay = input("Do You Want To Play again?  y or n: ").lower()
                if  replay == 'y':
                    break
                else:
                    game = False
                    print("\nThank You For Playing")
                    break
            
        

        except ValueError:
            print("You have to enter an Integer")
            continue
    except ValueError:
            print("You have to enter an Integer")
            continue

