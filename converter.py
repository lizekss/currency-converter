import tkinter as tk

class CurrencyConverter:
    rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.76, 'CAD': 1.27},
        'EUR': {'USD': 1.18, 'GBP': 0.89, 'CAD': 1.49},
        'GBP': {'USD': 1.32, 'EUR': 1.12, 'CAD': 1.68},
        'CAD': {'USD': 0.79, 'EUR': 0.67, 'GBP': 0.59}
    }

    def convert(self, from_currency, to_currency, amount):
        rate = self.rates[from_currency][to_currency]
        return rate * amount

def convert_currency():
    c = CurrencyConverter()
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_field.get())
    converted_amount = c.convert(from_currency, to_currency, amount)
    converted_amount_var.set(round(converted_amount, 2))

root = tk.Tk()

from_currency_var = tk.StringVar(root)
to_currency_var = tk.StringVar(root)
amount_field = tk.Entry(root)
converted_amount_var = tk.StringVar(root)

from_currency_var.set('USD')
to_currency_var.set('EUR')

from_currency_option = tk.OptionMenu(root, from_currency_var, 'USD', 'EUR', 'GBP', 'CAD')
to_currency_option = tk.OptionMenu(root, to_currency_var, 'USD', 'EUR', 'GBP', 'CAD')
convert_button = tk.Button(root, text="Convert", command=convert_currency)
converted_amount_label = tk.Label(root, textvariable=converted_amount_var)

amount_field.pack()
from_currency_option.pack()
to_currency_option.pack()
convert_button.pack()
converted_amount_label.pack()

root.mainloop()

