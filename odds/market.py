from decimal import Decimal


class MarketException(Exception):
    pass


class Market:

    def __init__(self):
        """Initialize with no sides and wagers"""
        self.sides = {}

    def add_side(self, side):
        """Add side to market"""
        if side.name in self.sides:
            raise MarketException('Side with name ' + side.name + ' already exists.')
        self.sides[side.name] = {
            'odds': side.odds,
            'wagers': []
        }

    def add_wager(self, side_name, wager):
        """Add a wager"""
        if side_name not in self.sides:
            raise MarketException('Side with name ' + side_name + ' does not exist for this market.')
        self.sides[side_name]['wagers'].append(wager)

    def overround(self):
        """Calculate overround based on implied probabilities"""
        total = 0
        for side in self.sides.values():
            total += side['odds'].probability
        return total - Decimal(1.0)

    def vigorish(self):
        """Vig as percentage"""
        overround = self.overround()
        return overround / (1 + overround)

    def handle(self):
        """Total wagers collected"""
        total = 0
        for side in self.sides.values():
            total += sum(side['wagers'])
        return total

    def total_payout(self, side_name):
        """Total amount paid out to all bettors for particular outcome"""
        if side_name not in self.sides:
            raise MarketException('Side with name ' + side_name + ' does not exist for this market.')
        wagered = sum(self.sides[side_name]['wagers'])
        winnings = self.sides[side_name]['odds'].win_from_wager(wagered)
        return wagered + winnings

    def gross_revenue(self, side_name):
        """Gross revenue from market, can be positive or negative"""
        if side_name not in self.sides:
            raise MarketException('Side with name ' + side_name + ' does not exist for this market.')
        return self.handle() - self.total_payout(side_name)
