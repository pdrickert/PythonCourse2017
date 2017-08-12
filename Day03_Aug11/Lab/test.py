class Portfolio():
    def __init__(self, Cash):
      self.Cash = Cash
      self.OwnedStockDictionary = {}
      self.MFList = []
      self.History = []


    def addCash(self, NewCash):
      self.Cash = float(self.Cash) + float(NewCash)
      self.History.append("You added $ %s. You now have $ %s" %(NewCash, self.Cash))
      return "You added $ %s. You now have $ %s" %(NewCash, self.Cash)

    def withdrawCash(self, WithdrawlAmount):
      self.Cash = float(self.Cash) - float(WithdrawlAmount)
      self.History.append("You withdrew $ %s. You now have $ %s" %(WithdrawlAmount, self.Cash))
      return "You withdrew $ %s. You now have $ %s" %(WithdrawlAmount, self.Cash)


    def buyStock(self, amount, name):
      if self.Cash < float(name.price)* float(amount):
        return "Insufficient Funds"
      else:
        self.OwnedStockDictionary[name.StockSymbol] = amount
        self.Cash = self.Cash - float(name.price)* float(amount)
        self.History.append("You bought %s shares of %s. You have $ %s" %(amount, name.StockSymbol, self.Cash))
      return "You bought %s shares of %s. You have $ %s" %(amount, name.StockSymbol, self.Cash)


    def buyMutualFund(self, name, amount):
      if self.Cash < amount:
        return "Insufficient Funds"
      else:
        self.MFDict[name] = amount
        self.Cash = self.Cash - float(amount)
        self.History.append("You bought %s shares of %s. You have $ %s" %(amount, name, self.Cash))
      return "You bought %s shares of %s. You have $ %s" %(amount, name, self.Cash)

    def sellMutualFund(self, name, amount):
        import random
        if amount <= self.MFDict[name]:
             self.MFDict[name] = int(self.MFDict[name]) - amount
             price = round(random.uniform(.9, 1.2), 2)
             self.Cash = self.Cash+ (price * amount)
             self.History.append("You sold %s shares of %s at $ %s. You have now have $ %s" %(amount, name, price, self.Cash))
             print "You sold %s shares of %s at $ %s. You have now have $ %s" %(amount, name, price, self.Cash)
        else:
            print "You don't have that much of that Mutual Fund"

    def sellStock(self, name, amount):
        if amount <= self.OwnedStockDictionary[name]:
            import random
            price = round(random.uniform(.5,1.5), 2)
            self.Cash = self.Cash + (price * amount * self.StockDictionary[name])
            self.OwnedStockDictionary[name] = self.OwnedStockDictionary[name] - amount
            self.History.append("You sold %s shares of %s at %s. You have $ %s." %(amount, name, price, self.Cash))
            print "You sold %s shares of %s at %s. You have $ %s." %(amount, name, price, self.Cash)
        else:
            print "You don't have that much of that stock"

def __str__(self):
    return self.Cash


class Stock(object):
    def __init__(self, price, StockSymbol):
        self.price = price
        self.StockSymbol = StockSymbol



class MutualFund(object):
    def __init__(self, name):
        self.name = name

    def buyMutualFund(self, name, amount):
      if self.Cash < amount:
        return "Insufficient Funds"
      else:
        self.MFDict[name] = amount
        self.Cash = self.Cash - float(amount)
        self.History.append("You bought %s shares of %s. You have $ %s" %(amount, name, self.Cash))
      return "You bought %s shares of %s. You have $ %s" %(amount, name, self.Cash)

        
