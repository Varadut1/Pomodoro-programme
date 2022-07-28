import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_init=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_listen():
    global i,w
    window.after_cancel(timer_init)
    canvas.itemconfig(timer, text='00:00')
    label1.config(text='Timer', fg=GREEN)
    label2.config(text='✔' * 0)
    i=1
    w=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_listen():
    global i, w
    if i%8==0:
        print(i)
        countdown(60)
        label1.config(text=f'Break', fg=RED)
    elif i%2:
        w+=1
        print(i)
        countdown(5)
        label1.config(text=f'Work', fg=GREEN)
    else:
        print(i)
        countdown(10)
        label1.config(text=f'Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
i=1
w=0
def countdown(count):
    global i
    global w
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        canvas.itemconfig(timer, text=f'{min}:0{sec}')
    else:
        canvas.itemconfig(timer, text=f'{min}:{sec}')

    if count>0:
        global timer_init
        timer_init = window.after(1000, countdown, count-1)
    else:
        label2.config(text='✔' * w)
        i+=1


    print("count", count)
    if count==0:
        print("its 0 and i: ", i)
        start_listen()


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title('Pomodoro')
window.minsize(500, 400)
window.config(padx=80, pady=80, bg=YELLOW)
canvas=Canvas(height=250, width=250, bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file='tomato.png')
canvas.create_image(125, 125,image=tomato)
timer=canvas.create_text(125, 140, text='00:00', font=(FONT_NAME, 24, "bold"), fill='white')
canvas.grid(row=2, column=2)
label1=Label(text='Timer', fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
label1.grid(row=1, column=2)
label2=Label(fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
label2.grid(row=4, column=2)
button1=Button(text='Start', command=start_listen)
button1.grid(row=3, column=1)
button2=Button(text='Reset', command=reset_listen)
button2.grid(row=3, column=3)

window.mainloop()
