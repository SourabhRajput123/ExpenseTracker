import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")  # Set window size
        
        # Set background color
        self.root.configure(bg="#f0f0f0")
        
        self.expenses = []
        
        # Entry fields
        tk.Label(root, text="Amount:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Category:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", relief="flat")
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        
        self.stats_button = tk.Button(root, text="Show Stats", command=self.show_stats, bg="#FF5733", fg="white", relief="flat")
        self.stats_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_all, bg="#337ab7", fg="white", relief="flat")
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Display area
        self.expense_listbox = tk.Listbox(root, width=50, height=10)
        self.expense_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Separator
        ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Label for statistics
        self.stats_label = tk.Label(root, text="Statistics:", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.stats_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Total spent label
        self.total_spent_label = tk.Label(root, text="Total Spent: $0.00", bg="#f0f0f0", font=("Arial", 10))
        self.total_spent_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if amount and category:
            self.expenses.append((float(amount), category))
            self.expense_listbox.insert(tk.END, f"${amount} - {category}")
        else:
            messagebox.showerror("Error", "Please enter both amount and category.")

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def show_stats(self):
        if not self.expenses:
            messagebox.showinfo("Statistics", "No expenses to show.")
            return

        categories = {}
        total_spent = 0

        for amount, category in self.expenses:
            total_spent += amount
            categories[category] = categories.get(category, 0) + amount

        if categories:
            # Plot pie chart
            fig, ax = plt.subplots()
            ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title("Spending by Category")

            # Display total spent
            self.total_spent_label.config(text=f"Total Spent: ${total_spent:.2f}")

            # Show pie chart in Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        else:
            messagebox.showinfo("Statistics", "No expenses to show.")

    def clear_all(self):
        self.expenses = []
        self.expense_listbox.delete(0, tk.END)
        self.total_spent_label.config(text="Total Spent: $0.00")
        messagebox.showinfo("Clear All", "All expenses cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")  # Set window size
        
        # Set background color
        self.root.configure(bg="#f0f0f0")
        
        self.expenses = []
        
        # Entry fields
        tk.Label(root, text="Amount:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Category:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", relief="flat")
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        
        self.stats_button = tk.Button(root, text="Show Stats", command=self.show_stats, bg="#FF5733", fg="white", relief="flat")
        self.stats_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_all, bg="#337ab7", fg="white", relief="flat")
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Display area
        self.expense_listbox = tk.Listbox(root, width=50, height=10)
        self.expense_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Separator
        ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Label for statistics
        self.stats_label = tk.Label(root, text="Statistics:", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.stats_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Total spent label
        self.total_spent_label = tk.Label(root, text="Total Spent: $0.00", bg="#f0f0f0", font=("Arial", 10))
        self.total_spent_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if amount and category:
            self.expenses.append((float(amount), category))
            self.expense_listbox.insert(tk.END, f"${amount} - {category}")
        else:
            messagebox.showerror("Error", "Please enter both amount and category.")

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def show_stats(self):
        if not self.expenses:
            messagebox.showinfo("Statistics", "No expenses to show.")
            return

        categories = {}
        total_spent = 0

        for amount, category in self.expenses:
            total_spent += amount
            categories[category] = categories.get(category, 0) + amount

        if categories:
            # Plot pie chart
            fig, ax = plt.subplots()
            ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title("Spending by Category")

            # Display total spent
            self.total_spent_label.config(text=f"Total Spent: ${total_spent:.2f}")

            # Show pie chart in Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        else:
            messagebox.showinfo("Statistics", "No expenses to show.")

    def clear_all(self):
        self.expenses = []
        self.expense_listbox.delete(0, tk.END)
        self.total_spent_label.config(text="Total Spent: $0.00")
        messagebox.showinfo("Clear All", "All expenses cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
