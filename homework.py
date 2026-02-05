# Here's the Portfolio class, where is assigned the name, the stocks and the aim.
class Portfolio:
    def __init__(self, user):
        self.user = user
        self.stocks = {}
        self.aim = {}

    # Method to add stock to the portfolio.
    def add_stock(self, stock, percentage):
        self.stocks[stock] = percentage

    # Method to add stock aim to the portfolio.
    def add_aim(self, stock, percentage):
        self.aim[stock] = percentage

    # Method to get info about the portfolio.
    def info(self):
        print("Your actual stocks:")
        for stock in self.stocks:
            print(f"{stock.name}: {self.stocks[stock]}%.")
        print()
        print("Your portfolio aim:")
        for stock in self.aim:
            print(f"{stock.name}: {self.aim[stock]}%.")
        print()

    # Method to rebalance which stocks should be sold and wich ones shoul be bought.
    def rebalance(self):
        # The idea is to use buy_stocks to store the percentage that needs to be bought
        # per stock.
        buy_stocks = self.aim
        
        print("Sell this stocks:")

        # This for is used to show all the stocks that needs to be sold with their
        # respective percentages while also storing the stocks that needs to be sold.
        # The reason why using buy_stocks instead of self.aim directly is because
        # there can be a posibility that you need to sell a stock from the portafolio
        # aim and reasigned it to another stock, so the idea is not to modify the
        # "allocated" stocks.
        for stock in self.stocks:

            # Show the stock in terminal if it isn't in the portfolio aim.
            if stock not in self.aim:
                print(f"{stock.name}: {self.stocks[stock]}%")

            else:
                diff_percentage = abs(round(self.stocks[stock] - self.aim[stock], 1))

                # Show the stock in terminal if the stock is in the portfolio, but
                # has more percentage that it should have.
                if self.stocks[stock] > self.aim[stock]:
                    print(f"{stock.name}: {diff_percentage}%")
                    del buy_stocks[stock]

                # Store the stock in buy_stocks if the stock is in the portfolio,
                # but has less percentage that it should have.
                elif self.stocks[stock] < self.aim[stock]:
                    buy_stocks[stock] = diff_percentage

                # The stock is in the portfolio and has the exact percentage required.
                else:
                    del buy_stocks[stock]

        print("Buy this stocks:")

        # Show the stocks that needs to be bought with their respective percentages.
        for stock in buy_stocks:
            print(f"{stock.name}: {buy_stocks[stock]}")

# Here's the Stock class, where is assigned the name and the price. To make it easier, the
# full name was omitted. Also, here's where is assumed that the "Current Price" method is.
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def current_price(self, new_price):
        self.price = new_price

if __name__ == "__main__":

    # Defining stocks.
    nvidia = Stock("NVDA", 172.18)
    nasdaq = Stock("NDAQ", 86.8)
    intel = Stock("INTC", 47.08)
    spy = Stock("SPY", 676.94)
    amazon = Stock("AMZN", 222.77)
    apple = Stock("AAPL", 273.59)

    #Creating a portfolio
    portfolio = Portfolio("Nicolás Paz")

    #Simulating the portfolio distribution
    portfolio.add_stock(nvidia, 23.2)
    portfolio.add_stock(intel, 15.7)
    portfolio.add_stock(spy, 26.1)
    portfolio.add_stock(amazon, 18.4)
    portfolio.add_stock(apple, 16.6)

    #Simulating the portfolio aim
    portfolio.add_aim(nasdaq, 63)
    portfolio.add_aim(spy, 37)

    #Print the portfolio distribution and aim (Uncomment to view portfolio and aim in terminal)
    # portfolio.info()

    #Using rebalance method
    portfolio.rebalance()