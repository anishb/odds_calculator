from decimal import Decimal
from fractions import Fraction


class Odds:

    def __init__(self, implied_probability):
        """Initializer with implied probabilty"""
        self.probability = implied_probability

    @classmethod
    def from_decimal(cls, decimal_odds):
        """Initialize from decimal odds"""
        if decimal_odds < Decimal('1.0'):
            raise ValueError('Decimal odds must be greater than equal to 1')
        probability = Decimal(1.0) / decimal_odds
        return cls(probability)

    @classmethod
    def from_fractional(cls, numerator, denominator):
        """Initialize from fractional odds"""
        if numerator <= 0 or denominator <= 0:
            raise ValueError('Both numerator and denominator must be greater than 0')
        probability = denominator / (numerator + denominator)
        return cls(probability)

    @classmethod
    def from_american(cls, american_odds):
        """Initialize from american odds"""
        if -100 < american_odds < 100:
            raise ValueError('American odds must be <= -100 and >= 100')
        if american_odds < 0:
            probability = (-1 * american_odds) / ((-1 * american_odds) + 100)
        else:
            probability = 100 / (american_odds + 100)
        return cls(probability)

    def to_decimal(self):
        """Express as decimal odds"""
        return Decimal('1.0') / self.probability

    def to_fractional(self):
        """Express as fractional odds"""
        decimal = (Decimal('1.0') / self.probability) - Decimal('1.0')
        f = Fraction(decimal).limit_denominator(1000)
        return f.numerator, f.denominator

    def to_american(self):
        """Express as american odds"""
        if self.probability > 0.5:
            odds = -1 * (self.probability / (Decimal('1') - self.probability)) * Decimal('100')
        else:
            odds = (Decimal('1') - self.probability) / self.probability * Decimal('100')
        return odds

    def win_from_wager(self, wager):
        """Potential win from wager"""
        return wager * ((Decimal('1') / self.probability) - Decimal('1'))

    def wager_to_win(self, win):
        """Wager required to win"""
        return win / (Decimal('1.0') / self.probability - Decimal('1'))

