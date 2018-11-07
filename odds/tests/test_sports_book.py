import unittest
from decimal import Decimal
from ..odds import Odds
from ..side import Side
from ..market import Market
from ..book import SportsBook


class SportsBookTests(unittest.TestCase):

    def setUp(self):
        self.book = SportsBook()

        market = Market('Panthers @ Steelers moneyline')
        odds = Odds.from_american(Decimal(170))
        side = Side('Carolina Panthers', odds)
        market.add_side(side)
        odds = Odds.from_american(Decimal(-198))
        side = Side('Pittsburgh Steelers', odds)
        market.add_side(side)
        market.add_wager('Carolina Panthers', Decimal(200))
        market.add_wager('Carolina Panthers', Decimal(100))
        market.add_wager('Pittsburgh Steelers', Decimal(300))
        self.book.add_market(market)

        market = Market('Cardinals @ Chiefs moneyline')
        odds = Odds.from_american(Decimal(980))
        side = Side('Arizona Cardinals', odds)
        market.add_side(side)
        odds = Odds.from_american(Decimal(-1600))
        side = Side('Kansas City Chiefs', odds)
        market.add_side(side)
        market.add_wager('Arizona Cardinals', Decimal(200))
        market.add_wager('Arizona Cardinals', Decimal(200))
        market.add_wager('Kansas City Chiefs', Decimal(100))
        self.book.add_market(market)

    def test_handle(self):
        self.assertEqual(Decimal(1100), self.book.handle())


if __name__ == '__main__':
    unittest.main()
