class SportsBook:

    def __init__(self):
        self.markets = {}

    def add_market(self, market):
        self.markets[market.name] = market

    def expected_value(self):
        pass

    def handle(self):
        return sum(market.handle() for market in self.markets.values())
