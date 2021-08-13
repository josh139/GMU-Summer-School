import tkinter

tk_window = tkinter.Tk()
tk_window.geometry("400x300")

tk_window.title("GUI")

def print_hello():
    print("Hello")

button = tkinter.Button(text="Say Hello",command=print_hello)
button.grid(column=0,row=1)

label = tkinter.Label(text="Hello There")
label.grid(column=0,row=2)
