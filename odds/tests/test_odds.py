import unittest
from decimal import Decimal
from ..odds import Odds


class OddsTests(unittest.TestCase):
    
    def test_from_decimal(self):
        odds = Odds.from_decimal(Decimal('1.25'))
        self.assertEqual(Decimal('0.8'), odds.probability)
        self.assertRaises(ValueError, Odds.from_decimal, Decimal('0.99'))

    def test_from_fractional(self):
        odds = Odds.from_fractional(Decimal('3'), Decimal('2'))
        self.assertEqual(Decimal('0.4'), odds.probability)
        self.assertRaises(ValueError, Odds.from_fractional, Decimal('0'), Decimal('2'))

    def test_from_american(self):
        odds = Odds.from_american(Decimal('-150'))
        self.assertEqual(Decimal('0.6'), odds.probability)
        odds = Odds.from_american(Decimal('150'))
        self.assertEqual(Decimal('0.4'), odds.probability)
        self.assertRaises(ValueError, Odds.from_american, Decimal('-99'))
        self.assertRaises(ValueError, Odds.from_american, Decimal('99'))

    def test_to_decimal(self):
        odds = Odds(Decimal('0.8'))
        self.assertEqual(Decimal('1.25'), odds.to_decimal())

    def test_to_fractional(self):
        odds = Odds(Decimal('0.8'))
        numerator, denominator = odds.to_fractional()
        self.assertEqual(1, numerator)
        self.assertEqual(4, denominator)

    def test_to_american(self):
        odds = Odds(Decimal('0.6'))
        self.assertEqual(Decimal('-150'), odds.to_american())
        odds = Odds(Decimal('0.4'))
        self.assertEqual(Decimal('150'), odds.to_american())

    def test_win_from_wager(self):
        odds = Odds(Decimal('0.4'))
        self.assertEqual(Decimal('3'), odds.win_from_wager(Decimal('2')))
        odds = Odds(Decimal('0.6'))
        self.assertEqual(Decimal('1.33'), round(odds.win_from_wager(Decimal('2')), 2))

    def test_wager_to_win(self):
        odds = Odds(Decimal('0.6'))
        self.assertEqual(Decimal('3'), round(odds.wager_to_win(Decimal('2')), 2))

if __name__ == '__main__':
    unittest.main()

