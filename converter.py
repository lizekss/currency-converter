from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount):
        pass

    @abstractmethod
    def get_currencies():
        pass


class BasicConverter(CurrencyConverter):
    def __init__(self):
        self.rates = {'USD': 1, 'EUR': 0.9, 'GBP': 0.76, 'CAD': 1.36}

    def convert(self, from_currency, to_currency, amount):
        rate = self.rates[to_currency] / self.rates[from_currency]
        return rate * amount

    def get_currencies(self):
        return self.rates.keys()

