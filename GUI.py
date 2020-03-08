import barchart, stats
from VendingMachine import VendingMachine
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *

#Window initialization
window = tk.Tk()
window.title("Avira Vending Machine")
window.geometry('720x480')

#Global variables
vender = VendingMachine()

payment_method = tk.StringVar()
payment_method.set("Cash")

money_str = tk.StringVar()
money_str.set("0")

input_money = 0
input_bills = {
        "1":0, 
        "5":0, 
        "10":0, 
        "50":0, 
        "100":0}

product_names = [
        "Avira Prime",
        "Antivirus PRO",
        "Phantom VPN",
        "Password Manager",
        "Optimizer",
        "System Speedup"]

selected_product = tk.StringVar()
selected_product.set(product_names[0])

#Functions

#insert a 1$ bill in the vending machine
def add_bill1():
    global input_bills, input_money, money_syr
    input_money += 1
    money_str.set(str(int(money_str.get())+1))
    input_bills["1"] += 1

#insert a 5$ bill in the vending machine
def add_bill5():
    global input_bills, input_money, money_str
    input_money += 5
    money_str.set(str(int(money_str.get())+5))
    input_bills["5"] += 1

#insert a 10$ bill in the vending machine
def add_bill10():
    global input_bills, input_money, money_str
    input_money += 10
    money_str.set(str(int(money_str.get())+10))
    input_bills["10"] += 1

#insert a 50$ bill in the vending machine
def add_bill50():
    global input_bills, input_money, money_str
    input_money += 50
    money_str.set(str(int(money_str.get())+50))
    input_bills["50"] += 1

#insert a 100$ bill in the vending machine
def add_bill100():
    global input_bills, input_money, money_str
    input_money += 100
    money_str.set(str(int(money_str.get())+100))
    input_bills["100"] += 1

#check whether the slected product can be buyed and is in stock
def perform_payment():
    global payment_method, input_money, vender, selected_product, input_bills, money_str
   
    if(payment_method.get() == "Cash"):
        if(input_money < vender.price[selected_product.get()]): # check wheter or not the buyer has enough money
            messagebox.showinfo("Alert!", "Not enough money to buy {}".format(selected_product.get()))
            return

        payment_response, input_bills = vender.can_give_change(input_money, input_bills, selected_product.get())
        if(payment_response == 1): #case 1: transaction successful
            input_money -= vender.price[selected_product.get()]
            money_str.set(str(int(money_str.get()) - vender.price[selected_product.get()]))
            messagebox.showinfo("Ok, successfully bought {}".format(selected_product.get()), "Cash payment successful!")
        elif(payment_response == 0): # case 0: no possible change
            messagebox.showinfo("Alert!", "The vending machine can\'t give change!\nPlease change the payment method.")
        elif(payment_response == -1): #case -1: product out of stock
            messagebox.showinfo("Alert!", "Product {} out of stock!".format(selected_product.get()))
    else:
        payment_response = vender.buy_card(selected_product.get())
        if(payment_response == 1): #case 1: transaction successful
            messagebox.showinfo("Ok, successfully bought {}".format(selected_product.get()), "Card payment successful!")
        elif(payment_response == -1): #case -1: product out of stock
            messagebox.showinfo("Alert!", "Product {} out of stock!".format(selected_product.get()))

#return the change in the machine to the buyer
def get_change():
    global input_bills, input_money, money_str

    messagebox.showinfo("Ok!", "All change returned.")

    #reset money variables
    input_money = 0
    money_str.set("0")
    input_bills = {
        "1":0,
        "5":0,
        "10":0,
        "50":0,
        "100":0}

#generate statistics charts
def get_charts():
    messagebox.showinfo("Ok!", "Generated statistics!")
    stats.create_charts()

#Label declaration
product_txt = tk.Label(
        window, 
        text = "Select product you want to buy")
bill_txt = tk.Label(
        window, 
        text = "Select the ammount of cash to add")
money_txt = tk.Label(
        window, 
        text = "Total cash in vending machine")
method_txt = tk.Label(
        window, 
        text = "Choose payment method")
money_value = tk.Label(
        window, 
        textvariable = money_str) #money tracker

#Buttons declaration
#command buttons
generate_charts_button = tk.Button(
        window, 
        text = 'Generate charts', 
        command = get_charts) 
get_change_button = tk.Button(
        window, 
        text = 'Get change', 
        command = get_change) 
cancel_button = tk.Button(
        window, 
        text = 'Cancel', 
        command = window.destroy) 
buy_button = tk.Button(
        window, 
        text = 'Buy', 
        command = perform_payment) 

#bill buttons
bill1_button = tk.Button(
        window, 
        text = 'Add 1$', 
        command = add_bill1)
bill5_button = tk.Button(
        window, 
        text = 'Add 5$', 
        command = add_bill5)
bill10_button = tk.Button(
        window, 
        text = 'Add 10$', 
        command = add_bill10)
bill50_button = tk.Button(
        window, 
        text = 'Add 50$', 
        command = add_bill50)
bill100_button = tk.Button(
        window, 
        text = 'Add 100$', 
        command = add_bill100)

#Radiobutton declaration
#method of payment buttons
cash_rad = tk.Radiobutton(
        window, 
        text = "Cash", 
        variable = payment_method, 
        value = "Cash")
card_rad = tk.Radiobutton(
        window, 
        text = "Card", 
        variable = payment_method, 
        value = "Card")

#product selection buttons
prod0_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[0], vender.price[product_names[0]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[0])
prod1_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[1], vender.price[product_names[1]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[1])
prod2_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[2], vender.price[product_names[2]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[2])
prod3_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[3], vender.price[product_names[3]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[3])
prod4_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[4], vender.price[product_names[4]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[4])
prod5_ind = tk.Radiobutton(
        window, 
        text = "{} - {}$".format(product_names[5], vender.price[product_names[5]]), 
        variable = selected_product, 
        indicatoron = 0, 
        value = product_names[5])

#Place objects on GUI

bill_txt.place(
        anchor = tk.CENTER,
        relx = 0.75,
        rely = 0.1,
        relwidth = 0.4,
        relheight = 0.08)
bill1_button.place(
        anchor = tk.CENTER, 
        relx = 0.65, 
        rely = 0.2, 
        relwidth = 0.2, 
        relheight = 0.08)
bill5_button.place(
        anchor = tk.CENTER, 
        relx = 0.85, 
        rely = 0.2, 
        relwidth = 0.2, 
        relheight = 0.08)
bill10_button.place(
        anchor = tk.CENTER, 
        relx = 0.65, 
        rely = 0.28, 
        relwidth = 0.2, 
        relheight = 0.08)
bill50_button.place(
        anchor = tk.CENTER, 
        relx = 0.85, 
        rely = 0.28, 
        relwidth = 0.2, 
        relheight = 0.08)
bill100_button.place(
        anchor = tk.CENTER, 
        relx = 0.75, 
        rely = 0.36, 
        relwidth = 0.2, 
        relheight = 0.08)

product_txt.place(
        anchor = tk.CENTER,
        relx = 0.25,
        rely = 0.1,
        relwidth = 0.3,
        relheight = 0.08)
prod0_ind.place(
        anchor = tk.CENTER, 
        relx = 0.13, 
        rely = 0.2, 
        relwidth = 0.24, 
        relheight = 0.08)
prod1_ind.place(
        anchor = tk.CENTER, 
        relx = 0.37, 
        rely = 0.2, 
        relwidth = 0.24, 
        relheight = 0.08)
prod2_ind.place(
        anchor = tk.CENTER, 
        relx = 0.13, 
        rely = 0.28, 
        relwidth = 0.24, 
        relheight = 0.08)
prod3_ind.place(
        anchor = tk.CENTER, 
        relx = 0.37, 
        rely = 0.28, 
        relwidth = 0.24, 
        relheight = 0.08)
prod4_ind.place(
        anchor = tk.CENTER, 
        relx = 0.13, 
        rely = 0.36, 
        relwidth = 0.24, 
        relheight = 0.08)
prod5_ind.place(
        anchor = tk.CENTER, 
        relx = 0.37, 
        rely = 0.36, 
        relwidth = 0.24, 
        relheight = 0.08)

method_txt.place(
        anchor = tk.CENTER, 
        relx = 0.75, 
        rely = 0.45, 
        relwidth = 0.3, 
        relheight = 0.08)
cash_rad.place(
        anchor = tk.CENTER, 
        relx = 0.70, 
        rely = 0.5, 
        relwidth = 0.1, 
        relheight = 0.07)
card_rad.place(
        anchor = tk.CENTER, 
        relx = 0.80, 
        rely = 0.5, 
        relwidth = 0.1, 
        relheight = 0.07)

money_txt.place(
        anchor = tk.CENTER, 
        relx = 0.5, 
        rely = 0.75, 
        relwidth = 0.3, 
        relheight = 0.08)
money_value.place(
        anchor = tk.CENTER, 
        relx = 0.5, 
        rely = 0.8, 
        relwidth = 0.08, 
        relheight = 0.08)

cancel_button.place(
        anchor = tk.CENTER, 
        relx = 0.85, 
        rely = 0.9, 
        relwidth = 0.2, 
        relheight = 0.08)
buy_button.place(
        anchor = tk.CENTER, 
        relx = 0.15, 
        rely = 0.9, 
        relwidth = 0.2, 
        relheight = 0.08)
get_change_button.place(
        anchor = tk.CENTER, 
        relx = 0.5,
        rely = 0.9, 
        relwidth = 0.2, 
        relheight = 0.08)
generate_charts_button.place(
        anchor = tk.CENTER, 
        relx = 0.75, 
        rely = 0.6, 
        relwidth = 0.2, 
        relheight = 0.08)

window.mainloop()
