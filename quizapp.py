import requests
import random2 as random
from tkinter import *

#  fetching API : 
response = requests.get(url = "https://opentdb.com/api.php?amount=14&category=18&difficulty=easy&type=boolean")
question_data = response.json()
choosen_question = random.randint(0, 13)
Q = question_data["results"][choosen_question]["question"].replace("&quot;" , "'")
rightAns =question_data["results"][choosen_question]["correct_answer"]
score = 0

# Regenetation of Questions 
def regenerate():
    global rightAns
    global Q
    choosen_question = random.randint(0, 13)
    Q = question_data["results"][choosen_question]["question"].replace("&quot;" , "'")
    window.config(bg = "white")
    label.config(text = f"{Q}" , bg = "white")
    scoreLabel.config(bg= "white")
    rightAns =question_data["results"][choosen_question]["correct_answer"]

# On clicking true button
def pressTrue():
    if rightAns == "True":
        global score
        score +=1
        scoreLabel.config(text = f"Score : {score}" , bg = "#ACE1AF")
        window.config(bg = "#ACE1AF")
        label.config(bg = "#ACE1AF")      
        regenerate()
    else:
        window.config(bg = "pink")
        label.config(bg = "pink")
        scoreLabel.config(bg = "pink")

# On clicking false button
def pressFalse():
    if rightAns == "False":
        global score
        score+=1
        scoreLabel.config(text = f"Score : {score}" , bg = "#ACE1AF")
        window.config(bg = "#ACE1AF")
        label.config(bg = "#ACE1AF")
        regenerate()
    else:
        window.config(bg = "pink")
        label.config(bg = "pink")
        scoreLabel.config(bg = 'pink')

#  Creating an tkinter window
window  = Tk()
window.title("Random Quote")
window.minsize(height = 300 , width = 500)
#  Score 
scoreLabel = Label(text = f"score : {score}")
scoreLabel.pack(padx = 50)
#  Question
label  = Label(text = f"{Q}", fg = "black" , font = ('Arial' , 15 , "bold"))
label.config(wraplength= 500 , justify = 'center')
label.pack(pady = 50 ,padx = 15)
# True and false button
true_button = Button(text = "True" , width = 20, bg = "green", fg ="white" , font = ('Arial' , 10 , "bold") ,command = pressTrue)
true_button.pack(pady = 5)
false_button = Button(text = "False" , width = 20, bg = "red", fg ="white", font = ('Arial' , 10 , "bold"), command = pressFalse)
false_button.pack(pady = 5)

window.mainloop()
