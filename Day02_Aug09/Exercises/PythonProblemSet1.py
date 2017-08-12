class Portfolio():
    def __init__(self, Cash = 0):
      self.Cash = Cash
      self.StockDictionary = {}
      self.OwnedStockDictionary = {}
      self.MFDict = {}
      self.History = []


    def addCash(self, NewCash):
     self.Cash = self.Cash + NewCash
     self.History.append("You added $ %.2f. You now have $ %.2f." %(NewCash, self.Cash))
     return "You added $ %.2f. You now have $ %.2f." %(NewCash, self.Cash)

    def withdrawCash(self, WithdrawlAmount):
      self.Cash = self.Cash - WithdrawlAmount
      self.History.append("You withdrew $ %.2f. You now have $ %.2f." %(WithdrawlAmount, self.Cash))
      return "You withdrew $ %.2f. You now have $ %.2f." %(WithdrawlAmount, self.Cash)


    def buyStock(self, amount, name):
      if self.Cash < float(name.price)* float(amount):
        return "Insufficient Funds"
      else:
        self.OwnedStockDictionary[name.StockSymbol] = amount
        self.StockDictionary[name.StockSymbol] = name.price
        self.Cash = self.Cash - name.price * (amount)
        self.History.append("You bought %s shares of %s. You have $ %.2f." %(amount, name.StockSymbol, self.Cash))
      return "You bought %s shares of %s. You have $ %.2f" %(amount, name.StockSymbol, self.Cash)


    def buyMutualFund(self, amount, name):
      if self.Cash < amount:
        return "Insufficient Funds"
      else:
        self.MFDict[name.MFName] = float(amount)
        self.Cash = self.Cash - float(amount)
        self.History.append("You bought %s shares of %s. You have $ %.2f" %(float(amount), name.MFName, self.Cash))
      return "You bought %s shares of %s. You have $ %.2f" %(float(amount), name.MFName, self.Cash)

    def sellMutualFund(self, name, amount):
        import random
        if amount <= self.MFDict[name]:
             self.MFDict[name] = round((self.MFDict[name] - amount), 2)
             price = round(random.uniform(.9, 1.2), 2)
             self.Cash = self.Cash + (price * float(amount))
             self.History.append("You sold %s shares of %s at $ %s. You have now have $ %.2f." %(float(amount), name, price, self.Cash))
             print "You sold %s shares of %s at $ %s. You have now have $ %.2f." %(float(amount), name, price, self.Cash)
        else:
            print "You don't have that much of that Mutual Fund"

    def sellStock(self, name, amount):
        if amount <= self.OwnedStockDictionary[name]:
            import random
            price = (round(random.uniform(.5,1.5), 2) * self.StockDictionary[name])
            self.Cash = self.Cash + (price * amount )
            self.OwnedStockDictionary[name] = self.OwnedStockDictionary[name] - amount
            self.History.append("You sold %s shares of %s at %s. You have $ %.2f.." %(amount, name, price, self.Cash))
            print "You sold %s shares of %s at %s. You have $ %.2f." %(amount, name, price, self.Cash)
        else:
            print "You don't have that much of that stock"

    def history(self):
        for elem in self.History:
            print elem

    def __str__(self):
        return "Cash: %.2f, \nStocks:%s,\nMutual Funds:%s" % (self.Cash, self.OwnedStockDictionary, self.MFDict)


class Stock(object):
    def __init__(self, price, StockSymbol):
        self.price = price
        self.StockSymbol = StockSymbol



class MutualFund(object):
    def __init__(self, MFName, price = 1):
        self.MFName = MFName
        self.price = price
