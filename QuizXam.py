# the json module to work with json files 
import json
import sqlite3
import tkinter
from tkinter import *
import random

# questions = [
#     "How many Keywords are there in C Programming language ?",
#     "Which of the following functions takes A console Input in Python ?",
#     "Which of the following is the capital of India ?",
#     "Which of The Following is must to Execute a Python Code ?",
#     "The Taj Mahal is located in  ?",
#     "The append Method adds value to the list at the  ?",
#     "Which of the following is not a costal city of india ?",
#     "Which of The following is executed in browser(client side) ?",
#     "Which of the following keyword is used to create a function in Python ?",
#     "To Declare a Global variable in python we use the keyword ?",
# ]

# answers_choice = [
#     ["23","32","33","43",],
#     ["get()","input()","gets()","scan()",],
#     ["Mumbai","Delhi","Chennai","Lucknow",],
#     ["TURBO C","Py Interpreter","Notepad","IDE",],
#     ["Patna","Delhi","Benaras","Agra",],
#     ["custom location","end","center","beginning",],
#     ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
#     ["perl","css","python","java",],
#     ["function","void","fun","def",],
#     ["all","var","let","global",],
# ] 

# load questions and answer choices from json file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answer choices
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]
global score
answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


# noinspection PyShadowingNames
def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))

    labelresulttext = Label(
        root,
        font=("Consolas", 10),
        background="#ffffff",
    )
    labelresulttext.pack()

    # Regestration button inserted

    img43 = PhotoImage(file="IR.png")

    btnReg = Button(
        root,
        image=img43,
        relief=FLAT,
        border=0,
        command=signUpPage,
    )





    btnReg.pack()

    if score >= 20:
        img = PhotoImage(file="great.png")

        labelimage.configure(image=img)

        labelimage.image = img

        labelresulttext.configure(text="You Are Excellent !!\nRegister to view your score :)")
        labelresulttext.configure(text="Register to view Your Score :) " + score)


    elif 10 <= score < 20:
        img = PhotoImage(file="ok.png")

        labelimage.configure(image=img)
        labelimage.image = img

        labelresulttext.configure(text="You Can Be Better !!\nRegister to view your score :)")
        labelresulttext.configure(text="Register to view Your Score :) " + score)

    else:
        img = PhotoImage(file="bad.png")

        labelimage.configure(image=img)
        labelimage.image = img

        labelresulttext.configure(text="You Should Work Hard !!\nRegister to view your score :) ")
        labelresulttext.configure(text="Register to view Your Score :) " + score)


def calc():
    # noinspection PyGlobalUndefined
    global indexes, user_answer, answers, score
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


# noinspection PyGlobalUndefined
def selected():
    # noinspection PyGlobalUndefined
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()


# noinspection PyGlobalUndefined
def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("QuizXam")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="QZ.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="QuizXam",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.place(relx=0.14, rely=0.8)
btnStart.pack()



# signup & login work


def loginPage(logdata):
    sup.destroy()
    # noinspection PyGlobalUndefined
    global login
    login = Tk()

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=440, bg="white")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Login", fg="black", bg="white")
    heading.config(font='calibre 40 bold')
    heading.place(relx=0.2, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username", fg='black', bg='white')
    ulabel.place(relx=0.21, rely=0.4)
    uname = Entry(login_frame, bg='black', fg='white', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password", fg='black', bg='white')
    plabel.place(relx=0.215, rely=0.5)
    pas = Entry(login_frame, bg='black', fg='white', textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.5)

    # SCORE
    slabel = Label(login_frame, text="Your Score is : ", fg='black', bg='white')
    slabel.config(font='calibre 20 bold')
    slabel.place(relx=0.14, rely=0.8)





    def check():
        for a, b, c, d in logdata:
            if b == uname.get() and c == pas.get():
                print("got you")


                dlabel = Label(login_frame, text=score, fg='black', bg='white')
                dlabel.config(font='calibre 20 bold')
                dlabel.place(relx=0.51, rely=0.8)



                break
            else:
                error = Label(login_frame, text="Wrong Username or Password!", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

    # LOGIN BUTTON
    log = Button(login_frame, text='VIEW MY SCORE', padx=5, pady=5, width=5, command=check)
    log.configure(width=15, height=1, activebackground="#33B5E5",bg = 'black',fg='white',relief=FLAT)
    log.place(relx=0.4, rely=0.6)
    #exit button
    out = Button(login_frame, text='EXIT',fg = 'red',bg='black', padx=5, pady=5, width=3, command=login.destroy)
    out.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT,font='calibre 10')
    out.place(relx=0.78, rely= 0.01)


    login.mainloop()


# noinspection PyGlobalUndefined
def signUpPage():
    root.destroy()
    global sup
    sup = Tk()

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    city = StringVar()

    sup_canvas = Canvas(sup, width=720, height=440, bg="white")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="white")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(sup_frame, text="SignUp", fg="black", bg="white")
    heading.config(font='calibre 40 bold')
    heading.place(relx=0.2, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="Full Name", fg='black', bg='white')
    flabel.place(relx=0.21, rely=0.4)
    fname = Entry(sup_frame, bg='black', fg='white', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Username", fg='black', bg='white')
    ulabel.place(relx=0.21, rely=0.5)
    user = Entry(sup_frame, bg='black', fg='white', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.31, rely=0.5)

    # password
    plabel = Label(sup_frame, text="Password", fg='black', bg='white')
    plabel.place(relx=0.215, rely=0.6)
    pas = Entry(sup_frame, bg='black', fg='white', textvariable=passW)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.6)

    # city
    clabel = Label(sup_frame, text="City", fg='black', bg='white')
    clabel.place(relx=0.215, rely=0.7)
    c = Entry(sup_frame, bg='black', fg='white', textvariable=city)
    c.config(width=42)
    c.place(relx=0.31, rely=0.7)

    def addUserToDataBase():
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        # noinspection PyShadowingNames
        city = c.get()

        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,CITY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)", (fullname, username, password, city))
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        #print(z)
        #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON
    sp = Button(sup_frame, text='SignUp', padx=5, pady=5, width=5, command=addUserToDataBase)
    sp.configure(width=15, height=1, activebackground="#33B5E5",bg='blue',relief=FLAT, fg='white')
    sp.place(relx=0.4, rely=0.8)

    log = Button(sup_frame, text='Already have a Account?', padx=5, pady=5, width=5, command=gotoLogin, bg="white")
    log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.9)

    sup.mainloop()

#Lower Rules
lblInstruction = Label(
    root,
    text="Read The Rules\nOnce You Are Ready Click Start !!",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 100))

lblRules = Label(
    root,
    text="This quiz contains 5 questions on any Random Topic\nYou will get 20 seconds\nOnce you select an option "
         "that will be a final\nSo think before you select",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="red",
)
lblRules.pack()

root.mainloop()



