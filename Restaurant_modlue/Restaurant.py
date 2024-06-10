import tkinter as tk
from tkinter import ttk, messagebox

def create_label_entry_pair(root, label_text, entry_var, row):
    label = ttk.Label(root, text=label_text)
    label.grid(row=row, column=0, padx=(10, 5), pady=5, sticky="e")
    entry = ttk.Entry(root, textvariable=entry_var, width=6)
    entry.grid(row=row, column=1, padx=(0, 10), pady=5, sticky="w")

def create_dropdown(root, label_text, options, row):
    label = ttk.Label(root, text=label_text)
    label.grid(row=row, column=0, padx=(10, 5), pady=5, sticky="e")
    selected_option = tk.StringVar()
    dropdown = ttk.OptionMenu(root, selected_option, options[0], *options)
    dropdown.grid(row=row, column=1, padx=(0, 10), pady=5, sticky="w")
    return selected_option

def create_radiobuttons(root, text1, text2, row):
    selected_option = tk.StringVar()
    ttk.Radiobutton(root, text=text1, variable=selected_option, value=text1).grid(row=row, column=0, padx=(0, 10), pady=5)
    ttk.Radiobutton(root, text=text2, variable=selected_option, value=text2).grid(row=row, column=1, pady=5)
    return selected_option

def create_checkboxes(root, text1, text2, row):
    extra_cheese_var = tk.IntVar()
    ttk.Checkbutton(root, text=text1, variable=extra_cheese_var).grid(row=row, column=0, padx=(10, 5), pady=5, sticky="w")
    extra_ketchup_var = tk.IntVar()
    ttk.Checkbutton(root, text=text2, variable=extra_ketchup_var).grid(row=row, column=1, padx=(0, 10), pady=5, sticky="w")
    return extra_cheese_var, extra_ketchup_var

def order_summary(pizza_quantity, pizza_size, burger_quantity, burger_size, soft_drink_quantity, extra_cheeses, extra_ketchup):
    
    def calculate_total_price(pizza_qty, pizza_size, burger_qty, burger_size, drinks_qty, extra_cheese, extra_ketchup):
        prices = {
            "Pizza": {"Small": 5, "Medium": 7, "Large": 10},
            "Burger": {"Classic": 5, "Big": 7},
            "Soft Drink": 2,
            "Extra Cheese": 1,
            "Extra Ketchup": 1
        }
        total = 0
        total += pizza_qty * prices["Pizza"][pizza_size]
        total += burger_qty * prices["Burger"][burger_size]
        total += drinks_qty * prices["Soft Drink"]
        if extra_cheese:
            total += prices["Extra Cheese"]
        if extra_ketchup:
            total += prices["Extra Ketchup"]
        return total

    total = calculate_total_price(pizza_quantity.get(), pizza_size.get(), burger_quantity.get(), burger_size.get(), soft_drink_quantity.get(), extra_cheeses.get(), extra_ketchup.get())
    message = f'''Pizza Quantity: {pizza_quantity.get()}  {pizza_size.get()}
Burger Quantity: {burger_quantity.get()}  {burger_size.get()}
Soft Drink Quantity: {soft_drink_quantity.get()}
Extra Cheese: {extra_cheeses.get()}
Extra Ketchup: {extra_ketchup.get()}
Total Price: {total}'''
    messagebox.showinfo('Order Summary', message)

root = tk.Tk()
root.title("Restaurant")

# Create a frame to contain all the elements
frame = ttk.Frame(root)
frame.pack(expand=True, fill="both", padx=20, pady=20)

row = 0

pizza_quantity_var = tk.IntVar()
create_label_entry_pair(frame, "Pizza Quantity:", pizza_quantity_var, row)
row += 1
pizza_size_var = create_dropdown(frame, "Pizza Size:", ["Large", "Medium", "Small"], row)
row += 1

burger_quantity_var = tk.IntVar()
create_label_entry_pair(frame, "Burger Quantity:", burger_quantity_var, row)
row += 1
burger_size_var = create_dropdown(frame, "Burger Size:", ["Classic", "Big"], row)
row += 1

soft_drinks_quantity_var = tk.IntVar()
create_label_entry_pair(frame, "Soft Drinks Quantity:", soft_drinks_quantity_var, row)
row += 1

order_type_var = create_radiobuttons(frame, "Take Away", "Dine", row)
row += 1

extra_cheese_var, extra_ketchup_var = create_checkboxes(frame, "Extra Cheese", "Extra Ketchup", row)


process_button = ttk.Button(frame, text="Submit", command=lambda: order_summary(pizza_quantity_var, pizza_size_var, burger_quantity_var, burger_size_var, soft_drinks_quantity_var, extra_cheese_var, extra_ketchup_var))
process_button.grid(row=row+1, columnspan=2, pady=10)

# Adjust the row and column weights to center the frame in the root window
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Center the frame in the root window
frame.grid(sticky="nsew")

root.mainloop()
