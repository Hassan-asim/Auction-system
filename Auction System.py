import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Auction System")

# Define global data structures
items = {}  # Dictionary to store item details
bids = {}  # Dictionary to store bids for each item

# Function to add an item
def add_item():
    item_number = item_number_entry.get()
    description = description_entry.get()
    reserve_price = reserve_price_entry.get()
    if not item_number.isdigit() or len(item_number) == 0:
        messagebox.showerror("Error", "Invalid item number. It must be a numeric value.")
        return
    if float(reserve_price) < 0:
        messagebox.showerror("Error", "Invalid reserve price. It must be a non-negative value.")
        return
    items[item_number] = {'description': description, 'reserve_price': float(reserve_price), 'number_of_bids': 0, 'highest_bid': 0, 'highest_bidder': None}
    bids[item_number] = []
    messagebox.showinfo("Success", f"Item {item_number} added successfully.")

# Function to place a bid
def place_bid():
    buyer_number = buyer_number_entry.get()
    item_number = bid_item_number_entry.get()
    bid_amount = float(bid_amount_entry.get())
    if item_number not in items:
        messagebox.showerror("Error", "Item does not exist.")
        return
    if bid_amount <= items[item_number]['highest_bid']:
        messagebox.showerror("Error", "Bid must be higher than the current highest bid.")
        return
    items[item_number]['number_of_bids'] += 1
    items[item_number]['highest_bid'] = bid_amount
    items[item_number]['highest_bidder'] = buyer_number
    bids[item_number].append((buyer_number, bid_amount))
    messagebox.showinfo("Success", f"Bid placed successfully by buyer {buyer_number} on item {item_number}.")

# Function to finalize the auction
def finalize_auction():
    total_fee = 0
    unsold_items = []
    no_bid_items = []
    for item_number, details in items.items():
        if details['number_of_bids'] == 0:
            no_bid_items.append(item_number)
        elif details['highest_bid'] >= details['reserve_price']:
            fee = details['highest_bid'] * 0.1
            total_fee += fee
        else:
            unsold_items.append((item_number, details['highest_bid']))
    sold_items_count = len(items) - len(unsold_items) - len(no_bid_items)
    messagebox.showinfo("Auction Results", f"Total fee from sold items: {total_fee}\nNumber of items sold: {sold_items_count}\nItems not meeting reserve price: {unsold_items}\nItems with no bids: {no_bid_items}")

# Create UI elements for adding items
item_number_label = tk.Label(root, text="Item Number:")
item_number_label.grid(row=0, column=0)
item_number_entry = tk.Entry(root)
item_number_entry.grid(row=0, column=1)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=1, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

reserve_price_label = tk.Label(root, text="Reserve Price:")
reserve_price_label.grid(row=2, column=0)
reserve_price_entry = tk.Entry(root)
reserve_price_entry.grid(row=2, column=1)

add_item_button = tk.Button(root, text="Add Item", command=add_item)
add_item_button.grid(row=3, column=0, columnspan=2)

# Create UI elements for placing bids
buyer_number_label = tk.Label(root, text="Buyer Number:")
buyer_number_label.grid(row=4, column=0)
buyer_number_entry = tk.Entry(root)
buyer_number_entry.grid(row=4, column=1)

bid_item_number_label = tk.Label(root, text="Item Number:")
bid_item_number_label.grid(row=5, column=0)
bid_item_number_entry = tk.Entry(root)
bid_item_number_entry.grid(row=5, column=1)

bid_amount_label = tk.Label(root, text="Bid Amount:")
bid_amount_label.grid(row=6, column=0)
bid_amount_entry = tk.Entry(root)
bid_amount_entry.grid(row=6, column=1)

place_bid_button = tk.Button(root, text="Place Bid", command=place_bid)
place_bid_button.grid(row=7, column=0, columnspan=2)

# Create UI elements for finalizing the auction
finalize_button = tk.Button(root, text="Finalize Auction", command=finalize_auction)
finalize_button.grid(row=8, column=0, columnspan=2)

# Run the application
root.mainloop()
