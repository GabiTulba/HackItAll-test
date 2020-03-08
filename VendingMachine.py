import json


class VendingMachine:

    # Type of bills that the vending machine has
    bills = ['1', '5', '10', '50', '100']

    def __init__(self):

        # Loading the stock of the products
        with open('stock.txt') as json_file:
            self.stock = json.load(json_file)

        # Loading the configuration of money in the machine
        with open('cash.txt') as json_file:
            self.noBills = json.load(json_file)

        # The configuration of money used for a purchase
        self.cashUsed = {}

        # Price of each type of product
        self.price = {
            "Avira Prime": 75,
            "Antivirus PRO": 35,
            "Phantom VPN": 50,
            "Password Manager": 20,
            "Optimizer": 10,
            "System Speedup": 25
        }

    # check if item is out os stock
    def out_of_stock(self, item):
        return self.stock[item] == 0

    # check the price of an item
    def get_price(self, item):
        return self.price[item]

    # update the stock and the configuration of money of the machine
    def update_jsons(self):
        with open('stock.txt', 'w') as json_file:
            json.dump(self.stock, json_file)

        with open('cash.txt', 'w') as json_file:
            json.dump(self.noBills, json_file)

    # create the log for the purchase
    def create_log(self, item, price, method, change):
        with open('log.json') as json_file:
            tmp = json.load(json_file)

        tmp["all_products"].append({
            "name": item,
            "price": price,
            "payment_method": method,
            "change": change
        })

        with open('log.json', 'w') as json_file:
            json.dump(tmp, json_file)

    # create the configuration of the change and return true if one exists
    def compute_change(self, sum):
        if sum == 0:
            return True

        i = len(self.bills) - 1
        while i >= 0 and (int(self.bills[i]) > sum or self.noBills[self.bills[i]] == 0):
            i -= 1

        if i == -1:
            return False

        if self.noBills[self.bills[i]] > sum // int(self.bills[i]):
            self.noBills[self.bills[i]] -= sum // int(self.bills[i])
            self.cashUsed[self.bills[i]] = sum // int(self.bills[i])
            return self.compute_change(sum - (sum // int(self.bills[i]) * int(self.bills[i])))
        else:
            self.cashUsed[self.bills[i]] = self.noBills[self.bills[i]]
            self.noBills[self.bills[i]] = 0
            return self.compute_change(sum - (self.cashUsed[self.bills[i]] * int(self.bills[i])))

    # check if the machine can give change to the sum inserted
    # returns -1 if out of stock, 0 if unable to give change, 1 for
    # transaction possible and the money configuration of the change
    def can_give_change(self, sum, input_bills, item):

        self.cashUsed = {
            "1": 0,
            "5": 0,
            "10": 0,
            "50": 0,
            "100": 0
        }

        # check if in stock
        if self.stock[item] == 0:
            return -1, self.cashUsed

        # update the money in the machine with the bills inserted
        for i in self.bills:
            if i in input_bills.keys():
                self.noBills[i] += input_bills[i]

        # check possible change
        if self.compute_change(sum - self.price[item]):
            self.stock[item] -= 1
            self.create_log(item, self.price[item], "cash", sum - self.price[item])
            flag = 1

        else:
            for i in self.bills:
                if i in input_bills.keys():
                    self.noBills[i] += input_bills[i]
            for i in self.bills:
                if i in self.cashUsed.keys():
                    self.noBills[i] += self.cashUsed[i]

            self.cashUsed = {
                "1": 0,
                "5": 0,
                "10": 0,
                "50": 0,
                "100": 0
            }

            flag = 0

        # update the data
        self.update_jsons()

        return flag, self.cashUsed

    # but with card
    def buy_card(self, item):
        if self.stock[item] == 0:
            return -1
        self.create_log(item, self.price[item], "card", 0)
        self.stock[item] -= 1
        return 1
