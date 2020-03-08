import json
import os
from barchart import *
dirname = os.path.dirname(__file__)

#a class for the products found in log.json
class Product:
    def __init__ (self, price, no_purchased, no_card, no_cash, change):
        self.price = price
        self.no_purchased = no_purchased
        self.no_cash = no_cash
        self.no_card = no_card
        self.change = change

#function that when called generates stats about the past transactions found in log.json
def create_charts():
    export_path = os.path.join(dirname, r"stats")
    if( os.path.exists(export_path) == False):
        os.mkdir(export_path)
    filename = os.path.join(dirname, 'log.json')
    with open(filename) as f:
        data = json.load(f)
    all_products = {}
    all_purchased = 0
    all_no_cash = 0
    all_no_card = 0
    all_change_given = 0
    all_money_earned = 0

    #populating the all_products list from the json file with all the transactions
    names = ["Avira Prime", "Antivirus PRO", "Phantom VPN", "Password Manager", "Optimizer", "System Speedup"]
    for current_name in names:
        all_products[current_name] = Product(0,0,0,0,0)
    for product in data["all_products"]:
        all_products[product["name"]].price = product["price"]
        all_products[product["name"]].no_purchased = all_products[product["name"]].no_purchased + 1
        all_products[product["name"]].change += int(product["change"])
        if product["payment_method"] == "cash":
            all_products[product["name"]].no_cash = all_products[product["name"]].no_cash + 1
            all_no_cash = all_no_cash + 1
            all_change_given += int(product["change"])
        else:
            all_products[product["name"]].no_card = all_products[product["name"]].no_card + 1
            all_no_card = all_no_card + 1
        all_purchased = all_purchased + 1
        all_money_earned += int(product["price"])
        
    #generating stats about the number of products purchased with card or cash
    all_payments = [all_no_cash, all_no_card]
    names = ["Cash", "Card"]
    colors = ['#BEEBE9', '#F4DADA']
    export_path_crt = os.path.join(export_path, "Cash vs Card")
    title = "Cash vs Card"
    make_barchart_percentage(all_payments, names, title, export_path_crt, colors)

    #generating stats about percentage of each product purchased
    all_products_purchased = []
    names = ["Avira Prime", "Antivirus PRO", "Phantom VPN", "Password Manager", "Optimizer", "System Speedup"]
    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B3C7BA', '#B28B90']
    for name in names:
        all_products_purchased.append(all_products[name].no_purchased)
    title = "Purchased Products Percentage"
    export_path_crt = os.path.join(export_path, title)
    names = ["Avira\nPrime", "Antivirus\n   PRO", "Phantom\n  VPN", "Password\nManager", "Optimizer", "System\nSpeedup"]
    make_barchart_percentage(all_products_purchased, names, title, export_path_crt, colors)

    #generating stats about number of dollars recieved vs number of dollars given as change
    all_values = [all_change_given, all_money_earned]
    names = ["Change\nGiven", "Money\nEarned"]
    title = "Earnings Details"
    export_path_crt = os.path.join(export_path, title)
    make_barchart_values(all_values, names, title, export_path_crt, colors)

    #generating stats about number of dollars received from each type of product
    all_values = []
    names = ["Avira Prime", "Antivirus PRO", "Phantom VPN", "Password Manager", "Optimizer", "System Speedup"]
    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B3C7BA', '#B28B90']
    for name in names:
        all_values.append(int(all_products[name].no_purchased) * int(all_products[name].price))
    title = "Purchased Products Earnings"
    export_path_crt = os.path.join(export_path, title)
    names = ["Avira\nPrime", "Antivirus\n   PRO", "Phantom\n  VPN", "Password\nManager", "Optimizer", "System\nSpeedup"]
    make_barchart_values(all_values, names, title, export_path_crt, colors)

    #generating stats about change received from each type of product 
    all_values = []
    names = ["Avira Prime", "Antivirus PRO", "Phantom VPN", "Password Manager", "Optimizer", "System Speedup"]
    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B3C7BA', '#B28B90']
    for name in names:
        all_values.append(int(all_products[name].change))
    title = "Purchased Products Change"
    export_path_crt = os.path.join(export_path, title)
    names = ["Avira\nPrime", "Antivirus\n   PRO", "Phantom\n  VPN", "Password\nManager", "Optimizer", "System\nSpeedup"]
    make_barchart_values(all_values, names, title, export_path_crt, colors)
        
