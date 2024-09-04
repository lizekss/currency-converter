class CurrencyConverter:
    rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.76, 'CAD': 1.27},
        'EUR': {'USD': 1.18, 'GBP': 0.89, 'CAD': 1.49},
        'GBP': {'USD': 1.32, 'EUR': 1.12, 'CAD': 1.68},
        'CAD': {'USD': 0.79, 'EUR': 0.67, 'GBP': 0.59}
    }

    def get_currencies(self):
        return self.rates.keys()

    def convert(self, from_currency, to_currency, amount):
        rate = self.rates[from_currency][to_currency]
        return rate * amount
