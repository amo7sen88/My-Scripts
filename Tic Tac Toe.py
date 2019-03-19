#!/usr/bin/env python
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# In[ ]:





# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('{}  |  {}  |  {}'.format(board[7],board[8],board[9]))
    print('{}   |  {}   |  {}'.format("","",""))
    print("-"*15)
    print('{}  |  {}  |  {}'.format(board[4],board[5],board[6]))
    print('{}   |  {}   |  {}'.format("","",""))
    print("-"*15)
    print('{}   |  {}   |  {}'.format("","",""))
    print('{}  |  {}  |  {}'.format(board[1],board[2],board[3]))


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[4]:


test_board = ['#','O','h','X','X',' ','X','y','X','X']
display_board(test_board)


# In[69]:


tboard = [" "]*10
display_board(tboard)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[2]:


def player_input():
    marker = ""
    while marker not in ("X","O"):
        print('Please select X or O')
        marker = input().upper()
    
    if marker == "X":
        return ("X", "O")
    elif marker == "O":
        return ("O","X")


# In[ ]:


player1,player2 = player_input()


# In[6]:


player1


# In[ ]:





# **TEST Step 2:** run the function to make sure it returns the desired output

# In[ ]:


player1_mark, player2_mark = player_input()


# In[15]:


player1_mark


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[ ]:


place_marker(test_board,'Hey',8)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[4]:


def win_check(board, mark):
    if ( board[1] == mark and board[2] == mark and board[3] == mark or
        board[4] == mark and board[5] == mark and board[6] == mark or
        board[7] == mark and board[8] == mark and board[9] == mark or

        board[1] == mark and board[4] == mark and board[5] == mark or
        board[2] == mark and board[5] == mark and board[8] == mark or
        board[3] == mark and board[6] == mark and board[9] == mark or

        board[1] == mark and board[5] == mark and board[9] == mark or
        board[3] == mark and board[5] == mark and board[7] == mark ):
        return True
    else:
        return False
        


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[ ]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[5]:


import random

def choose_first():
    first = random.randint(0,1)
    if first == 0:
        #print("player 1 start")
        return first
    elif first == 1:
        #print("player 2 start")
        return first
    


# In[66]:


print(choose_first())


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[6]:


def space_check(board, position):
    return board[position] == " "

    


# In[101]:


space_check(test_board, 6)


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[7]:


def full_board_check(board):
    check = False
    for i in range(1,10) :
        if board[i] == " ":
            check = False
            break

        else:
            check =  True
    return check


# In[29]:


full_board_check(test_board)


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[8]:


def player_choice(board):
    print("Please choose your next Position")
    position = int(input())
    return space_check(board,position)
    


# In[53]:


player_choice(test_board)


# In[54]:


position 


# In[49]:


position


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[9]:


def replay():
    print("Do you want to play again? Y or N")
    reply = str(input())
    return reply.upper() == "Y"


# In[2]:


replay()


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


prg = True
while prg:
    
    
    print("Welcome to the game")
    answer = input('Are you ready to play y or n: ')
    if answer.lower() == 'y':
        game = True
    else:
        game = False
        break
    player1, player2 = player_input()
    first = choose_first()
    board = [" "]*10
    while game:
        # player 1############################################################
        if first == "player 1":
            display_board(board)
            print('player 1 play')
            print(f"player {first}, Please choose Position from 1-9")
            position = player_choice(board)
            place_marker(board, player1, position)
            display_board(board)
                
            if full_board_check(board) == True:
                
                display_board(board)
                print("Game is Tie")
                game = False

            elif win_check(board,player1) == True:
                
                display_board(board)
                print(f' {first} wins')
                game = False

            else:
                first = "player 2"

        # player 2 ################################################################       
        elif first == "player 2":
            display_board(board)
            print('player 2 play')
            print(f"player {first}, Please choose Position from 1-9")
            position = position = player_choice(board)
            place_marker(board, player2, position)
            display_board(board)
                
            if full_board_check(board) == True:
                
                display_board(board)
                print("Game is Tie")
                game = False

            elif win_check(board,player2) == True:
                
                display_board(board)
                print(f' {first} wins')
                game = False

            else:
                first = "player 1"


# ## Good Job!
