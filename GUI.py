import tkinter as tk
from tkinter import messagebox

#Functions
def performPayment():
    #TODO
    messagebox.showinfo("Ok", "Payment successfull")
    return

#Window Initialization
window = tk.Tk()
window.title("Avira Vending Machine")
window.geometry('720x480')

#Labels declaration
cashLabel = tk.Label(text = "Given Cash")
chooseLabel = tk.Label(text = "Choose A Product")

#

#Buttons declaration
cancelButton = tk.Button(window, text = 'Cancel', command = window.destroy)
buyButton = tk.Button(window, text = 'Buy', command = performPayment)

#Entries declaration
cashEntry = tk.Entry(window, width = 40)


#Place objects on GUI

cashLabel.place(anchor = tk.E, relx = 0.3, rely = 0.05)
cashEntry.place(anchor = tk.W, relx = 0.3, rely = 0.05)
cancelButton.place(anchor = tk.CENTER, relx = 0.85, rely = 0.9, width = 120, height = 45)
buyButton.place(anchor = tk.CENTER, relx = 0.15, rely = 0.9, width = 120, height = 45)

window.mainloop()
