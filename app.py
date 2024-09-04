import tkinter as tk
from converter import CurrencyConverter


FROM_DEFAULT = 'USD'
TO_DEFAULT = 'EUR'

converter = CurrencyConverter()

def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_field.get())
    converted_amount = converter.convert(from_currency, to_currency, amount)
    converted_amount_var.set(round(converted_amount, 2))

def clear_fields():
    from_currency_var.set(FROM_DEFAULT)
    to_currency_var.set(TO_DEFAULT)
    amount_field.delete(0, tk.END)
    converted_amount_var.set('')

root = tk.Tk()

from_currency_var = tk.StringVar(root)
to_currency_var = tk.StringVar(root)
amount_field = tk.Entry(root)
converted_amount_var = tk.StringVar(root)

from_currency_var.set(FROM_DEFAULT)
to_currency_var.set(TO_DEFAULT)

from_currency_option = tk.OptionMenu(root, from_currency_var, *converter.get_currencies())
to_currency_option = tk.OptionMenu(root, to_currency_var, *converter.get_currencies())
convert_button = tk.Button(root, text="Convert", command=convert_currency)
clear_button = tk.Button(root, text="Clear", command=clear_fields)
converted_amount_label = tk.Label(root, textvariable=converted_amount_var)

amount_field.pack()
from_currency_option.pack()
to_currency_option.pack()
convert_button.pack()
clear_button.pack()
converted_amount_label.pack()

root.mainloop()

