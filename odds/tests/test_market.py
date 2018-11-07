import unittest
from decimal import Decimal
from ..odds import Odds
from ..side import Side
from ..market import Market


class MarketTests(unittest.TestCase):

    def setUp(self):
        self.market = Market('Panthers @ Steelers moneyline')
        odds = Odds.from_american(Decimal(170))
        side = Side('Carolina Panthers', odds)
        self.market.add_side(side)
        odds = Odds.from_american(Decimal(-198))
        side = Side('Pittsburgh Steelers', odds)
        self.market.add_side(side)

    def test_overround(self):
        self.assertEqual(Decimal('0.0348'), round(self.market.overround(), 4))

    def test_vigorish(self):
        self.assertEqual(Decimal('0.0336'), round(self.market.vigorish(), 4))

    def test_handle(self):
        self.market.add_wager('Carolina Panthers', Decimal(200))
        self.market.add_wager('Pittsburgh Steelers', Decimal(300))
        self.assertEqual(Decimal(500), self.market.handle())

    def test_total_payout(self):
        self.market.add_wager('Carolina Panthers', Decimal(200))
        self.market.add_wager('Carolina Panthers', Decimal(100))
        self.market.add_wager('Pittsburgh Steelers', Decimal(300))
        self.assertEqual(Decimal(810), self.market.total_payout('Carolina Panthers'))

    def test_gross_revenue(self):
        self.market.add_wager('Carolina Panthers', Decimal(200))
        self.market.add_wager('Carolina Panthers', Decimal(100))
        self.market.add_wager('Pittsburgh Steelers', Decimal(300))
        self.assertEqual(Decimal('-210.00'), self.market.gross_revenue('Carolina Panthers'))
        self.assertEqual(Decimal('148.48'), self.market.gross_revenue('Pittsburgh Steelers'))

if __name__ == '__main__':
    unittest.main()
