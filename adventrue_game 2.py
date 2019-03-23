import time
from graphics import *

######################
    
def first_riddle():
    answer = 'teapot'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue

    return False
###############################################

def second_riddle():
    answer = 'coin'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue
    return False

############################################

def third_riddle():
    answer = 'word'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue
    return False

#############################################

def fourth_riddle():
    answer = 'echo'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue
    return False


#############################################

def fifth_riddle():
    answer = 'my name'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue
    return False
#################################################
def sixth_riddle():
    answer = 'moon'
    count = 0
    while count < 3:
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
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count} tries only")
            
            continue
    return False
##############################################
def exit_riddle():
    answer = ('footsteps','steps')
    count = 0
    while count < 3:
        print("\nExit Riddle: The more you take, the more you leave behind. What am I?\n")
        print("\n")
        print("\n")
        answer_user = input("\nPlease type your answer to sea if it is correct: ").lower()
        print("emm....")
        time.sleep(2)
        if answer_user in answer:
            return True
        else:
            count += 1
            print(f"\nSorry Monk, You have to Try harder. and you have now {3-count-1} tries only")
            
            continue
    return False
##############################################
def location (location):
    location = Line(Point(location[0],location[1]),Point(location[0]+10,location[1]))
    location.setArrow("first")
    location.setFill('green')
    location.draw(win)

##############################################
win = GraphWin("Hotel", 800,800)
win.setCoords(0.0,0.0,800.0,800.0)
base = Rectangle(Point(150,100),Point(650,750))
gate_entrance = Rectangle(Point(350,100),Point(450,125))
main_entrance = Text(Point(400,80),"Main Entrance")
main_entrance.setFill('red')


###Left Side

## Drawing the First Door and label
door1 = Rectangle(Point(150,175),Point(175,275))

door1_label = Text(Point(100,225),"Door 1")


## Drawing the Third Door and label
door3 = door1.clone()
door3.move(0,200)

door3_label = door1_label.clone()
door3_label.move(0,200)
door3_label.setText("Door 3")



## Drawing the Fifth door and label
door5 = door1.clone()
door5.move(0,400)

door5_label = door1_label.clone()
door5_label.move(0,400)
door5_label.setText("Door 5")


### Right Side

## Drawing the Second Door and label
door2 = Rectangle(Point(650,175),Point(625,275))

door2_label = Text(Point(700,225),"Door 2")


## Drawing the Fourth Door and label
door4 = door2.clone()
door4.move(0,200)

door4_label = door2_label.clone()
door4_label.move(0,200)
door4_label.setText("Door 4")



## Drawing the Sixth door and label
door6 = door2.clone()
door6.move(0,400)

door6_label = door2_label.clone()
door6_label.move(0,400)
door6_label.setText("Door 6")


## Exit Door

exit_door = gate_entrance.clone()
exit_door.move(0,650)

exit_label = main_entrance.clone()
exit_label.move(0,650)
exit_label.setText("Exit Door")

#### door Coordinates
door_1 = (150,225)
door_3 = (150,425)
door_5 = (150,625)
door_2 = (625,225)
door_4 = (625,425)
door_6 = (625,625)
last_door = (480,730)

#### Walls

wall1 = Rectangle(Point(150,325),Point(650,325))
wall1.setFill('black')

wall2 = wall1.clone()
wall2.move(0,200)
#############################################



#############################################
print("Welcome to the Adventure Game")
print("\n")
print("In This game you are going to be direction to several rooms in a hotel")
print("\n")
print("Behind every door is riddle you have to solve to escape.")
print("\n")
print("Here is the Hotel, You have to pass each level to go to the Other")

game = True
level= 0
inhotel = True
while game:
    game_ans = input("Are You Ready to Start Playing? y or n: ").lower()
    if game_ans == "n":
        game = False
        print("\n ***Thank You For Playing***")
        thanks = Text(Point(400,400),"***Thank You For Playing***")
        thanks.setFill("blue")
        thanks.setSize(20)
        thanks.draw(win)
        break
    elif game_ans == 'y':
        game = True
        level = 0
        win.close()
        win = GraphWin("Hotel", 800,800)
        win.setCoords(0.0,0.0,800.0,800.0)
        main_entrance.draw(win)
        gate_entrance.draw(win)
        base.draw(win)
        door1_label.draw(win)
        door1.draw(win)
        door3.draw(win)
        door3_label.draw(win)
        door5.draw(win)
        door5_label.draw(win)
        door2.draw(win)
        door2_label.draw(win)
        door4.draw(win)
        door4_label.draw(win)
        door6.draw(win)
        door6_label.draw(win)
        exit_door.draw(win)
        exit_label.draw(win)
        wall2.draw(win)
        wall1.draw(win)
        pass
    else:
        print("Wrong answer!!!!!\n")
        continue
    
#### Here we Start the logic
    
    while level < 4:
        direction = input(f"\nWelcome, You can see your position once you choose.Please Choose Left or Right: ").lower()
        level += 1
        if level > 4:
            break
        else:
            pass
        if direction not in ("left","right"):
            print("Sorry, Wrong Answer")
            continue
        else:
            pass

        
        while level == 1:
            if direction == 'left':
                location(door_1)
                firstone = first_riddle()
                if firstone:
                    door1.setFill("green")
                    print("Congrats, Lets take the other one")
                    location(door_2)
                    secondone = second_riddle()
                    if secondone:
                        level1 = False
                        print("Well, Thats was not a challenge lets step to the 2nd Stage")
                        door2.setFill('green')
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    level = 4
                    break
            elif direction == 'right':
                location(door_2)
                secondone = second_riddle()
                if secondone:
                    print("Well, Lets take the other one")
                    location(door_1)
                    door2.setFill('green')
                    firstone = first_riddle()
                    if firstone:
                        level1 = False
                        print("Congrats, lets step to the 2nd Stage")
                        door1.setFill('green')
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    level = 4
                    break
            
            
        while level == 2:
            if direction == 'left':
                location(door_3)
                thirdone = third_riddle()
                if thirdone:
                    door3.setFill("green")
                    print("Congrats, Lets take the other one")
                    location(door_4)
                    fourthone = fourth_riddle()
                    if fourthone:
                        print("Well, Thats was not a challenge lets step to the 3rd Stage")
                        door4.setFill('green')
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    break
            elif direction == 'right':
                location(door_4)
                fourthone = fourth_riddle()
                if fourthone:
                    print("Well, Lets take the other one")
                    location(door_3)
                    door4.setFill('green')
                    thirdone = third_riddle()
                    if thirdone:
                        print("Congrats, lets step to the 2nd Stage")
                        door3.setFill('green')
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                    
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    level = 4
                    break


        while level == 3:
            if direction == 'left':
                location(door_5)
                fifthone = fifth_riddle()
                if fifthone:
                    door5.setFill("green")
                    print("Congrats, Lets take the other one")
                    location(door_6)
                    sixthone = sixth_riddle()
                    if sixthone:
                        print("Well, You have immpressed me, Now You have to Unlock the Exit Door")
                        door6.setFill('green')
                        level +=1
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    level = 4
                    break
            elif direction == 'right':
                location(door_6)
                sixthone = sixth_riddle()
                if sixthone:
                    print("Well, Lets take the other one")
                    location(door_5)
                    door6.setFill('green')
                    fifthone = fifth_riddle()
                    if fifthone:
                        print("Well, You have immpressed me, Now You have to Unlock the Exit Door")
                        door5.setFill('green')
                        level +=1
                        break
                    else:
                        print("Sorry, You are Trapped here, You will never get out")
                        inhouse = False
                        level = 4
                        break
                    
                else:
                    print("Sorry, You are Trapped here, You will never get out")
                    inhouse = False
                    level = 4
                    break


        

    if level > 4:
        finalone = exit_riddle()
        location(last_door)
        if finalone:
            exit_door.setFill("green")
            base.setFill("green")
            print("You have Escaped the Hotel of Riddles, Congrats,")
        else:
            print("Sorry, You are Trapped here, You will never get out")
            inhouse = False
        break

   
