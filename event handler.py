from tkinter import *

window = Tk()
window.title("event handler")
window.geometry("200x200")

def handle_keypress(event):
    """Print the character associated with the keypress"""
    print(event.char)

window.bind("<Key>" , handle_keypress)

def handle_click(event):
    print("button was clicked")
    
button = Button(text = "click me")
button.pack()
button.bind("<Button - 1>" , handle_click)
window.mainloop()
    