import tkinter as tk
from todo.app import TodoApp
from calculator.app import CalculatorApp

class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TOOL LAUNCHER")
        self.geometry("300x200")

        tk.Label(self, text="Select the app", font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="Todo", font=("Arial", 12), command=self.launch_todo).pack(pady=5)
        tk.Button(self, text="Calculator", font=("Arial", 12), command=self.launch_calculator).pack(pady=5)

    def launch_todo(self):
        self.destroy()
        TodoApp().mainloop()

    def launch_calculator(self):
        self.destroy()
        CalculatorApp().mainloop()

if __name__ == "__main__":
    Launcher().mainloop()
