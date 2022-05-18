from tkinter import *

button_height = 1
button_width = 3

screen_width = 450
screen_height = 600

root = Tk()
root.title("Simple Calculator")
root.geometry(f"{screen_width}x{screen_height}")
root.maxsize(screen_width, screen_height)
root.minsize(screen_width, screen_height)
root.configure(background="gray")

sclvalue = StringVar()
sclvalue.set("")


def click_me(event):
    value = event.widget.cget("text")
    # print(value)
    if value == "=":

        try:
            if sclvalue.get().isdigit():
                finalvalue = int(sclvalue.get())
            else:
                finalvalue = eval(sclvalue.get())
                sclvalue.set(finalvalue)
                screen.update()
        except:
            sclvalue.set("Unknown error")
            screen.update()

    elif value == "<=":
        sclvalue.set(sclvalue.get()[:-1])
        screen.update()
    elif value == "1/x":
        if sclvalue.get().isdigit():
            val = int(sclvalue.get())
            sclvalue.set(1 / val)
            screen.update()
        else:
            sclvalue.set("Unknown error")
    elif value == "C":
        sclvalue.set("")
        screen.update()
    else:
        sclvalue.set(sclvalue.get() + value)
        screen.update()


screen = Entry(root, textvar=sclvalue, font="lucida 40 bold", justify=RIGHT)
screen.pack(fill=X, padx=5, pady=5)

valuelist = ["/", "%", "C", "<=", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "1/x", "0", ".", "="]

for i in range(20):

    if i % 4 == 0:
        frame = Frame(root, bg="gray")
        frame.pack()

    b = Button(frame, text=valuelist[i], height=button_height, width=button_width, font="ludida 35 bold")
    b.bind("<Button-1>", click_me)
    b.pack(side=LEFT, padx=3, pady=3)

root.mainloop()