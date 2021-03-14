from tkinter import *

#Sets each field to false to begin with
Field = ['false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false']

xWins = 0
oWins = 0

#Each odd turn is player 1 and each even turn is player 2
PlayerTurn = 1

#For Darkmode
def DarkMode(isOn):

    count = 0

    #Changes tiles to dark mode and displays button to go in light mode
    if isOn == 1:
        root.configure(background = '#1E1E1E')

        darkMode = Button(root, text = 'Light Mode', width = 5, height = 5, command = lambda:DarkMode(0), background = '#1E1E1E', foreground = 'White')
        darkMode.pack()
        darkMode.place(height = 100, width = 100, x = 400, y = 100)

        while count < len(accessories):
            accessories[count].configure(background = '#1E1E1E', foreground = 'White')
            count += 1

    #Changes tiles to light mode and displays button to go in dark mode
    else:
        root.configure(background = 'SystemButtonFace')

        darkMode = Button(root, text = 'Dark Mode', width = 5, height = 5, command = lambda:DarkMode(1), background = 'SystemButtonFace', foreground = '#1E1E1E')
        darkMode.pack()
        darkMode.place(height = 100, width = 100, x = 400, y = 100)

        while count < len(accessories):
            accessories[count].configure(background = 'SystemButtonFace', foreground = '#1E1E1E')
            count += 1

#resets Field
def resetField():
    global PlayerTurn
    count = 0

    while count < 9:
        Field[count] = 'false'
        buttons[count].configure(text = '-', background = 'SystemButtonFace')
        count += 1

    PlayerTurn = 1

    accessories[0].configure(text = 'Player Xs Turn')

def resetScore():
    global xWins, oWins

    oWins = 0
    xWins = 0

    accessories[2].configure(text = 'X Wins: '+ '\n')
    accessories[3].configure(text = 'O Wins: '+ '\n')

#Changes the field to display as pressed
#Checks if draw or won
#Checks if legal move
#Calls reset function
def ChangeToPressed(number):
    global PlayerTurn, xWins, oWins

    #Checks to see if move is legal
    if ( Field[number] != 'false'):
        accessories[0].configure(text = 'ILLEGAL MOVE!\n Please try a\n different flied!')
        return

    #Sets it to X (Player 1) at odd turn and to O (Player 2) at even turn
    if (PlayerTurn % 2 == 1):
        Field[number] = 'X'
        buttons[number].configure(text = 'X', background = 'darkgrey', font=(50))
        accessories[0].configure(text = 'Player Os turn')

    else:
        Field[number] = 'O'
        buttons[number].configure(text = 'O', background = 'white', font=(50))
        accessories[0].configure(text = 'Player Xs turn')

    #Increments PlayerTurn (decides whos turn it is)
    PlayerTurn += 1

    #Function to check if someone won
    Won = CheckWin()

    #Checks if draw
    if (PlayerTurn == 10 and Won == 0):
        accessories[0].configure(text = 'Draw!\n Player Xs turn')
        resetField()
        return

    #If someone won, field gets reset
    if (Won > 0):

        #Checks who won
        if (Won == 1):
            print('X won')
            accessories[0].configure(text = 'Player X won!\n Player Xs turn!')
            xWins += 1
            accessories[2].configure(text = 'X Wins: ' + str(xWins) + '\n')
        else:
            print('O won')
            accessories[0].configure(text = 'Player O won!\n Player Xs turn!')
            oWins += 1
            accessories[3].configure(text = 'O Wins: ' + str(oWins) + '\n')

        #To reset Button text & color and Field
        resetField()

#checks who (if anyone) won
def CheckWin():
    if( (Field[6] == 'X' and Field[7] == 'X' and Field[8] == 'X') or #Unten gerade
        (Field[3] == 'X' and Field[4] == 'X' and Field[5] == 'X') or #Mitte gerade
        (Field[0] == 'X' and Field[1] == 'X' and Field[2] == 'X') or #Oben gerade
        (Field[0] == 'X' and Field[3] == 'X' and Field[6] == 'X') or #Links runter
        (Field[1] == 'X' and Field[4] == 'X' and Field[7] == 'X') or #Mitte runter
        (Field[2] == 'X' and Field[5] == 'X' and Field[8] == 'X') or #Rechts runter
        (Field[0] == 'X' and Field[4] == 'X' and Field[8] == 'X') or #Diagonal von links oben
        (Field[2] == 'X' and Field[4] == 'X' and Field[6] == 'X')):  #Diagonal von rechts oben
        return 1

    elif((Field[6] == 'O' and Field[7] == 'O' and Field[8] == 'O') or #Unten gerade
         (Field[3] == 'O' and Field[4] == 'O' and Field[5] == 'O') or #Mitte gerade
         (Field[0] == 'O' and Field[1] == 'O' and Field[2] == 'O') or #Oben gerade
         (Field[0] == 'O' and Field[3] == 'O' and Field[6] == 'O') or #Links runter
         (Field[1] == 'O' and Field[4] == 'O' and Field[7] == 'O') or #Mitte runter
         (Field[2] == 'O' and Field[5] == 'O' and Field[8] == 'O') or #Rechts runter
         (Field[0] == 'O' and Field[4] == 'O' and Field[8] == 'O') or #Diagonal von links oben
         (Field[2] == 'O' and Field[4] == 'O' and Field[6] == 'O')):  #Diagonal von rechts oben
        return 2

    else:
        return 0

root = Tk()
root.geometry("500x500")

#array for the buttons so text can be changed through accessing the array with the number of the button that was pressed
#E.g.: First button in array gets pressed, calls function with value 0 and function changes the text of the button in position
# 0 in the button arrray
buttons = []

#For settings buttons and labels
accessories = []
buttonCount = 0

#Initializes buttons to array
buttons.append(Button(text="-", command = lambda:ChangeToPressed(0)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(1)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(2)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(3)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(4)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(5)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(6)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(7)))
buttons.append(Button(text="-", command = lambda:ChangeToPressed(8)))

#While loop to pack buttons
while buttonCount < 9:
    buttons[buttonCount].pack()
    buttonCount += 1

#Places buttons in window
buttons[0].place(height=100, width=100, x = 0  , y = 0  )
buttons[1].place(height=100, width=100, x = 100, y = 0  )
buttons[2].place(height=100, width=100, x = 200, y = 0  )

buttons[3].place(height=100, width=100, x = 0  , y = 100)
buttons[4].place(height=100, width=100, x = 100, y = 100)
buttons[5].place(height=100, width=100, x = 200, y = 100)

buttons[6].place(height=100, width=100, x = 0  , y = 200)
buttons[7].place(height=100, width=100, x = 100, y = 200)
buttons[8].place(height=100, width=100, x = 200, y = 200)

#Labels to display information
#In order:
#Whos turn it is
#Reset button for field
#Wins for player X
#Wins for player O
#Reset button for score
accessories.append(Label (root, text = 'Player Xs turn'))
accessories.append(Button(root, text = 'Reset Field', width = 5, height = 5, command = lambda:resetField()))
accessories.append(Label (root, text = 'X Wins:\n'))
accessories.append(Label (root, text = 'O Wins:\n'))
accessories.append(Button(root, text = 'Reset Score', width = 5, height = 5, command = lambda:resetScore()))

accessories[0].place(height = 100, width = 100, x = 300, y = 0  )
accessories[1].pack()
accessories[1].place(height = 100, width = 100, x = 400, y = 0  )
accessories[2].place(height = 25 , width = 200, x = 0  , y = 310)
accessories[3].place(height = 25 , width = 200, x = 0  , y = 325)
accessories[4].pack()
accessories[4].place(height = 100, width = 100, x = 400, y = 300)

root.title("Tic Tac Toe")

photo = PhotoImage(file = "File.png")
root.iconphoto(False, photo)

DarkMode(1)

root.mainloop()