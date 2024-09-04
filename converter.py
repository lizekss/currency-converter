import requests
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


class APIConverter(CurrencyConverter):
	def __init__(self):
		self.base_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1'
		self.base_curr = 'usd'

		rates_resp = requests.get(self.base_url + f'/currencies/{self.base_curr}.json')
		self.rates = rates_resp.json()[self.base_curr]

		currs_resp = requests.get(self.base_url + '/currencies.json')
		self.currs = currs_resp.json()

		if rates_resp.status_code != 200 or currs_resp.status_code != 200:
                        raise Exception('Failed to fetch data from API')

	def convert(self, from_currency, to_currency, amount):
		from_currency = from_currency.lower()
		to_currency = to_currency.lower()

		rate = self.rates[to_currency] / self.rates[from_currency]

		return rate * amount

	def get_currencies(self):
		return [curr.upper() for curr in self.currs.keys()]
