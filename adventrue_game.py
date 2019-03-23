import time
def first_floor():
    print("This floor consists of three doors that contains 3 riddles")


def first_riddle():
    answer = 'teapot'
    count = 0
    while count <= 3:
        print("\nFirst1#: What beging with 'T', ends with 'T', and has 'T' in it?\n")
        print("\n")
        
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(3)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue

    return False
###############################################

def second_riddle():
    answer = 'coin'
    count = 0
    while count <= 3:
        print("\nSecond2#:What has a head and a tail but no body?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(3)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False

############################################

def third_riddle():
    answer = 'word'
    count = 0
    while count <= 3:
        print("\nThird3#:You can keep it, even if you gave it to someone?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(3)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False

#############################################

def fourth_riddle():
    answer = 'echo'
    count = 0
    while count <= 3:
        print("\nFourth4#: cannot talk to,but he will always reply when speak to?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(2)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False


#############################################

def fifth_riddle():
    answer = 'my name'
    count = 0
    while count <= 3:
        print("\nFifth5#: It belongs to you, but other people use it more than you do. What is it?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(2)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False
#################################################
def sixth_riddle():
    answer = 'moon'
    count = 0
    while count <= 3:
        print("\nSixth6#: It’s been around for millions of years, but is never more than a month old. What is it?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(2)
        if answer == answer_user:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False




#############################################
print("Welcome to the Adventure Game")
print("\n")
print("In This game you are going to be introudced to several riddles in a hotel rooms")
print("There are two floors, floor one is simple riddles, floor 2 is more advanced")
print("\n")
print("You have to Listen read carefully to solve them.")
print("as it may lead you to treassure or death!, \n Good Luck")
game = True
turn = 0
inhotel = True
while game:
    game_input = input("Do You Want to Play? y or n: ").lower()
    if game_input != 'n' and game_input != 'y':
        print("please choose y or n only")
        continue

    elif game_input == 'n':
        print("\n ***Thank You for Playing***")
        game = False
        break
    else:
        game = True
        turn = 0
        inhotel = True

    print("\nYou have to solve all the six riddles to win the treassure, or you will be dead")
    print("\nbut you can choose the floor start whether it's the first of the 2nd floor")
    floor_choice = input("Please choose the floor with 1 or 2: ")
    if floor_choice == "1" or floor_choice == "2":
        pass
    else:
        print("You have chosen wrong floor number")
        continue

    while inhotel:
        try:
            floor_choice_user = int(floor_choice)
            while turn <= 2:
                if floor_choice_user == 1:
                    first_floor()
                    firstone = first_riddle()
                    if firstone:
                        print("Well Done, We are going to the next one")
                        secondone = second_riddle()
                        if secondone:
                            print("Well Done, We are going to the next one")
                            thirdone = third_riddle()
                            if thirdone:
                                
                                floor_choice = 2
                                turn += 1
                                
                                if turn == 2:
                                    print("Amazing, you wealth is your knowledge and intellegence :D")
                                    inhotel = False
                                    break
                                else:
                                    print("Well Done, We are going to the Second Floor")
                                    break
                            else:
                                print("\nSorry pal, You are doomed")
                                inhotel = False
                                break
                        else:
                            print("\nSorry pal, You are doomed")
                            inhotel = False
                            break
                    else:
                        print("\nSorry pal, You are doomed")
                        inhotel = False
                        break

                elif floor_choice_user == 2:
                    fourthone = fourth_riddle()
                    if fourthone:
                        print("Well Done, We are going to the fifth one")
                        fifthone = fifth_riddle()
                        if fifthone:
                            print("Amazing, the NEXT!!")
                            sixthone = sixth_riddle()
                            if sixthone:
                                print("Amazing,D")
                                turn += 1
                                floor_choice =1
                                
                                if turn == 2:
                                        print("Your wealth is your knowledge and intellegence :D")
                                        inhotel = False
                                        break
                                else:
                                    
                                    break
                            else:
                                print("\nSorry pal,although you have reached here so far but you are doomed!!!!")
                                inhotel = False
                                break
                        else:
                            print("\nSorry pal,although you have reached here so far but you are doomed!!!!")
                            inhotel = False
                            break
                    else:
                        print("\nSorry pal, You are doomed")
                        inhotel = False
                        break
        except ValueError:
            print("Please Choose again the floor Number between 1 or 2")
            continue
