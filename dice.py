from graphics import *
import random

def dice1 (x,y):
    d1 = Circle(Point(x+25,y+25),4)
    d1.setFill('black')
    d1.draw(win)
    
def dice2 (x,y):
    d1 = Circle(Point(x+10,y+10),4)
    d2 = Circle(Point(x+40,y+40),4)
    d1.setFill('black')
    d2.setFill('black')
    d1.draw(win)
    d2.draw(win)



def dice3(x,y):
    d1 = Circle(Point(x+10,y+10),4)
    d2 = Circle(Point(x+25,y+25),4)
    d3 = Circle(Point(x+40,y+40),4)
    d1.setFill('black')
    d2.setFill('black')
    d3.setFill('black')
    d1.draw(win)
    d2.draw(win)
    d3.draw(win)


def dice4(x,y):
    d1 = Circle(Point(x+10,y+10),4)
    d2 = Circle(Point(x+40,y+40),4)
    d3 = Circle(Point(x+40,y+10),4)
    d4 = Circle(Point(x+10,y+40),4)
    d1.setFill('black')
    d2.setFill('black')
    d3.setFill('black')
    d4.setFill('black')
    d1.draw(win)
    d2.draw(win)
    d3.draw(win)
    d4.draw(win)

def dice5(x,y):
    d1 = Circle(Point(x+10,y+10),4)
    d2 = Circle(Point(x+40,y+40),4)
    d3 = Circle(Point(x+40,y+10),4)
    d4 = Circle(Point(x+10,y+40),4)
    d5 = Circle(Point(x+25,y+25),4)
    d1.setFill('black')
    d2.setFill('black')
    d3.setFill('black')
    d4.setFill('black')
    d5.setFill('black')
    d1.draw(win)
    d2.draw(win)
    d3.draw(win)
    d4.draw(win)
    d5.draw(win)

def dice6(x,y):
    d1 = Circle(Point(x+10,y+10),4)
    d2 = Circle(Point(x+40,y+40),4)
    d3 = Circle(Point(x+40,y+10),4)
    d4 = Circle(Point(x+10,y+40),4)
    d5 = Circle(Point(x+25,y+10),4)
    d6 = Circle(Point(x+25,y+40),4)
    d1.setFill('black')
    d2.setFill('black')
    d3.setFill('black')
    d4.setFill('black')
    d5.setFill('black')
    d6.setFill('black')
    d1.draw(win)
    d2.draw(win)
    d3.draw(win)
    d4.draw(win)
    d5.draw(win)
    d6.draw(win)


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    

win = GraphWin("Dice",300,300)
win.setCoords(0,0,300.0,300.0)
game = True

while game:
    clear(win)
    dice_sqr1 = Rectangle(Point(100,100),Point(150,150))
    dice_sqr1.draw(win)
    dice_sqr2 = Rectangle(Point(170,100),Point(220,150))
    dice_sqr2.draw(win)

    x = random.randint(1,6)

    if x == 1:
        dice1(100,100)
        print(f"The Value of the first dice is {x}")
    elif x == 2:
        dice2(100,100)
        print(f"The Value of the first dice is {x}")
    elif x == 3:
        dice3(100,100)
        print(f"The Value of the first dice is {x}")
    elif x == 4:
        dice4(100,100)
        print(f"The Value of the first dice is {x}")
    elif x == 5:
        dice5(100,100)
        print(f"The Value of the first dice is {x}")
    elif x == 6:
        dice6(100,100)
        print(f"The Value of the first dice is {x}")

    y = random.randint(1,6)

    if y == 1:
        dice1(170,100)
        print(f"The Value of the Second dice is {y}")
    elif y == 2:
        dice2(170,100)
        print(f"The Value of the Second dice is {y}")
    elif y == 3:
        dice3(170,100)
        print(f"The Value of the Second dice is {y}")
    elif y == 4:
        dice4(170,100)
        print(f"The Value of the Second dice is {y}")
    elif y == 5:
        dice5(170,100)
        print(f"The Value of the Second dice is {y}")
    elif y == 6:
        dice6(170,100)
        print(f"The Value of the Second dice is {y}")

    while True:
        ex = input("Do you want to roll again y or n: ").lower()
        if ex == 'y':
            break
        elif ex =='n':
            print('Thank you for Playing')
            game = False
            break
        else:
            print("you have chosen wrong answer")
            continue
