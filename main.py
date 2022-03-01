import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def click_reset():
    global check
    global reps
    reps = 0
    check = ""
    window.after_cancel(timer)
    label.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(text_image, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def click_start():
    global reps
    global check
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60, "Long Break")
        check = ""
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60, "Break")
        checkmark.config(text=check)
    else:
        count_down(WORK_MIN * 60, 'Work')
        check += "✔"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, work_title):
    global timer
    mins = count // 60
    secs = count % 60
    time_text = f"{mins}:{secs}"
    if mins < 10 and secs < 10:
        time_text = f"0{mins}:0{secs}"
    elif mins < 10:
        time_text = f"0{mins}:{secs}"
    elif secs < 10:
        time_text = f"{mins}:0{secs}"
    canvas.itemconfig(text_image, text=time_text)
    label.config(text=work_title)
    if count > 0:
        timer = window.after(1000, count_down, count - 1, work_title)
    else:
        click_start()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(row=0, column=1)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
text_image = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
start = tkinter.Button(text="start", command=click_start)
start.grid(row=2, column=0)
checkmark = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmark.grid(row=3, column=1)
reset = tkinter.Button(text="reset", command=click_reset)
reset.grid(row=2, column=2)

window.mainloop()
