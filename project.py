from tkinter import *
from PIL import Image,ImageTk
from random import randint

def reset():
    playerScore["text"] = '0'
    computerScore["text"] = '0'
    reset_button["text"]="reset"
    updateMessage("")
    enable_button()

def enable_button():
        rock['state']='normal'
        paper['state']='normal'
        scissor['state']='normal'
def disable_button():
        rock['state']='disable'
        paper['state']='disable'
        scissor['state']='disable'
        reset_button["text"]="Play again"
    
#update choices
def updateChoice(user_choice):

    #for user
    if user_choice=="rock":
        user_label.config(image = rock_img)
    elif user_choice=="paper":
        user_label.config(image = paper_img)
    else:
        user_label.config(image = scissor_img)

    #for computer
    l=["rock","paper","scissor"]
    comp_choice = l[randint(0,2)]
    if comp_choice=="rock":
        comp_label.config(image = rock_img)
    elif comp_choice=="paper":
        comp_label.config(image = paper_img)
    else:
        comp_label.config(image = scissor_img)

    CheckWin(user_choice,comp_choice)

#main window
root = Tk()
root.title("Rock paper scissor")
root.configure(background = "#9b59b6")

#images
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))

#indicators
user_indicator = Label(root,font=50,text="User",bg="#9b59b6")
comp_indicator = Label(root,font=50,text="computer",bg="#9b59b6")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#insert picture
user_label = Label(root,image=rock_img,bg="#9b59b6")
comp_label = Label(root,image=rock_img,bg="#9b59b6")
user_label.grid(row=1,column=4)
comp_label.grid(row=1,column=0)

#scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
playerScore.grid(row = 1, column = 3)
computerScore.grid(row = 1, column = 1)

#messages
msg = Label(root,font =50,bg="#9b59b6",fg="white")
msg.grid(row = 3, column = 2)

def updateMessage(x):
    msg['text'] = x

#update score
def updateUserScore():
    score = int(playerScore["text"])
    score+=1
    playerScore["text"] = str(score)
    if score==10:
        updateMessage("Congrats, You won the match!!")
        disable_button()

def updateCompScore():
    score = int(computerScore["text"])
    score+=1
    computerScore["text"] = str(score)
    if score==10:
        updateMessage("Oops!, better luck next time")
        disable_button()

def CheckWin(player,computer):
    if player == computer:
        updateMessage("Its a tie,``Your choice is same as Computer``")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose,~ Paper covers Rock ~")
            updateCompScore()
        else:
            updateMessage("<<< YOU WIN >>>")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose,~ Scissor cuts Paper ~")
            updateCompScore()
        else:
            updateMessage("<<< YOU WIN >>>")
            updateUserScore()
    else:
        if computer == "rock":
            updateMessage("You lose,~ Rock smashes Scissor ~")
            updateCompScore()
        else:
            updateMessage("<<<YOU WIN >>>")
            updateUserScore()
        
    
#button
rock = Button(root,width=20,height=2,text="Rock",bg="#FF3E4D",fg="white",command = lambda:updateChoice("rock"))
paper = Button(root,width=20,height=2,text="Paper",bg="#FAD02E",fg="white",command = lambda:updateChoice("paper"))
scissor = Button(root,width=20,height=2,text="Scissor",bg="#0ABDE3",fg="white",command = lambda:updateChoice("scissor"))
reset_button = Button(root,width=20,height=2,text="reset",bg="#0000FF",fg="white",command = reset)
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)
reset_button.grid(row=4, column=4)

root.mainloop()

