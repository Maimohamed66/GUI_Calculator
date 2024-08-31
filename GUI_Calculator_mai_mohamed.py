import tkinter as tk

def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '(', ')'
]

row_val = 1
col_val = 0

for button in buttons:
    b = tk.Button(root, text=button, width=5, height=2, command=lambda b=button: click_button(b))
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add '=' button separately to have it on its own row
equal_button = tk.Button(root, text='=', width=5, height=2, command=calculate_result)
equal_button.grid(row=row_val, column=2, padx=5, pady=5)

# Swap the positions of clear and plus buttons
plus_button = tk.Button(root, text='+', width=5, height=2, command=lambda: click_button('+'))
plus_button.grid(row=row_val, column=3, padx=5, pady=5)

# Create the clear button and position it correctly
clear_button = tk.Button(root, text='C', width=5, height=2, command=clear_entry)
clear_button.grid(row=row_val, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
