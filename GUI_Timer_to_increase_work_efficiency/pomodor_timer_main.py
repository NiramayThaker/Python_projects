import math
from tkinter import *

# TO get hex of color ->  https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 0.25
# SHORT_BREAK_MIN = 0.5
# LONG_BREAK_MIN = 0.20
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    work_time = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long break", fg=RED, font=(FONT_NAME, 45))
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="short break", fg=PINK, font=(FONT_NAME, 45))
    else:
        count_down(work_time)
        timer_label.config(text="Work Session", fg=GREEN, font=(FONT_NAME, 45))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:  # Using else as when count gets 0 it will stop so when it stop timer will start again
        start_timer()
        marks = ""
        for _ in range(0, math.floor(reps/2)):
            marks += "✔"
        tick_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore timer")  # Pomodore means tomato in italian
window.config(padx=150, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
timer_label.grid(column=2, row=0)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

tick_mark_label = Label(bg=YELLOW)
tick_mark_label.grid(column=2, row=4)

window.mainloop()
