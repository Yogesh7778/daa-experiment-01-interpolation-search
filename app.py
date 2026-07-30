import tkinter as tk
from tkinter import messagebox, ttk


def interpolation_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high and values[low] <= target <= values[high]:
        if values[low] == values[high]:
            return low if values[low] == target else -1
        position = low + (target - values[low]) * (high - low) // (values[high] - values[low])
        if values[position] == target:
            return position
        if values[position] < target:
            low = position + 1
        else:
            high = position - 1
    return -1


def search():
    try:
        values = sorted({int(number.strip()) for number in numbers_entry.get().split(",")})
        target = int(target_entry.get())
        if not values:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter comma-separated integers and a target integer.")
        return

    index = interpolation_search(values, target)
    array_label.config(text=f"Sorted array: {values}")
    result_label.config(text=f"{target} found at index {index}." if index >= 0 else f"{target} was not found.")


root = tk.Tk()
root.title("Interpolation Search")
root.resizable(False, False)
frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Interpolation Search", font=("Arial", 16, "bold")).grid(column=0, row=0, columnspan=2, pady=(0, 12))
ttk.Label(frame, text="Numbers (comma-separated):").grid(column=0, row=1, sticky="w", pady=4)
numbers_entry = ttk.Entry(frame, width=42)
numbers_entry.insert(0, "10, 20, 30, 40, 50, 60, 70")
numbers_entry.grid(column=1, row=1, pady=4)
ttk.Label(frame, text="Target:").grid(column=0, row=2, sticky="w", pady=4)
target_entry = ttk.Entry(frame, width=42)
target_entry.insert(0, "40")
target_entry.grid(column=1, row=2, pady=4)
ttk.Button(frame, text="Search", command=search).grid(column=0, row=3, columnspan=2, pady=12)
array_label = ttk.Label(frame, text="")
array_label.grid(column=0, row=4, columnspan=2)
result_label = ttk.Label(frame, text="Enter values and click Search.", font=("Arial", 11, "bold"))
result_label.grid(column=0, row=5, columnspan=2, pady=(8, 0))

root.mainloop()
