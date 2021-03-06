#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bank account for player and computer class
class Wallet():
    
    def __init__(self,credit=0):
      
        self.credit = credit
             
    def add_to(self,amount):
        self.credit += amount
        return self.credit
    
    def take_from(self,amount):
        self.credit -= amount
        return self.credit
    
    def __int__(self):
        return (self.credit)
    


# In[2]:


def displayboard(list1,list2):
    clear_output()
    print(f'     Computer Hand {list1}   {sum(list1)}') 
    print("\n"*4)
    print(f'     Player Hand {list2}   {sum(list2)}')
    
    


# In[3]:


# Player Board and the deck
import random
card_list = ['1B ','2B','3B','4B','5B','6B','7B','8B','9B','10B','KB','QB','JB',                 '1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','KH','QH','JH',                 '1R','2R','3R','4R','5R','6R','7R','8R','9R','10R','KR','QR','JR',                 '1T','2T','3T','4T','5T','6T','7T','8T','9T','10T','KT','QT','JT']
def table_board(deck):
    random.shuffle(deck)
    return deck
    


# In[4]:


def win_game(list1,list2):
    if sum(list1) <= 21 and len(list1) > 2 and max(sum(list1),sum(list2)) == sum(list1):
        return list1
    elif sum(list1) <= 21 and len(list1) > 2 and max(sum(list1),sum(list2)) == sum(list2):
        return list2
    else:
        pass
    


# In[5]:


class Bust():
    
    def __init__ (self,on_hand):
        self.on_hand = on_hand
    
    def check (self):
        if sum(self.on_hand) > 21:
            return True
        else:
            return False


# Full Code i think :)

# In[ ]:


import random
from IPython.display import clear_output
print("Welcome to Black Jack")
card_list = ['1B ','2B','3B','4B','5B','6B','7B','8B','9B','10B','KB','QB','JB',                 '1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','KH','QH','JH',                 '1R','2R','3R','4R','5R','6R','7R','8R','9R','10R','KR','QR','JR',                 '1T','2T','3T','4T','5T','6T','7T','8T','9T','10T','KT','QT','JT']
game = True
camount = Wallet()
pamount = Wallet(int(input("Please enter your Account Balance: ")))
pbalance = pamount.add_to(0)
cbalance = pamount.add_to(0)
playerhand = []
computerhand = []
turn = True


# shuffle the deck
deck = table_board(card_list)
displayboard(computerhand,playerhand)
# asking player to raise 
while True:
    betting = int(input('Please Enter your bet: '))
    if betting > pbalance:
        continue
    else:
        pbalance = pamount.take_from(betting)
        break

while game:
    displayboard(computerhand,playerhand)
    print("You have placed a bet of: {} \nYour Balance is: {}".format(betting,pbalance.__int__()))
    print("\n"*2)

    # Player Card Distribution
    # Player Card
    card_list = table_board(card_list)
    for i in range (0,2,1):
        x = card_list.pop()
        if len(x)>2:
            x = [int(x[0])]
            playerhand.append(x[0])
            displayboard(computerhand,playerhand)
        elif "K" in x or "Q" in x or "J" in x:
            x = 10
            playerhand.append(x)
            displayboard(computerhand,playerhand)
        elif x ==1:
            x = int(input("what do you want for the value of Ace 1 or 11: "))
            playerhand.append(x)
            displayboard(computerhand,playerhand)
        else:
            x = int(x[0])
            playerhand.append(x)
            displayboard(computerhand,playerhand)

    # Computer Card Distribution
    # Computer Card       
    for i in range (0,2,1):
        x = card_list.pop()
        if len(x)>2:
            x = [int(x[0])]
            computerhand.append(x[0])
            displayboard(computerhand,playerhand)

        elif "K" in x or "Q" in x or "J" in x:
            x = 10
            computerhand.append(x)
            displayboard(computerhand,playerhand)

        elif x ==1:
            x = random.choice([1,11])
            computerhand.append(x)
            displayboard(computerhand,playerhand)

        else:
            x = int(x[0])
            computerhand.append(x)
            displayboard(computerhand,playerhand)

    ###############################################################################
    # asking the player to hit and pop from the list
    while turn:
        hit = input('Do you want to Hit??')
        if hit.lower() != 'y':
            winner = win_game(computerhand,playerhand)
            if winner == computerhand:
                print('Computer Wins')
                game = False
            elif winner == playerhand:
                print('Player Wins')
                game = False
            else:
                turn = False
        else:
            x = card_list.pop()
            if len(x)>2:
                x = [int(x[0])]
                playerhand.append(x[0])
                displayboard(computerhand,playerhand)
            elif "K" in x or "Q" in x or "J" in x:
                x = 10
                playerhand.append(x)
                displayboard(computerhand,playerhand)
            elif x ==1:
                x = int(input("what do you want for the value of Ace 1 or 10: "))
                playerhand.append(x[0])
                displayboard(computerhand,playerhand)
            else:
                x = int(x[0])
                playerhand.append(x)
                displayboard(computerhand,playerhand)

        if Bust(playerhand)== True:

            cbalance = pamount.add_to(betting)
            displayboard(computerhand,playerhand)
            print('Computer Wins')
            game = False

        else:
            turn = False
            break

    #computer Turn


    while not turn:
        x = card_list.pop()
        if len(x)>2:
            x = [int(x[0])]
            computerhand.append(x[0])
            displayboard(computerhand,playerhand)
            winner = win_game(computerhand,playerhand)
            if winner == computerhand:
                print('Computer Wins')
                game = False
            elif winner == playerhand:
                print('Player Wins')
                game = False
            else:
                turn = False
        elif "K" in x or "Q" in x or "J" in x:
            x = 10
            computerhand.append(x)
            displayboard(computerhand,playerhand)
            winner = win_game(computerhand,playerhand)
            if winner == computerhand:
                print('Computer Wins')
                game = False
            elif winner == playerhand:
                print('Player Wins')
                game = False
            else:
                turn = False
        elif x ==1:
            x = random.choice([1,11])
            computerhand.append(x)
            displayboard(computerhand,playerhand)
            winner = win_game(computerhand,playerhand)
            if winner == computerhand:
                print('Computer Wins')
                game = False
            elif winner == playerhand:
                print('Player Wins')
                game = False
            else:
                turn = False
        else:
            x = [int(x[0])]
            computerhand.append(x)
            displayboard(computerhand,playerhand)
            winner = win_game(computerhand,playerhand)
            if winner == computerhand:
                print('Computer Wins')
                game = False
            elif winner == playerhand:
                print('Player Wins')
                game = False
            else:
                turn = False

        if Bust(computerhand)== True:

            pbalance = pamount.add_to(betting)
            displayboard(computerhand,playerhand)
            print('Computer Wins')
            game = False

        else:
            turn = False
            break
            
            
            






